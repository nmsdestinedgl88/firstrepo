from lib import *
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import ParagraphStyle
from PIL import Image
import statistics
OUT = '/home/user/firstrepo/memory-workbook/'
T = 'The 5-Minute Memory Workbook'
PAGES = 128; TRIM_W, TRIM_H, BLEED = 8.5, 11.0, 0.125
SPINE = PAGES * 0.002252
FW = 2*TRIM_W + SPINE + 2*BLEED; FH = TRIM_H + 2*BLEED
DPI = 300
print('spine in', round(SPINE,4), 'wrap in', round(FW,4), 'x', FH, 'px', round(FW*DPI), round(FH*DPI))
pw, ph = FW*72, FH*72
def prep(path, out):
    im = Image.open(path).convert('RGB'); w, h = im.size
    pan_w = (TRIM_W + BLEED) * DPI / 300  # inches
    target_ratio = (TRIM_W + BLEED) / FH
    tw = round(h * target_ratio); x0 = (w - tw) // 2
    im.crop((x0, 0, x0 + tw, h)).save(out)
    return im, x0, tw, h
fim, fx0, ftw, fh = prep(OUT + 'cover_memory-workbook.png', '/tmp/front_panel.png')
bim, bx0, btw, bh = prep(OUT + 'cover_memory-workbook_back.png', '/tmp/back_panel.png')
panel_w = (TRIM_W + BLEED) * 72
sp_w = SPINE * 72
# spine colour: median of front cover background (sample interior ruled-paper area)
px = fim.load(); samples = [px[x, y] for x in range(60, 400, 7) for y in range(40, 120, 7)]
bg = tuple(int(statistics.median(s[i] for s in samples)) for i in range(3))
print('spine bg', bg)
c = canvas.Canvas(OUT + 'cover_memory-workbook_wrap.pdf', pagesize=(pw, ph), initialFontName='Body', initialFontSize=12)
c.setTitle(T + ' wrap cover'); c.setAuthor('Cimple Books')
c.drawImage('/tmp/back_panel.png', 0, 0, panel_w, ph)
c.setFillColorRGB(*[v/255 for v in bg]); c.rect(panel_w, 0, sp_w, ph, stroke=0, fill=1)
c.drawImage('/tmp/front_panel.png', panel_w + sp_w, 0, panel_w, ph)
# back text, positioned inside the reserved panel (source px -> pts)
scale_pts = ph / bh   # points per source pixel
def src_x(xp): return ((xp - bx0) / btw) * panel_w
def src_y(yp): return ph - (yp / bh) * ph
px0, px1, py0, py1 = 270, 1290, 400, 1465   # reserved panel in source px
left, right, top, bottom = src_x(px0) + 26, src_x(px1) - 26, src_y(py0) - 24, src_y(py1) + 20
width = right - left
print('panel text box pts', round(width), round(top - bottom))
head = ParagraphStyle('bh', fontName='Body-B', fontSize=22, leading=25, textColor=INK, spaceAfter=7)
bod = ParagraphStyle('bb', fontName='Body', fontSize=12.5, leading=16.5, textColor=INK, spaceAfter=6)
bul = ParagraphStyle('bu', fontName='Body', fontSize=12, leading=15.5, textColor=INK, leftIndent=14, bulletIndent=2, spaceAfter=2)
note = ParagraphStyle('bn', fontName='Body-I', fontSize=11, leading=14, textColor=GREY, spaceBefore=6, spaceAfter=3)
imp = ParagraphStyle('bi', fontName='Body-B', fontSize=11, leading=14, textColor=GREEN)
story = [Paragraph('Forgot Why You Walked Into the Room?', head),
 Paragraph('Misplaced keys. A name on the tip of your tongue. A week of &ldquo;what was I about to do?&rdquo; Everyday forgetfulness is common in midlife, and small, steady habits are a practical place to start.', bod),
 Paragraph('<b>The 5-Minute Memory Workbook</b> is a six-week programme of tiny daily habits you can fit around a busy life. Each week adds one simple routine, with prompts, trackers and &ldquo;if this, then that&rdquo; planners to help it stick. No memory palaces. No gimmicks. Just five minutes a day.', bod)]
for b in ['A 6-week plan: one tiny habit per week', 'A self-check at the start and the end, so you can see your own progress',
          'Daily logs, trackers and weekly reflection pages', 'Habit-stacking planners built around your real routine', 'A plain-language page on when to talk to a doctor']:
    story.append(Paragraph(b, bul, bulletText='•'))
story += [Paragraph('A practical habit workbook, not medical advice.', note), Paragraph('Cimple Books &nbsp;|&nbsp; www.cimpledigital.com/books', imp)]
used = 0
for fl in story:
    _, h_ = fl.wrap(width, 9999); used += h_ + fl.style.spaceAfter + getattr(fl.style, 'spaceBefore', 0)
print('text height needed', round(used), 'available', round(top - bottom))
fr = Frame(left, bottom, width, top - bottom, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, showBoundary=0)
rest = fr.addFromList(story, c)
assert not story, 'back text overflowed panel'
# spine text (vector), reading top to bottom, inside 0.0625 in margins
cx = panel_w + sp_w / 2
c.saveState(); c.translate(cx, ph - 0.9*72); c.rotate(-90)
c.setFillColor(INK); c.setFont('Body-B', 10.5)
tw_ = c.stringWidth(T, 'Body-B', 10.5); c.drawString(0, -3.6, T)
c.setFont('Body', 9); c.setFillColor(GREEN)
imp_w = c.stringWidth('Cimple Books', 'Body', 9)
c.drawString(ph - 1.8*72 - imp_w, -3.1, 'Cimple Books')
c.restoreState()
c.showPage(); c.save()
print('spine title length in', round(tw_/72, 2), 'of', round((ph-1.8*72)/72, 2))
