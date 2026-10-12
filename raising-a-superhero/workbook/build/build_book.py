#!/usr/bin/env python3
"""Builds the Raising a Superhero interior (7 x 10 in, 144 pages) from the markdown in ../content.

Usage: python3 build_book.py [--cover path/to/front.png]
Outputs (in ./out):
  raising-a-superhero_print_interior.pdf   144 pages, no cover (for KDP)
  raising-a-superhero_digital.pdf          cover + 144 pages (only if --cover is given)
  page_map.json                            page number -> section, font scale used
"""
import re, os, sys, json, glob
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white, Color
from reportlab.platypus import Paragraph, Table, TableStyle

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, '..', 'content')
FONTS = os.path.join(HERE, 'fonts')
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)

for name, f in [('Cabin', 'Cabin-Regular'), ('Cabin-Bold', 'Cabin-Bold'), ('Cabin-Italic', 'Cabin-Italic'),
                ('Cabin-BoldItalic', 'Cabin-BoldItalic'), ('Baloo', 'Baloo2-ExtraBold')]:
    pdfmetrics.registerFont(TTFont(name, os.path.join(FONTS, f + '.ttf')))
pdfmetrics.registerFontFamily('Cabin', normal='Cabin', bold='Cabin-Bold', italic='Cabin-Italic', boldItalic='Cabin-BoldItalic')


def mix(c1, c2, t):
    return Color(c1.red * (1 - t) + c2.red * t, c1.green * (1 - t) + c2.green * t, c1.blue * (1 - t) + c2.blue * t)


GREEN = HexColor('#30A666')
LIGHT = HexColor('#56CB87')
TINT = HexColor('#F3F9F5')
INK = HexColor('#1F2A24')
MUTED = HexColor('#52625A')
LINE = mix(LIGHT, white, 0.45)
LINE_DARK = mix(LIGHT, white, 0.1)

PW, PH = 504, 720
CW = 408
TOP, BOTTOM = 666, 56
BASE = 12.5


# ----------------------------------------------------------------------------- text helpers
def tc(s):
    """Title-case: capitalise the first letter of every word."""
    return re.sub(r"(?<![\w'’])([a-z])", lambda m: m.group(1).upper(), s)


def fmt(s):
    s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', s)
    s = re.sub(r'"([^"]*)"', '“\\1”', s)
    s = re.sub(r"(\w)'(\w)", '\\1’\\2', s)
    s = re.sub(r"(\w)'(?=[\s.,;:!?)]|$)", '\\1’', s)
    return s.replace("'", '’')


def styles(s):
    b = BASE * s
    d = {}
    d['body'] = ParagraphStyle('body', fontName='Cabin', fontSize=b, leading=b * 1.36, textColor=INK)
    d['body_i'] = ParagraphStyle('bi', parent=d['body'], fontName='Cabin-Italic')
    d['small'] = ParagraphStyle('small', parent=d['body'], fontSize=b * 0.86, leading=b * 0.86 * 1.32)
    d['label'] = ParagraphStyle('label', parent=d['body'], fontName='Cabin-Bold', fontSize=b * 0.92, leading=b * 0.92 * 1.28)
    d['cell'] = ParagraphStyle('cell', parent=d['body'], fontSize=b * 0.8, leading=b * 0.8 * 1.28)
    d['cell_b'] = ParagraphStyle('cellb', parent=d['cell'], fontName='Cabin-Bold')
    d['cell_l'] = ParagraphStyle('celll', parent=d['body'], fontSize=b * 0.88, leading=b * 0.88 * 1.3)
    d['cell_b_l'] = ParagraphStyle('cellbl', parent=d['cell_l'], fontName='Cabin-Bold')
    d['th'] = ParagraphStyle('th', parent=d['cell'], fontName='Cabin-Bold', textColor=white)
    d['h1'] = ParagraphStyle('h1', fontName='Baloo', fontSize=23 * s, leading=25 * s, textColor=GREEN)
    d['h2'] = ParagraphStyle('h2', fontName='Baloo', fontSize=13.5 * s, leading=15 * s, textColor=GREEN)
    d['quote'] = ParagraphStyle('quote', parent=d['body'], fontName='Cabin-Italic', textColor=INK)
    d['pull'] = ParagraphStyle('pull', fontName='Baloo', fontSize=15.5 * s, leading=19 * s, textColor=GREEN, alignment=1)
    d['mtitle'] = ParagraphStyle('mtitle', fontName='Baloo', fontSize=36 * s, leading=40 * s, textColor=GREEN)
    d['msub'] = ParagraphStyle('msub', fontName='Cabin-Italic', fontSize=13.5 * s, leading=18 * s, textColor=MUTED)
    d['kick'] = ParagraphStyle('kick', fontName='Baloo', fontSize=11 * s, leading=13 * s, textColor=GREEN)
    d['band_t'] = ParagraphStyle('bandt', fontName='Baloo', fontSize=17 * s, leading=19 * s, textColor=white)
    d['band_k'] = ParagraphStyle('bandk', fontName='Cabin-Bold', fontSize=8.5 * s, leading=10 * s, textColor=mix(TINT, GREEN, 0.05))
    d['meta'] = ParagraphStyle('meta', fontName='Cabin', fontSize=9.5 * s, leading=12 * s, textColor=MUTED)
    return d


