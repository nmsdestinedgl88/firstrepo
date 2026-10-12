#!/usr/bin/env python3
"""Builds the KDP wrap-around cover (back | spine | front) at 300 dpi from the two accepted cover images.

Usage: python3 build_wrap.py FRONT.png BACK.png
Outputs in ./out: cover_raising-a-superhero_wrap.pdf / .png, cover_raising-a-superhero_wrap_proof.png
"""
import os, sys, re, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
FONTS = os.path.join(HERE, 'fonts')
for n, f in [('Cabin', 'Cabin-Regular'), ('Cabin-Bold', 'Cabin-Bold'), ('Cabin-Italic', 'Cabin-Italic'),
             ('Cabin-BoldItalic', 'Cabin-BoldItalic'), ('Baloo', 'Baloo2-ExtraBold')]:
    pdfmetrics.registerFont(TTFont(n, os.path.join(FONTS, f + '.ttf')))
pdfmetrics.registerFontFamily('Cabin', normal='Cabin', bold='Cabin-Bold', italic='Cabin-Italic', boldItalic='Cabin-BoldItalic')

GREEN = HexColor('#30A666'); INK = HexColor('#1F2A24')

# ---- KDP paperback wrap geometry (white paper), confirm in KDP's cover calculator
TRIM_W, TRIM_H, PAGES = 7.0, 10.0, 144
SPINE_IN = PAGES * 0.002252
BLEED = 0.125
DPI = 300
W_IN = 2 * TRIM_W + SPINE_IN + 2 * BLEED
H_IN = TRIM_H + 2 * BLEED
W_PX, H_PX = round(W_IN * DPI), round(H_IN * DPI)
SPINE_PX = round(SPINE_IN * DPI)
BACK_PX = round((TRIM_W + BLEED) * DPI)           # left bleed + back trim
FRONT_PX = W_PX - BACK_PX - SPINE_PX               # front trim + right bleed
PT = 72.0 / DPI


def cover_fit(im, tw, th):
    """Scale uniformly to cover (tw x th), centre-crop. Returns (image, scale, crop_x, crop_y)."""
    sc = max(tw / im.width, th / im.height)
    r = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    cx, cy = (r.width - tw) // 2, (r.height - th) // 2
    return r.crop((cx, cy, cx + tw, cy + th)), sc, cx, cy