# ----------------------------------------------------------------------------- icons
def icon(c, kind, cx, cy, r=6.5):
    c.saveState()
    c.setStrokeColor(GREEN); c.setFillColor(GREEN); c.setLineWidth(1.3)
    if kind == 'idea':
        c.circle(cx, cy + 1.2, r * 0.62, stroke=1, fill=0)
        c.rect(cx - r * 0.3, cy - r * 0.78, r * 0.6, r * 0.34, stroke=0, fill=1)
        for a in (-0.9, 0, 0.9):
            import math
            c.line(cx + math.sin(a) * r * 0.85, cy + 1.2 + math.cos(a) * r * 0.85,
                   cx + math.sin(a) * r * 1.15, cy + 1.2 + math.cos(a) * r * 1.15)
    elif kind == 'steps':
        for i, yy in enumerate((cy + 4, cy, cy - 4)):
            c.circle(cx - r * 0.7, yy, 1.1, stroke=0, fill=1)
            c.line(cx - r * 0.3, yy, cx + r * 0.9, yy)
    elif kind == 'say':
        c.roundRect(cx - r, cy - r * 0.55, r * 2, r * 1.35, 3, stroke=1, fill=0)
        p = c.beginPath(); p.moveTo(cx - r * 0.5, cy - r * 0.55); p.lineTo(cx - r * 0.7, cy - r * 1.05); p.lineTo(cx - r * 0.05, cy - r * 0.55)
        c.drawPath(p, stroke=0, fill=1)
    elif kind == 'notice':
        c.ellipse(cx - r, cy - r * 0.55, cx + r, cy + r * 0.55, stroke=1, fill=0)
        c.circle(cx, cy, r * 0.28, stroke=0, fill=1)
    elif kind == 'pause':
        c.circle(cx, cy, r * 0.95, stroke=0, fill=1)
        c.setFillColor(white)
        c.rect(cx - r * 0.38, cy - r * 0.42, r * 0.22, r * 0.84, stroke=0, fill=1)
        c.rect(cx + r * 0.16, cy - r * 0.42, r * 0.22, r * 0.84, stroke=0, fill=1)
    elif kind == 'retry':
        c.arc(cx - r * 0.8, cy - r * 0.8, cx + r * 0.8, cy + r * 0.8, 40, 270)
        p = c.beginPath(); p.moveTo(cx + r * 0.45, cy + r * 0.95); p.lineTo(cx + r * 1.05, cy + r * 0.3); p.lineTo(cx + r * 0.0, cy + r * 0.45)
        c.drawPath(p, stroke=0, fill=1)
    elif kind == 'star':
        import math
        p = c.beginPath()
        for i in range(10):
            ang = math.pi / 2 + i * math.pi / 5
            rr = r if i % 2 == 0 else r * 0.45
            x, y = cx + rr * math.cos(ang), cy + rr * math.sin(ang)
            (p.moveTo if i == 0 else p.lineTo)(x, y)
        p.close(); c.drawPath(p, stroke=0, fill=1)
    c.restoreState()


HEADERS = []  # every header-like string, checked in qa()


# ----------------------------------------------------------------------------- blocks
class B:
    units = 0
    extra = 0

    def h(self, w): return 0

    def draw(self, c, x, y, w): pass


class Spacer(B):
    def __init__(s, hh): s.hh = hh
    def h(s, w): return s.hh


class Para(B):
    def __init__(s, text, st, sb=0, sa=6, indent=0, raw=False):
        s.p = Paragraph(text if raw else fmt(text), st); s.sb = sb; s.sa = sa; s.indent = indent

    def h(s, w):
        return s.sb + s.p.wrap(w - s.indent, 10000)[1] + s.sa

    def draw(s, c, x, y, w):
        ph = s.p.wrap(w - s.indent, 10000)[1]
        s.p.drawOn(c, x + s.indent, y - s.sb - ph)


class Heading(B):
    def __init__(s, text, st, ic=None, sb=8, sa=5, rule=True):
        s.text = tc(text); s.st = st; s.ic = ic; s.sb = sb; s.sa = sa; s.rule = rule; HEADERS.append(('heading', s.text, st.fontSize))
        s.p = Paragraph(fmt(s.text), st)

    def h(s, w):
        off = 20 if s.ic else 0
        return s.sb + s.p.wrap(w - off, 1000)[1] + (4 if s.rule else 0) + s.sa

    def draw(s, c, x, y, w):
        off = 20 if s.ic else 0
        ph = s.p.wrap(w - off, 1000)[1]
        s.p.drawOn(c, x + off, y - s.sb - ph)
        if s.ic:
            icon(c, s.ic, x + 8, y - s.sb - ph / 2 - 0.5)
        if s.rule:
            c.setStrokeColor(LINE); c.setLineWidth(0.8)
            c.line(x, y - s.sb - ph - 3, x + w, y - s.sb - ph - 3)


class Bullets(B):
    def __init__(s, items, st, kind='bullet', gap=3.5, sa=6):
        s.items = [Paragraph(fmt(i), st) for i in items]; s.kind = kind; s.gap = gap; s.sa = sa; s.st = st

    def h(s, w):
        return sum(p.wrap(w - 20, 1000)[1] + s.gap for p in s.items) + s.sa

    def draw(s, c, x, y, w):
        fs = s.st.fontSize
        for i, p in enumerate(s.items, 1):
            ph = p.wrap(w - 20, 1000)[1]
            p.drawOn(c, x + 20, y - ph)
            my = y - fs * 0.68
            if s.kind == 'bullet':
                c.setFillColor(GREEN); c.circle(x + 6, my, 2.2, stroke=0, fill=1)
            elif s.kind == 'number':
                c.setFillColor(GREEN); c.setFont('Baloo', fs * 1.0); c.drawString(x + 1, y - fs * 0.95, f'{i}.')
            else:
                c.setStrokeColor(GREEN); c.setLineWidth(1.1); c.roundRect(x + 1, my - 4.5, 9, 9, 2, stroke=1, fill=0)
            y -= ph + s.gap


class QuoteBox(B):
    def __init__(s, lines, st):
        s.ps = [Paragraph(fmt(l), st) for l in lines]; s.pad = 8

    def h(s, w):
        return 2 * s.pad + sum(p.wrap(w - 2 * s.pad - 8, 1000)[1] + 3 for p in s.ps) - 3 + 6

    def draw(s, c, x, y, w):
        hh = s.h(w) - 6
        c.setFillColor(TINT); c.setStrokeColor(LINE); c.setLineWidth(0.8)
        c.roundRect(x, y - hh, w, hh, 6, stroke=1, fill=1)
        c.setFillColor(LIGHT); c.roundRect(x, y - hh, 4, hh, 2, stroke=0, fill=1)
        yy = y - s.pad
        for p in s.ps:
            ph = p.wrap(w - 2 * s.pad - 8, 1000)[1]
            p.drawOn(c, x + s.pad + 6, yy - ph); yy -= ph + 3


class Box(B):
    def __init__(s, blocks, fill=TINT, stroke=LIGHT, pad=9, sa=8):
        s.blocks = blocks; s.fill = fill; s.stroke = stroke; s.pad = pad; s.sa = sa

    @property
    def units(s): return sum(b.units for b in s.blocks)

    def set_extra(s, e):
        for b in s.blocks: b.extra = e if b.units else 0

    def inner(s, w): return sum(b.h(w - 2 * s.pad) for b in s.blocks)

    def h(s, w): return s.inner(w) + 2 * s.pad + s.sa

    def draw(s, c, x, y, w):
        hh = s.inner(w) + 2 * s.pad
        c.setFillColor(s.fill); c.setStrokeColor(s.stroke); c.setLineWidth(1.2)
        c.roundRect(x, y - hh, w, hh, 7, stroke=1, fill=1)
        yy = y - s.pad
        for b in s.blocks:
            b.draw(c, x + s.pad, yy, w - 2 * s.pad); yy -= b.h(w - 2 * s.pad)


class PullQuote(B):
    def __init__(s, text, st):
        s.p = Paragraph(fmt(text), st)

    def h(s, w): return s.p.wrap(w - 60, 1000)[1] + 34 + 8

    def draw(s, c, x, y, w):
        ph = s.p.wrap(w - 60, 1000)[1]; hh = ph + 34
        c.setFillColor(TINT); c.setStrokeColor(LIGHT); c.setLineWidth(1.2); c.roundRect(x, y - hh, w, hh, 9, stroke=1, fill=1)
        icon(c, 'star', x + 18, y - hh / 2, 6)
        icon(c, 'star', x + w - 18, y - hh / 2, 6)
        s.p.drawOn(c, x + 30, y - 17 - ph)


class Band(B):
    def __init__(s, kicker, title, st):
        s.k = Paragraph(fmt(tc(kicker)).upper(), st['band_k']); s.t = tc(title); s.st = st; HEADERS.append(('band', s.t, 17)); HEADERS.append(('kicker', tc(kicker), 8.5))

    def h(s, w): return 54

    def draw(s, c, x, y, w):
        c.setFillColor(GREEN); c.roundRect(x, y - 48, w, 48, 9, stroke=0, fill=1)
        c.setFillColor(LIGHT); c.circle(x + w - 24, y - 24, 11, stroke=0, fill=1)
        icon(c, 'star', x + w - 24, y - 24, 7)
        c.saveState(); c.setFillColor(white)
        s.k.wrap(w - 70, 20); s.k.drawOn(c, x + 14, y - 17)
        size = s.st['band_t'].fontSize
        while pdfmetrics.stringWidth(s.t, 'Baloo', size) > w - 70 and size > 10: size -= 0.5
        c.setFont('Baloo', size); c.drawString(x + 14, y - 40, s.t)
        c.restoreState()


class Meta(B):
    def __init__(s, left, right, st):
        s.l = left; s.r = right; s.st = st
        s.p = Paragraph(f'<b>{fmt(tc(left))}</b>   |   <b>{tc("you will need")}:</b> {fmt(right)}', st['meta'])

    def h(s, w): return s.p.wrap(w - 20, 100)[1] + 14 + 8

    def draw(s, c, x, y, w):
        ph = s.p.wrap(w - 20, 100)[1]; hh = ph + 10
        c.setFillColor(TINT); c.setStrokeColor(LINE); c.setLineWidth(0.7); c.roundRect(x, y - hh, w, hh, 5, stroke=1, fill=1)
        s.p.drawOn(c, x + 10, y - 5 - ph)


class TableBlock(B):
    def __init__(s, rows, weights, st, first_bold=True, sa=8, big=False):
        s.rows = rows; s.w = weights; s.st = st; s.fb = first_bold; s.sa = sa; s._k = None; s.big = big

    def _t(s, w):
        if s._k == w: return s._t_
        data = []
        for i, r in enumerate(s.rows):
            if i == 0: data.append([Paragraph(fmt(tc(c)), s.st['th']) for c in r])
            else: data.append([Paragraph(fmt(c), s.st[('cell_b' if (j == 0 and s.fb) else 'cell') + ('_l' if s.big else '')]) for j, c in enumerate(r)])
        t = Table(data, colWidths=[w * x for x in s.w], repeatRows=1)
        ts = [('BACKGROUND', (0, 0), (-1, 0), GREEN), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
              ('GRID', (0, 0), (-1, -1), 0.6, LINE), ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
              ('TOPPADDING', (0, 0), (-1, -1), 7 if s.big else 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 7 if s.big else 4)]
        for i in range(1, len(s.rows)):
            if i % 2 == 0: ts.append(('BACKGROUND', (0, i), (-1, i), TINT))
        t.setStyle(TableStyle(ts)); t.wrap(w, 10000); s._t_ = t; s._k = w
        return t

    def h(s, w): return s._t(w)._height + s.sa

    def draw(s, c, x, y, w):
        t = s._t(w); t.drawOn(c, x, y - t._height)


class Lines(B):
    def __init__(s, n, st, label=None, unit=21, sa=6):
        s.n = n; s.units = n; s.unit = unit; s.sa = sa
        s.lab = Paragraph(fmt(label), st['label']) if label else None

    def h(s, w):
        return (s.lab.wrap(w, 1000)[1] + 2 if s.lab else 0) + s.n * (s.unit + s.extra) + s.sa

    def draw(s, c, x, y, w):
        if s.lab:
            lh = s.lab.wrap(w, 1000)[1]; s.lab.drawOn(c, x, y - lh); y -= lh + 2
        c.setStrokeColor(LINE_DARK); c.setLineWidth(0.6)
        for i in range(s.n):
            yy = y - (i + 1) * (s.unit + s.extra) + 3
            c.line(x, yy, x + w, yy)


class Fields(B):
    def __init__(s, labels, st, gap=15):
        s.ps = [Paragraph(fmt(l), st['label']) for l in labels]; s.units = len(labels); s.gap = gap

    def h(s, w): return sum(p.wrap(w, 1000)[1] + s.gap + s.extra for p in s.ps) + 4

    def draw(s, c, x, y, w):
        c.setStrokeColor(LINE_DARK); c.setLineWidth(0.6)
        for p in s.ps:
            ph = p.wrap(w, 1000)[1]; p.drawOn(c, x, y - ph)
            yy = y - ph - s.gap - s.extra + 3
            c.line(x, yy, x + w, yy); y -= ph + s.gap + s.extra


class Rating(B):
    def __init__(s, label, st, sa=8):
        s.p = Paragraph(fmt(label), st['label']); s.sa = sa

    def h(s, w): return s.p.wrap(w, 1000)[1] + 24 + s.sa

    def draw(s, c, x, y, w):
        ph = s.p.wrap(w, 1000)[1]; s.p.drawOn(c, x, y - ph)
        cy = y - ph - 13
        for i in range(5):
            cx = x + 10 + i * 30
            c.setStrokeColor(GREEN); c.setFillColor(white); c.setLineWidth(1.1); c.circle(cx, cy, 8.5, stroke=1, fill=1)
            c.setFillColor(MUTED); c.setFont('Cabin-Bold', 8.5); c.drawCentredString(cx, cy - 3, str(i + 1))