def main(front_path, back_path):
    front = Image.open(front_path).convert('RGB')
    back = Image.open(back_path).convert('RGB')
    print('source px', front.size, back.size)
    eff = front.height / (H_IN)
    print(f'effective dpi of art at placed size: {eff:.0f}')

    # ---- patch the back cover's baked imprint (it overlaps the barcode zone) and retypeset it as vector text
    b = np.array(back).copy()
    b[1815:1918, 400:1000] = b[1705:1808, 400:1000]
    back = Image.fromarray(b)

    back_p, bsc, bcx, bcy = cover_fit(back, BACK_PX, H_PX)
    front_p, fsc, fcx, fcy = cover_fit(front, FRONT_PX, H_PX)

    # ---- spine: blend row by row between the neighbouring edge colours so there is no seam
    bl = np.array(back_p).astype(float)[:, -6:, :].mean(axis=1)
    fr = np.array(front_p).astype(float)[:, :6, :].mean(axis=1)
    blur = lambda a: np.array(Image.fromarray(a.astype('uint8')[None, :, :].repeat(3, 0)).filter(ImageFilter.GaussianBlur(25)))[0].astype(float)
    # simple vertical smoothing
    k = 61
    ker = np.ones(k) / k
    sm = lambda a: np.stack([np.convolve(np.pad(a[:, c], (k // 2, k // 2), mode='edge'), ker, mode='valid') for c in range(3)], axis=1)
    bl, fr = sm(bl), sm(fr)
    t = np.linspace(0, 1, SPINE_PX)[None, :, None]
    spine = (bl[:, None, :] * (1 - t) + fr[:, None, :] * t).clip(0, 255).astype('uint8')
    spine_img = Image.fromarray(spine)

    # ---- flat raster composite (artwork only); vector text is added in the PDF
    canvas_img = Image.new('RGB', (W_PX, H_PX), (255, 255, 255))
    canvas_img.paste(back_p, (0, 0)); canvas_img.paste(spine_img, (BACK_PX, 0)); canvas_img.paste(front_p, (BACK_PX + SPINE_PX, 0))
    art_path = os.path.join(OUT, '_wrap_art.png'); canvas_img.save(art_path, dpi=(DPI, DPI))

    # ---- PDF with vector text
    pdf_path = os.path.join(OUT, 'cover_raising-a-superhero_wrap.pdf')
    c = canvas.Canvas(pdf_path, pagesize=(W_IN * 72, H_IN * 72))
    c.setTitle('Raising a Superhero - wrap cover'); c.setAuthor('Cimple Books')
    c.drawImage(art_path, 0, 0, W_IN * 72, H_IN * 72)
    PH = H_IN * 72

    # back panel (measured on the source art, mapped through the scale and crop)
    def mapx(x): return (x * bsc - bcx) * PT
    def mapy(y): return PH - (y * bsc - bcy) * PT
    px0, px1, py0, py1 = mapx(191), mapx(1212), mapy(257), mapy(1105)
    pad = 24
    tw = px1 - px0 - 2 * pad; th = py0 - py1 - 2 * pad

    def tc(s): return re.sub(r"(?<![\w'’])([a-z])", lambda m: m.group(1).upper(), s)
    head = tc('Their Biggest Challenges May Be Hiding Their Biggest Strengths.')
    blurb = ("Intense focus. Endless energy. Racing ideas. Big feelings. Many kids with ADHD have traits that cause friction at home "
             "and could grow into real strengths. <b>Raising a Superhero</b> gives you simple things to do about it, plus a way to keep "
             "your own patience from running dry.")
    bullets = ['40 simple missions to do together, mostly 10 to 20 minutes each, with little or no prep',
               '8 modules: Deep Focus, Active Power, Spark Ideas, Big Heart, Wide Radar, Sidekick Systems, Learning Style, Allies and Comebacks',
               'A one-minute Guardian Pause in every mission to build your patience',
               'Ready-to-use phrases, a Patience Toolkit, a Phrase Bank, a 30-Day Tracker and a Wins Log']

    def build(s):
        hs = ParagraphStyle('h', fontName='Baloo', fontSize=19 * s, leading=22 * s, textColor=GREEN)
        bs = ParagraphStyle('b', fontName='Cabin', fontSize=10.6 * s, leading=14.2 * s, textColor=INK)
        ls = ParagraphStyle('l', parent=bs, fontSize=10 * s, leading=13.4 * s, leftIndent=12, bulletIndent=0)
        flow = [(Paragraph(head, hs), 8), (Paragraph(blurb, bs), 9)]
        for t_ in bullets: flow.append((Paragraph(t_, ls, bulletText='•'), 3.5))
        return flow
    for s in (1.12, 1.08, 1.04, 1.0, 0.96, 0.92, 0.88, 0.84):
        flow = build(s)
        tot = sum(p.wrap(tw, 1000)[1] + g for p, g in flow)
        if tot <= th: break
    else:
        raise SystemExit('back text does not fit the panel')
    print(f'back text scale {s}, uses {tot:.0f} of {th:.0f} pt')
    y = py0 - pad - (th - tot) / 2 * 0.8
    for p, g in flow:
        ph = p.wrap(tw, 1000)[1]; p.drawOn(c, px0 + pad, y - ph); y -= ph + g

    # non-medical line below the panel, on the green
    c.setFillColor(white); c.setFont('Cabin', 9.2)
    mid = mapx(700)
    for i, line in enumerate(['Non-medical family activities.', 'Not a substitute for professional advice.']):
        c.drawCentredString(mid, mapy(1215) - i * 12, line)

    # retypeset imprint (the baked one was patched out), kept clear of the barcode zone
    cx_img = 640
    c.setFont('Cabin-Bold', 15); c.drawCentredString(mapx(cx_img), mapy(1855), 'Cimple Books')
    c.setFont('Cabin', 13.2); c.drawCentredString(mapx(cx_img), mapy(1905), 'www.cimpledigital.com/books')

    # spine text (KDP allows spine text at 79+ pages; safe width = spine - 2 x 0.0625 in)
    sx = (BACK_PX + SPINE_PX / 2) * PT
    safe = SPINE_IN * 72 - 2 * 0.0625 * 72
    c.saveState(); c.setFillColor(white)
    c.translate(sx, PH - (BLEED * 72 + 26)); c.rotate(-90)
    c.setFont('Baloo', 11); c.drawString(0, -3.6, 'Raising a Superhero')
    c.restoreState()
    c.saveState(); c.setFillColor(white)
    wimp = pdfmetrics.stringWidth('Cimple Books', 'Cabin-Bold', 9)
    c.translate(sx, BLEED * 72 + 26 + wimp); c.rotate(-90)
    c.setFont('Cabin-Bold', 9); c.drawString(0, -3.1, 'Cimple Books')
    c.restoreState()
    print(f'spine {SPINE_IN:.4f} in ({SPINE_IN * 25.4:.1f} mm); safe text height {safe:.1f} pt; title 11pt, imprint 9pt')
    c.showPage(); c.save()

    # ---- PNG at 300 dpi + proof
    png = os.path.join(OUT, 'cover_raising-a-superhero_wrap')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-png', '-singlefile', pdf_path, png], check=True)
    flat = Image.open(png + '.png')
    if flat.size != (W_PX, H_PX): flat = flat.crop((0, 0, W_PX, H_PX)); flat.save(png + '.png', dpi=(DPI, DPI))
    print('wrap png', flat.size, 'expected', (W_PX, H_PX))
    proof = flat.copy().resize((W_PX // 3, H_PX // 3)); d = ImageDraw.Draw(proof)
    s3 = DPI / 3.0
    def X(inches): return inches * s3
    tx0, tx1 = BLEED, W_IN - BLEED; ty0, ty1 = BLEED, H_IN - BLEED
    d.rectangle([X(tx0), X(ty0), X(tx1), X(ty1)], outline=(255, 0, 0), width=2)               # trim
    d.line([X(BLEED + TRIM_W), 0, X(BLEED + TRIM_W), proof.height], fill=(0, 90, 255), width=2)   # spine left edge
    d.line([X(BLEED + TRIM_W + SPINE_IN), 0, X(BLEED + TRIM_W + SPINE_IN), proof.height], fill=(0, 90, 255), width=2)
    m = 0.125                                                                                    # safe margin
    d.rectangle([X(tx0 + m), X(ty0 + m), X(BLEED + TRIM_W - m), X(ty1 - m)], outline=(0, 160, 0), width=1)
    d.rectangle([X(BLEED + TRIM_W + SPINE_IN + m), X(ty0 + m), X(tx1 - m), X(ty1 - m)], outline=(0, 160, 0), width=1)
    bx1 = BLEED + TRIM_W - 0.25; bx0 = bx1 - 2.0; by1 = H_IN - BLEED - 0.25; by0 = by1 - 1.2                # barcode zone
    d.rectangle([X(bx0), X(by0), X(bx1), X(by1)], outline=(255, 0, 255), width=3)
    d.text((X(bx0) + 4, X(by0) + 4), 'KDP barcode zone 2 x 1.2 in', fill=(255, 0, 255))
    proof.save(os.path.join(OUT, 'cover_raising-a-superhero_wrap_proof.png'))
    os.remove(art_path)
    print('done')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