class Cards(B):
    def __init__(s, cards, st, cols=2, minh=96):
        s.cards = cards; s.st = st; s.cols = cols; s.minh = minh

    def _geo(s, w):
        cw = (w - 10 * (s.cols - 1)) / s.cols
        items = []
        for t, x in s.cards:
            pt = Paragraph(fmt(tc(t)), ParagraphStyle('ct', fontName='Baloo', fontSize=13, leading=15, textColor=GREEN))
            px = Paragraph(fmt(x), s.st['body'])
            items.append((pt, px, pt.wrap(cw - 20, 500)[1] + px.wrap(cw - 20, 500)[1] + 28))
        rows = [items[i:i + s.cols] for i in range(0, len(items), s.cols)]
        rh = [max(s.minh, max(i[2] for i in r)) for r in rows]
        return cw, rows, rh

    def h(s, w):
        cw, rows, rh = s._geo(w); return sum(rh) + 10 * (len(rows) - 1) + 8

    def draw(s, c, x, y, w):
        cw, rows, rh = s._geo(w)
        for r, hh in zip(rows, rh):
            for j, (pt, px, _) in enumerate(r):
                cx = x + j * (cw + 10)
                c.setFillColor(TINT); c.setStrokeColor(LIGHT); c.setLineWidth(1.2); c.setDash(4, 3)
                c.roundRect(cx, y - hh, cw, hh, 8, stroke=1, fill=1); c.setDash()
                a = pt.wrap(cw - 20, 500)[1]; pt.drawOn(c, cx + 10, y - 10 - a)
                b = px.wrap(cw - 20, 500)[1]; px.drawOn(c, cx + 10, y - 14 - a - b)
            y -= hh + 10


class LogTable(B):
    def __init__(s, headers, nrows, weights, st, prefill=None, hint=None, unit=26, sa=6):
        s.hd = headers; s.n = nrows; s.wts = weights; s.st = st; s.pre = prefill; s.hint = hint
        s.units = nrows; s.unit = unit; s.sa = sa
        s.hp = [Paragraph(fmt(tc(h)), st['th']) for h in headers]

    def _hh(s, w):
        return max(p.wrap(w * x - 8, 200)[1] for p, x in zip(s.hp, s.wts)) + 8

    def h(s, w): return s._hh(w) + s.n * (s.unit + s.extra) + s.sa

    def draw(s, c, x, y, w):
        hh = s._hh(w); xs = [x]
        for q in s.wts: xs.append(xs[-1] + q * w)
        c.setFillColor(GREEN); c.roundRect(x, y - hh, w, hh, 5, stroke=0, fill=1)
        c.rect(x, y - hh, w, hh / 2, stroke=0, fill=1)
        for p, x0, q in zip(s.hp, xs, s.wts):
            p.wrap(w * q - 8, 200); p.drawOn(c, x0 + 4, y - hh + 4)
        rh = s.unit + s.extra; yy = y - hh
        c.setStrokeColor(LINE); c.setLineWidth(0.7)
        for i in range(s.n):
            if i % 2 == 1:
                c.setFillColor(TINT); c.rect(x, yy - rh, w, rh, stroke=0, fill=1)
            c.line(x, yy - rh, x + w, yy - rh)
            if s.pre:
                c.setFillColor(INK); c.setFont('Cabin-Bold', 9); c.drawString(xs[0] + 5, yy - rh / 2 - 3, s.pre.format(i + 1))
            if s.hint:
                c.setFillColor(mix(MUTED, white, 0.35)); c.setFont('Cabin', 8.5)
                c.drawString(xs[1] + 5, yy - rh / 2 - 3, s.hint)
            yy -= rh
        c.line(x, y - hh, x, yy); c.line(x + w, y - hh, x + w, yy)
        for x0 in xs[1:-1]: c.line(x0, y - hh, x0, yy)


class DayBox(B):
    def __init__(s, n, st): s.n = n; s.st = st
    def h(s, w): return 96

    def draw(s, c, x, y, w):
        hh = 90
        c.setFillColor(TINT); c.setStrokeColor(LIGHT); c.setLineWidth(1); c.roundRect(x, y - hh, w, hh, 7, stroke=1, fill=1)
        c.setFillColor(GREEN); c.roundRect(x, y - 22, 54, 22, 7, stroke=0, fill=1)
        c.setFillColor(white); c.setFont('Baloo', 12); c.drawString(x + 9, y - 16, f'Day {s.n}')
        c.setFillColor(INK); c.setFont('Cabin-Bold', 9); c.drawString(x + 64, y - 15, 'Date:')
        c.setStrokeColor(LINE_DARK); c.setLineWidth(0.6); c.line(x + 90, y - 17, x + 170, y - 17)
        for k, lab in enumerate(('Mission Done', 'Guardian Pause')):
            bx = x + 190 + k * 100
            c.setStrokeColor(GREEN); c.setLineWidth(1.1); c.roundRect(bx, y - 18, 10, 10, 2, stroke=1, fill=0)
            c.setFillColor(INK); c.setFont('Cabin', 9); c.drawString(bx + 14, y - 16, lab)
        for k, lab in enumerate(("My Child's Mood", 'My Patience')):
            bx = x + 10 + k * (w / 2)
            c.setFillColor(INK); c.setFont('Cabin-Bold', 8.5); c.drawString(bx, y - 40, lab)
            for i in range(5):
                cx = bx + 6 + i * 22 + (88 if k == 0 else 62) * 0
                c.setStrokeColor(GREEN); c.setFillColor(white); c.setLineWidth(1); c.circle(bx + 80 * (1 if k == 0 else 0.8) + i * 20 - 70 + 70, y - 38, 7, stroke=1, fill=1)
                c.setFillColor(MUTED); c.setFont('Cabin-Bold', 7.5); c.drawCentredString(bx + 80 * (1 if k == 0 else 0.8) + i * 20, y - 40.5, str(i + 1))
        c.setFillColor(INK); c.setFont('Cabin-Bold', 9); c.drawString(x + 10, y - 66, 'Note:')
        c.setStrokeColor(LINE_DARK); c.setLineWidth(0.6)
        c.line(x + 40, y - 68, x + w - 10, y - 68); c.line(x + 10, y - 82, x + w - 10, y - 82)


# ----------------------------------------------------------------------------- parsing
def parse_file(path):
    mod = None; secs = []; cur = None; sub = None
    for line in open(path, encoding='utf8').read().split('\n'):
        if line.startswith('# ') and not line.startswith('## '):
            mod = [p.strip() for p in line[2:].split('|')]
        elif line.startswith('## '):
            parts = [p.strip() for p in line[3:].split('|')]
            cur = {'key': parts[0], 'parts': parts, 'lines': [], 'subs': {}, 'order': []}; secs.append(cur); sub = None
        elif line.startswith('### ') and cur is not None:
            sub = line[4:].strip(); cur['subs'][sub] = []; cur['order'].append(sub)
        elif cur is not None:
            (cur['subs'][sub] if sub else cur['lines']).append(line)
    return mod, secs


def tokens(lines):
    toks = []; i = 0; n = len(lines)
    SPECIAL = ('TABLE', 'FIELDS', 'CARDS', 'PROMPT:', 'PULLQUOTE:', 'RATING:', 'CHECKLIST:', 'LOG:', 'TALLY:', 'DAYS:', 'LINES:')
    while i < n:
        ln = lines[i].rstrip()
        if not ln.strip(): i += 1; continue
        if ln == 'TABLE':
            i += 1; rows = []
            while lines[i].strip() != 'ENDTABLE':
                rows.append([c.strip() for c in lines[i].split(' | ')]); i += 1
            toks.append(('table', rows)); i += 1
        elif ln == 'FIELDS':
            i += 1; ls = []
            while lines[i].strip() != 'ENDFIELDS': ls.append(lines[i].strip()); i += 1
            toks.append(('fields', ls)); i += 1
        elif ln == 'CARDS':
            i += 1; cs = []
            while lines[i].strip() != 'ENDCARDS':
                a, b = lines[i].split(' | ', 1); cs.append((a.strip(), b.strip())); i += 1
            toks.append(('cards', cs)); i += 1
        elif ln.startswith('PROMPT:'):
            txt = ln[7:].strip(); nl = 0
            if i + 1 < n and lines[i + 1].startswith('LINES:'):
                nl = int(lines[i + 1].split(':')[1]); i += 1
            toks.append(('prompt', txt, nl)); i += 1
        elif ln.startswith('PULLQUOTE:'): toks.append(('pull', ln[10:].strip())); i += 1
        elif ln.startswith('RATING:'): toks.append(('rating', ln[7:].strip())); i += 1
        elif ln.startswith('CHECKLIST:'):
            title = ln[10:].strip(); i += 1; items = []
            while i < n and lines[i].startswith('- '): items.append(lines[i][2:].strip()); i += 1
            toks.append(('check', title, items))
        elif ln.startswith('LOG:') or ln.startswith('TALLY:'):
            kind = 'log' if ln.startswith('LOG:') else 'tally'
            heads = [h.strip() for h in ln.split(':', 1)[1].split('|')]; i += 1
            nr = int(lines[i].split(':')[1]); i += 1
            toks.append((kind, heads, nr))
        elif ln.startswith('DAYS:'):
            a, b = ln[5:].strip().split('-'); toks.append(('days', int(a), int(b))); i += 1
        elif ln.startswith('LINES:'): toks.append(('lines', int(ln.split(':')[1]))); i += 1
        elif ln.startswith('- '):
            items = []
            while i < n and lines[i].startswith('- '): items.append(lines[i][2:].strip()); i += 1
            toks.append(('ul', items))
        elif re.match(r'^\d+\. ', ln):
            items = []
            while i < n and re.match(r'^\d+\. ', lines[i]): items.append(re.sub(r'^\d+\. ', '', lines[i]).strip()); i += 1
            toks.append(('ol', items))
        elif ln.startswith('> '):
            qs = []
            while i < n and lines[i].startswith('> '): qs.append(lines[i][2:].strip()); i += 1
            toks.append(('quote', qs))
        else:
            buf = [ln.strip()]; i += 1
            while i < n and lines[i].strip() and not lines[i].startswith(SPECIAL) and not lines[i].startswith(('- ', '> ')) \
                    and not re.match(r'^\d+\. ', lines[i]):
                buf.append(lines[i].strip()); i += 1
            toks.append(('p', ' '.join(buf)))
    return toks


def col_weights(n):
    return {2: [0.40, 0.60], 3: [0.28, 0.36, 0.36], 4: [0.2, 0.22, 0.28, 0.30]}.get(n, [1 / n] * n)


def to_blocks(toks, st, skip_title=False):
    out = []
    for t in toks:
        k = t[0]
        if k == 'p': out.append(Para(t[1], st['body'], sa=7))
        elif k == 'ol': out.append(Bullets(t[1], st['body'], 'number'))
        elif k == 'ul': out.append(Bullets(t[1], st['body'], 'bullet'))
        elif k == 'quote': out.append(QuoteBox(t[1], st['quote'])); out.append(Spacer(4))
        elif k == 'table': out.append(TableBlock(t[1], col_weights(len(t[1][0])), st, first_bold=True, big=(len(t[1][0]) == 2 and len(t[1]) > 6)))
        elif k == 'fields': out.append(Fields(t[1], st))
        elif k == 'pull': out.append(PullQuote(t[1], st['pull'])); out.append(Spacer(4))
        elif k == 'rating': out.append(Rating(t[1], st))
        elif k == 'prompt':
            out.append(Lines(t[2] or 3, st, label=t[1], sa=8))
        elif k == 'check':
            out.append(Para(f'<b>{fmt(t[1])}</b>', st['body'], sa=5, raw=True)); out.append(Bullets(t[2], st['body'], 'check'))
        elif k == 'cards': out.append(Cards(t[1], st))
        elif k == 'log':
            hd = t[1]; out.append(LogTable(hd, t[2], col_weights_log(len(hd)), st))
        elif k == 'tally':
            hd = t[1]; out.append(LogTable(hd, t[2], [0.14, 0.2, 0.33, 0.33], st, prefill='Week {}', hint='1   2   3   4   5'))
        elif k == 'days':
            for d in range(t[1], t[2] + 1):
                out.append(DayBox(d, st))
        elif k == 'lines': out.append(Lines(t[1], st, unit=24))
    return out


def col_weights_log(n):
    return {3: [0.2, 0.4, 0.4], 6: [0.09, 0.09, 0.22, 0.16, 0.19, 0.25]}.get(n, [1 / n] * n)


# ----------------------------------------------------------------------------- layout engine
def layout(blocks, avail, w):
    for b in blocks:
        b.extra = 0
        if hasattr(b, 'set_extra'): b.set_extra(0)
    H = sum(b.h(w) for b in blocks)
    if H > avail: return H, False
    units = sum(b.units for b in blocks)
    if units:
        e = min((avail - H) / units, 14)
        for b in blocks:
            if b.units:
                if hasattr(b, 'set_extra'): b.set_extra(e)
                else: b.extra = e
        H = sum(b.h(w) for b in blocks)
    return H, True


# ----------------------------------------------------------------------------- pages
class Page:
    def __init__(s, key, label, build, special=None, chrome=True):
        s.key = key; s.label = label; s.build = build; s.special = special; s.chrome = chrome


def build_pages():
    pages = []
    mod, front = parse_file(os.path.join(CONTENT, '00_front.md'))
    _, back = parse_file(os.path.join(CONTENT, '09_back.md'))

    def text_page(sec, head_title=None):
        title = head_title or sec['parts'][1]
        toks = tokens(sec['lines'])
        def build(st, s):
            blocks = [Para(fmt(tc(title)), st['h1'], sa=14, raw=True)]; HEADERS.append(('title', tc(title), 23))
            blocks += to_blocks(toks, st)
            return blocks
        return Page(sec['key'], tc(title), build)

    for sec in front:
        k = sec['key']
        if k == 'TITLE': pages.append(Page(k, '', None, special='title', chrome=False))
        elif k == 'CONTENTS': pages.append(Page(k, 'Contents', None, special='contents'))
        elif k == 'NOTICE': pages.append(text_page(sec))
        else: pages.append(text_page(sec))

    for mi in range(1, 9):
        path = glob.glob(os.path.join(CONTENT, f'{mi:02d}_*.md'))[0]
        mod, secs = parse_file(path)
        mnum = mod[0].split()[1]; mname = mod[1]; msub = mod[2]
        hdr = f'Module {mnum}: {mname}'
        sd = {s['key']: s for s in secs}
        missions = [s for s in secs if s['key'].startswith('MISSION')]

        # opener 1
        o1 = sd['OPENER-1']; t1 = tokens(o1['lines'])
        def b_o1(st, s, mnum=mnum, mname=mname, msub=msub, o1=o1, t1=t1):
            HEADERS.append(('module', tc(mname), 36)); HEADERS.append(('modsub', tc(msub), 13.5))
            bl = [Para(fmt(tc(f'Module {mnum}')).upper(), st['kick'], sa=0, raw=True),
                  Para(fmt(tc(mname)), st['mtitle'], sa=2, raw=True),
                  Para(fmt(tc(msub)), st['msub'], sa=12, raw=True),
                  Heading(o1['parts'][1], st['h2'], ic='star')]
            return bl + to_blocks(t1, st)
        pages.append(Page(f'M{mnum}-O1', hdr, b_o1))

        # opener 2
        o2 = sd['OPENER-2']; t2 = tokens(o2['lines'])
        def b_o2(st, s, o2=o2, t2=t2):
            bl = [Heading(o2['parts'][1], st['h2'], ic='star', sb=0)]
            box = []
            for t in t2:
                if t[0] == 'table': bl.append(TableBlock(t[1], col_weights(len(t[1][0])), st, first_bold=True, sa=14))
                elif t[0] == 'prompt':
                    txt = re.sub(r'^Patience Check-In\.\s*', '', t[1])
                    if t[1].startswith('Patience Check-In.'): box.append(Heading('Patience Check-In', st['h2'], ic='pause', sb=0, sa=3, rule=False))
                    box.append(Lines(t[2], st, label=txt, sa=4))
            bl.append(Box(box))
            return bl
        pages.append(Page(f'M{mnum}-O2', hdr, b_o2))

        # missions
        for ms in missions:
            num = ms['parts'][0].split()[1]; title = ms['parts'][1]; mtime = ms['parts'][2]; need = ms['parts'][3]
            sub = {k: tokens(v) for k, v in ms['subs'].items()}
            def b_left(st, s, num=num, title=title, mtime=mtime, need=need, sub=sub):
                bl = [Band(f'Mission {num}', title, st), Spacer(4), Meta(mtime, need, st)]
                bl.append(Heading('The Idea', st['h2'], ic='idea', sb=2)); bl += to_blocks(sub['The Idea'], st)
                bl.append(Heading('Steps', st['h2'], ic='steps')); bl += to_blocks(sub['Steps'], st)
                bl.append(Heading('Say This', st['h2'], ic='say')); bl += to_blocks(sub['Say This'], st)
                hp = Heading('Plan It', st['h2'], ic='star', sb=4); fp = Fields(['When Will We Try This?', 'What I Need To Get Ready:'], st, gap=14)
                hp.opt = fp.opt = True
                bl += [hp, fp]
                return bl
            pages.append(Page(f'M{mnum}-{num}L', hdr, b_left))

            def b_right(st, s, num=num, title=title, sub=sub):
                bl = [Band(f'Mission {num} Notes', title, st), Spacer(4)]
                bl.append(Heading('Notice', st['h2'], ic='notice', sb=2))
                items = sub['Notice'][0][1]
                bl.append(Bullets(items, st['body'], 'check'))
                gp = [Heading('Guardian Pause', st['h2'], ic='pause', sb=0, sa=3, rule=False),
                      Para(sub['Guardian Pause'][0][1], st['body'], sa=0)]
                bl.append(Box(gp, sa=6))
                bl.append(Heading("If It Isn't Working", st['h2'], ic='retry', sb=4))
                bl.append(Para(sub["If It Isn't Working"][0][1], st['body'], sa=6))
                bl.append(Heading('How It Went', st['h2'], ic='star', sb=2))
                bl.append(Fields(['Date And Time:', "How My Child Responded:", 'What Worked:', 'What I Would Change:'], st, gap=13))
                bl.append(Rating('How Did It Go? (1 = Tough, 5 = Great)', st, sa=2))
                bl.append(Rating('How Steady Was My Patience? (1 = Stretched, 5 = Steady)', st, sa=2))
                return bl
            pages.append(Page(f'M{mnum}-{num}R', hdr, b_right))

        # debrief
        db = sd['DEBRIEF']
        lb = tokens(db['subs']['Look Back']); la = tokens(db['subs']['Look Ahead'])
        def b_lb(st, s, mnum=mnum, lb=lb, missions=missions):
            bl = [Band(f'Module {mnum} Debrief', 'Look Back', st), Spacer(6)]
            bl += to_blocks(lb, st)
            rows = [['Done', 'Mission', 'How It Went']]
            for ms in missions: rows.append(['☐' if False else '', f"{ms['parts'][0].split()[1]}  {ms['parts'][1]}", ''])
            bl.append(Heading('Mission Check-Off', st['h2'], ic='steps', sb=2))
            bl.append(MissionChecks(rows, st))
            return bl
        pages.append(Page(f'M{mnum}-D1', hdr, b_lb))

        def b_la(st, s, mnum=mnum, la=la):
            bl = [Band(f'Module {mnum} Debrief', 'Look Ahead', st), Spacer(6)]
            bl += to_blocks(la, st)
            bl.append(Lines(2, st, label='A Sentence I Want To Say To My Child This Week:', sa=6))
            bl.append(Lines(2, st, label='A Strength I Will Watch For This Week:', sa=6))
            return bl
        pages.append(Page(f'M{mnum}-D2', hdr, b_la))

    for sec in back:
        k = sec['key']
        pages.append(text_page(sec))
    return pages


class MissionChecks(B):
    def __init__(s, rows, st):
        s.rows = rows; s.st = st; s.units = len(rows) - 1; s.unit = 28

    def h(s, w): return 22 + s.units * (s.unit + s.extra) + 6

    def draw(s, c, x, y, w):
        c.setFillColor(GREEN); c.roundRect(x, y - 22, w, 22, 5, stroke=0, fill=1); c.rect(x, y - 22, w, 11, stroke=0, fill=1)
        c.setFillColor(white); c.setFont('Cabin-Bold', 8.5)
        c.drawString(x + 8, y - 15, 'Done'); c.drawString(x + 52, y - 15, 'Mission'); c.drawString(x + w * 0.62, y - 15, 'How It Went')
        rh = s.unit + s.extra; yy = y - 22
        c.setStrokeColor(LINE); c.setLineWidth(0.7)
        for i, r in enumerate(s.rows[1:]):
            if i % 2 == 1: c.setFillColor(TINT); c.rect(x, yy - rh, w, rh, stroke=0, fill=1)
            c.line(x, yy - rh, x + w, yy - rh)
            c.setStrokeColor(GREEN); c.setLineWidth(1.1); c.roundRect(x + 10, yy - rh / 2 - 5, 10, 10, 2, stroke=1, fill=0)
            c.setStrokeColor(LINE); c.setLineWidth(0.7)
            c.setFillColor(INK); c.setFont('Cabin', 9.5); c.drawString(x + 52, yy - rh / 2 - 3.5, tc(r[1]))
            yy -= rh
        c.line(x, y - 22, x, yy); c.line(x + w, y - 22, x + w, yy)


# ----------------------------------------------------------------------------- special pages
def draw_emblem(c, cx, cy, sc=1.0):
    import math
    c.saveState(); c.translate(cx, cy); c.scale(sc, sc)
    c.setFillColor(LIGHT)
    p = c.beginPath(); p.moveTo(-70, 20); p.curveTo(-120, 30, -140, -10, -150, -30); p.curveTo(-110, -20, -90, -40, -45, -35); p.close()
    c.drawPath(p, stroke=0, fill=1)
    c.setFillColor(GREEN); c.setStrokeColor(GREEN); c.setLineWidth(5)
    p = c.beginPath(); p.moveTo(-55, 70); p.lineTo(55, 70); p.lineTo(55, 5); p.curveTo(55, -45, 20, -75, 0, -88); p.curveTo(-20, -75, -55, -45, -55, 5); p.close()
    c.drawPath(p, stroke=1, fill=1)
    c.setFillColor(white)
    p = c.beginPath()
    for i in range(10):
        ang = math.pi / 2 + i * math.pi / 5
        r = 36 if i % 2 == 0 else 15
        x, y = r * math.cos(ang), r * math.sin(ang) - 2
        (p.moveTo if i == 0 else p.lineTo)(x, y)
    p.close(); c.drawPath(p, stroke=0, fill=1)
    c.restoreState()


def draw_title(c):
    # nothing touches the page edge, so the paperback can be set up with no bleed
    c.setStrokeColor(LIGHT); c.setLineWidth(2)
    c.line(54, PH - 54, PW - 54, PH - 54); c.line(54, 54, PW - 54, 54)
    draw_emblem(c, PW / 2, 520, 1.15)
    c.setFillColor(GREEN); c.setFont('Baloo', 46); c.drawCentredString(PW / 2, 360, 'Raising a')
    c.drawCentredString(PW / 2, 312, 'Superhero')
    sub = Paragraph(fmt("A Parent's Activity Workbook for Turning ADHD Traits into Strengths and Growing Your Patience"),
                    ParagraphStyle('ts', fontName='Cabin', fontSize=14, leading=19, textColor=INK, alignment=1))
    sub.wrap(340, 200); sub.drawOn(c, (PW - 340) / 2, 232)
    c.setStrokeColor(LIGHT); c.setLineWidth(1.2); c.line(PW / 2 - 40, 210, PW / 2 + 40, 210)
    c.setFillColor(INK); c.setFont('Cabin-Bold', 12); c.drawCentredString(PW / 2, 100, 'Cimple Books')
    c.setFont('Cabin', 10.5); c.setFillColor(MUTED); c.drawCentredString(PW / 2, 83, 'www.cimpledigital.com/books')


def toc_entries(pages):
    # (title, page number, level)
    ent = []
    for i, p in enumerate(pages, 1):
        k = p.key
        if k in ('WELCOME', 'HOWTO', 'QUICKSTART', 'FRAMEWORK', 'PROFILE', 'BASELINE'): ent.append((p.label, i, 0, None))
        elif k.endswith('-O1'): ent.append((p.label, i, 1, []))
        elif re.match(r'M\d-\d\.\dL', k): ent[-1][3].append((k.split('-')[1][:3], i))
        elif k in ('PT-1', 'PB-1', 'TRACK-1', 'WINS-1', 'NOTES-1', 'CLOSING', 'SUPPORT'):
            names = {'PT-1': 'Patience Toolkit', 'PB-1': 'Phrase Bank', 'TRACK-1': '30-Day Mission Tracker',
                     'WINS-1': 'Strengths Bank And Wins Log', 'NOTES-1': 'Notes', 'CLOSING': 'Keep Going, Hero Guardian',
                     'SUPPORT': 'Support And Next Steps'}
            ent.append((names[k], i, 0, None))
    return ent


def draw_contents(c, pages, x0, st):
    ent = toc_entries(pages)
    y = TOP
    c.setFillColor(GREEN); c.setFont('Baloo', 23); c.drawString(x0, y - 20, 'Contents'); y -= 40
    # mission titles
    mtitles = {}
    for p in pages:
        pass
    modtitles = {}
    for mi in range(1, 9):
        path = glob.glob(os.path.join(CONTENT, f'{mi:02d}_*.md'))[0]
        mod, secs = parse_file(path)
        modtitles[mi] = (mod[1], [(s['parts'][0].split()[1], s['parts'][1]) for s in secs if s['key'].startswith('MISSION')])
    mi = 0
    for title, pg, lvl, ms in ent:
        if lvl == 1:
            mi += 1; name, mlist = modtitles[mi]
            c.setFillColor(GREEN); c.setFont('Baloo', 12.5); c.drawString(x0, y - 12, f'Module {mi}: {tc(name)}')
            c.setFillColor(INK); c.setFont('Cabin-Bold', 10.5); c.drawRightString(x0 + CW, y - 12, str(pg)); y -= 16
            pgmap = dict(ms)
            line = '  ·  '.join((f'{n} {tc(t)} ({pgmap[n]})').replace(' ', '\u00a0') for n, t in mlist)
            para = Paragraph(fmt(line), ParagraphStyle('toc', fontName='Cabin', fontSize=8.2, leading=10.4, textColor=MUTED))
            h = para.wrap(CW - 14, 100)[1]; para.drawOn(c, x0 + 10, y - h); y -= h + 5
        else:
            c.setFillColor(INK); c.setFont('Cabin-Bold', 10.5)
            c.drawString(x0, y - 11, tc(title)); c.drawRightString(x0 + CW, y - 11, str(pg))
            tw = pdfmetrics.stringWidth(tc(title), 'Cabin-Bold', 10.5)
            c.setStrokeColor(LINE_DARK); c.setDash(1, 3); c.setLineWidth(0.8)
            c.line(x0 + tw + 6, y - 12, x0 + CW - 20, y - 12); c.setDash(); y -= 16
    return y


# ----------------------------------------------------------------------------- render
def render(pages, path, cover=None):
    c = canvas.Canvas(path, pagesize=(PW, PH))
    c.setTitle('Raising a Superhero'); c.setAuthor('Cimple Books'); c.setSubject('A Parent\'s Activity Workbook')
    meta = []
    if cover:
        from PIL import Image
        im = Image.open(cover); iw, ih = im.size
        sc = max(PW / iw, PH / ih); dw, dh = iw * sc, ih * sc
        c.drawImage(cover, (PW - dw) / 2, (PH - dh) / 2, dw, dh)
        c.showPage()
    for i, p in enumerate(pages, 1):
        verso = (i % 2 == 0)
        x0 = 42 if verso else 54
        if p.special == 'title':
            draw_title(c)
        else:
            # chrome
            if p.chrome:
                c.setFillColor(GREEN); c.setFont('Cabin-Bold', 8.5)
                hdr = 'Raising A Superhero' if verso else tc(p.label); HEADERS.append(('running', hdr, 8.5))
                if verso: c.drawString(x0, PH - 36, hdr)
                else: c.drawRightString(x0 + CW, PH - 36, hdr)
                c.setStrokeColor(LINE); c.setLineWidth(0.8); c.line(x0, PH - 42, x0 + CW, PH - 42)
                fx = x0 + 6 if verso else x0 + CW - 6
                c.setFillColor(GREEN); c.circle(fx, 28, 9, stroke=0, fill=1)
                c.setFillColor(white); c.setFont('Cabin-Bold', 8.5); c.drawCentredString(fx, 25, str(i))
            if p.special == 'contents':
                draw_contents(c, pages, x0, None)
                meta.append({'page': i, 'key': p.key, 'scale': 1.0})
            else:
                used = None
                dropped = False
                for s in (1.0, 1.0, 0.97, 0.94, 0.91, 0.88, 0.85):
                    st = styles(s); blocks = p.build(st, s)
                    if dropped: blocks = [b for b in blocks if not getattr(b, 'opt', False)]
                    if s == 1.0 and not dropped:
                        H, ok = layout(blocks, TOP - BOTTOM, CW)
                        if ok: used = s; break
                        blocks = [b for b in blocks if not getattr(b, 'opt', False)]; dropped = True
                    H, ok = layout(blocks, TOP - BOTTOM, CW)
                    if ok: used = s; break
                if used is None:
                    raise SystemExit(f'OVERFLOW page {i} ({p.key}): needs {H:.0f}pt of {TOP - BOTTOM}')
                y = TOP
                for b in blocks:
                    b.draw(c, x0, y, CW); y -= b.h(CW)
                meta.append({'page': i, 'key': p.key, 'scale': used, 'fill': round((TOP - y) / (TOP - BOTTOM), 2)})
        c.showPage()
    c.save()
    return meta


def qa(meta):
    problems = []
    for kind, s, size in HEADERS:
        for w in re.split(r'[\s]+', s):
            m = re.search(r'[A-Za-z]', w)
            if m and not w[m.start()].isupper(): problems.append(f'not title-cased [{kind}]: {s!r} ({w})')
        font = 'Baloo' if kind in ('heading', 'title', 'band', 'module') else 'Cabin-Bold'
        wd = pdfmetrics.stringWidth(s, font, size)
        limit = CW - (70 if kind == 'band' else 0)
        if kind in ('running',) and wd > CW: problems.append(f'running header too wide: {s!r} {wd:.0f}pt')
        if kind == 'band' and wd > CW - 70:
            # band shrinks font down to 10pt; make sure it does fit at 10pt
            if pdfmetrics.stringWidth(s, 'Baloo', 10) > CW - 70: problems.append(f'band overrun: {s!r}')
        if kind in ('module',) and wd > CW: problems.append(f'module title too wide: {s!r} {wd:.0f}pt')
    return problems


if __name__ == '__main__':
    cover = None
    if '--cover' in sys.argv: cover = sys.argv[sys.argv.index('--cover') + 1]
    pages = build_pages()
    print('pages:', len(pages))
    assert len(pages) % 2 == 0, 'page count must be even'
    meta = render(pages, os.path.join(OUT, 'raising-a-superhero_print_interior.pdf'))
    if cover: render(pages, os.path.join(OUT, 'raising-a-superhero_digital.pdf'), cover=cover)
    json.dump(meta, open(os.path.join(OUT, 'page_map.json'), 'w'), indent=1)
    probs = qa(meta)
    print('header checks:', len(HEADERS), 'strings,', len(probs), 'problems')
    for q in probs: print('  ', q)
    wide = [(k, s) for k, s, z in HEADERS if k in ('title', 'heading') and pdfmetrics.stringWidth(s, 'Baloo', z) > CW]
    print('headings that wrap to 2 lines (allowed, never overrun):', [s for k, s in wide])
    small = [m for m in meta if m['scale'] < 1.0]
    print('shrunk pages:', [(m['page'], m['key'], m['scale']) for m in small])
    low = [m for m in meta if m.get('fill', 1) < 0.6]
    print('low fill pages:', [(m['page'], m['key'], m['fill']) for m in low])
