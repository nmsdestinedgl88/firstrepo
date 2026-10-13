from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Paragraph, Spacer, Table, TableStyle, Flowable, PageBreak,
                                KeepTogether)

FD = '/usr/share/fonts/truetype/crosextra/'
pdfmetrics.registerFont(TTFont('Body', FD + 'Carlito-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Body-B', FD + 'Carlito-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Body-I', FD + 'Carlito-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Body-BI', FD + 'Carlito-BoldItalic.ttf'))
pdfmetrics.registerFontFamily('Body', normal='Body', bold='Body-B', italic='Body-I', boldItalic='Body-BI')

ParagraphStyle.defaults['fontName'] = 'Body'
ParagraphStyle.defaults['bulletFontName'] = 'Body'
GREEN = colors.HexColor('#30A666')
LGREEN = colors.HexColor('#56CB87')
TINT = colors.HexColor('#F3F9F5')
INK = colors.HexColor('#1F2D2B')
GREY = colors.HexColor('#5E6E69')
RULE = colors.HexColor('#B9CFC5')
WHITE = colors.white

PW, PH = letter
M = 0.8 * inch
CW = PW - 2 * M

S = {
 'body': ParagraphStyle('body', fontName='Body', fontSize=13, leading=18.2, textColor=INK, spaceAfter=7),
 'small': ParagraphStyle('small', fontName='Body', fontSize=11, leading=14.5, textColor=GREY, spaceAfter=4),
 'lab': ParagraphStyle('lab', fontName='Body-B', fontSize=12, leading=15, textColor=INK),
 'kicker': ParagraphStyle('kicker', fontName='Body-B', fontSize=12.5, leading=15, textColor=GREEN, spaceAfter=2),
 'h1': ParagraphStyle('h1', fontName='Body-B', fontSize=29, leading=33, textColor=INK, spaceAfter=8),
 'h2': ParagraphStyle('h2', fontName='Body-B', fontSize=16.5, leading=20, textColor=GREEN, spaceBefore=6, spaceAfter=4),
 'center': ParagraphStyle('center', fontName='Body', fontSize=13, leading=18, textColor=INK, alignment=TA_CENTER, spaceAfter=6),
 'bul': ParagraphStyle('bul', fontName='Body', fontSize=13, leading=17.5, textColor=INK, leftIndent=18, bulletIndent=2, spaceAfter=3.5),
 'cell': ParagraphStyle('cell', fontName='Body', fontSize=11.5, leading=14.5, textColor=INK),
 'cellb': ParagraphStyle('cellb', fontName='Body-B', fontSize=11.5, leading=14.5, textColor=INK),
 'callt': ParagraphStyle('callt', fontName='Body-B', fontSize=13.5, leading=16.5, textColor=GREEN, spaceAfter=3),
 'callb': ParagraphStyle('callb', fontName='Body', fontSize=12.5, leading=17, textColor=INK, spaceAfter=0),
}

def P(t, st='body'): return Paragraph(t, S[st])
def sp(h=6): return Spacer(1, h)

def H(title, kicker=None):
    out = []
    if kicker: out.append(Paragraph(kicker, S['kicker']))
    out.append(Paragraph(title, S['h1']))
    out.append(Rule(CW, 2.2, GREEN, after=10))
    return out

def H2(t): return Paragraph(t, S['h2'])

class Rule(Flowable):
    def __init__(self, w, th=0.7, col=RULE, after=4):
        super().__init__(); self.w=w; self.th=th; self.col=col; self.after=after
    def wrap(self, aw, ah): return (self.w, self.th + self.after)
    def draw(self):
        self.canv.setStrokeColor(self.col); self.canv.setLineWidth(self.th)
        self.canv.line(0, self.after, self.w, self.after)

def B(items, st='bul'):
    return [Paragraph(i, S[st], bulletText='•') for i in items]

def Callout(title, text, w=None):
    w = w or CW
    cells = []
    if title: cells.append(Paragraph(title, S['callt']))
    if isinstance(text, str): text = [text]
    for t in text: cells.append(Paragraph(t, S['callb']))
    inner = Table([[c] for c in cells], colWidths=[w - 30])
    inner.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'Body'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
                               ('TOPPADDING',(0,0),(-1,-1),1.5),('BOTTOMPADDING',(0,0),(-1,-1),1.5)]))
    t = Table([[inner]], colWidths=[w])
    t.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'Body'),('BACKGROUND',(0,0),(-1,-1),TINT),('LINEBEFORE',(0,0),(0,-1),4,GREEN),
                           ('LEFTPADDING',(0,0),(-1,-1),16),('RIGHTPADDING',(0,0),(-1,-1),12),
                           ('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),10)]))
    return [t, sp(9)]

class Fld(Flowable):
    """Label (wrapped if long) with n ruled writing lines beneath it."""
    def __init__(self, label, lines=1, lh=22, w=None, hint=None):
        super().__init__(); self.label=label; self.lines=lines; self.lh=lh; self.w=w or CW; self.hint=hint
    def wrap(self, aw, ah):
        from reportlab.lib.utils import simpleSplit
        from reportlab.pdfbase.pdfmetrics import stringWidth
        self.ll = simpleSplit(self.label, 'Body-B', 12, self.w)
        self.hint_inline = False
        if self.hint:
            if stringWidth(self.ll[-1], 'Body-B', 12) + 6 + stringWidth(self.hint, 'Body-I', 10.5) <= self.w: self.hint_inline = True
            else: self.ll = self.ll + ['\x00' + self.hint]
        self.h = 5 + 15 * len(self.ll) + 2 + self.lines * self.lh
        return (self.w, self.h)
    def draw(self):
        c = self.canv; y = self.h - 12
        for i, t in enumerate(self.ll):
            if t.startswith('\x00'):
                c.setFont('Body-I', 10.5); c.setFillColor(GREY); c.drawString(0, y, t[1:])
            else:
                c.setFont('Body-B', 12); c.setFillColor(INK); c.drawString(0, y, t)
                if self.hint_inline and i == len(self.ll) - 1:
                    c.setFont('Body-I', 10.5); c.setFillColor(GREY); c.drawString(c.stringWidth(t, 'Body-B', 12) + 6, y, self.hint)
            y -= 15
        c.setStrokeColor(RULE); c.setLineWidth(0.8)
        top = self.h - 15 * len(self.ll) - 2
        for i in range(self.lines):
            yy = top - (i + 1) * self.lh + 6
            c.line(0, yy, self.w, yy)

class FillLines(Flowable):
    """Ruled lines filling all remaining height of the page frame."""
    def __init__(self, label=None, lh=24, hint=None, minh=48):
        super().__init__(); self.label=label; self.lh=lh; self.hint=hint; self.minh=minh
    def wrap(self, aw, ah):
        self.w = aw; self.h = max(ah - 2, 0)
        if self.h < self.minh: self.h = 0
        return (aw, self.h)
    def draw(self):
        if self.h <= 0: return
        c = self.canv; top = self.h
        if self.label:
            c.setFont('Body-B', 12); c.setFillColor(INK); c.drawString(0, top-12, self.label)
            if self.hint:
                lw = c.stringWidth(self.label, 'Body-B', 12)
                c.setFont('Body-I', 10.5); c.setFillColor(GREY); c.drawString(lw+6, top-12, self.hint)
            top -= 20
        c.setStrokeColor(RULE); c.setLineWidth(0.8)
        y = top - self.lh + 6
        while y > 4:
            c.line(0, y, self.w, y); y -= self.lh

class Check(Flowable):
    def __init__(self, text, w=None, st='cell'):
        super().__init__(); self.p = Paragraph(text, S[st]); self.w = w or CW
    def wrap(self, aw, ah):
        pw, ph = self.p.wrap(self.w - 26, ah); self.h = max(ph, 15) + 6; return (self.w, self.h)
    def draw(self):
        c = self.canv; c.setStrokeColor(GREEN); c.setLineWidth(1.3); c.setFillColor(WHITE)
        c.rect(0, self.h - 17, 13, 13, stroke=1, fill=1)
        self.p.drawOn(c, 26, self.h - 3 - self.p.height)

def Checks(items, st='cell'): return [Check(i, st=st) for i in items]

class Scale(Flowable):
    def __init__(self, label, n=5, low='Low', high='High', w=None):
        super().__init__(); self.label=label; self.n=n; self.low=low; self.high=high; self.w=w or CW
    def wrap(self, aw, ah): return (self.w, 27)
    def draw(self):
        from reportlab.pdfbase.pdfmetrics import stringWidth
        c = self.canv; c.setFont('Body-B', 12); c.setFillColor(INK); c.drawString(0, 12, self.label)
        hw = stringWidth(self.high, 'Body-I', 10); lw = stringWidth(self.low, 'Body-I', 10)
        x = self.w - hw - 6 - self.n * 30 - 2
        assert stringWidth(self.label, 'Body-B', 12) + 10 < x - 8 - lw, ('Scale label too long', self.label)
        c.setFont('Body-I', 10); c.setFillColor(GREY)
        c.drawRightString(x - 8, 12, self.low)
        for i in range(self.n):
            cx = x + i * 30 + 12
            c.setStrokeColor(GREEN); c.setLineWidth(1.2); c.setFillColor(WHITE); c.circle(cx, 14, 10.5, stroke=1, fill=1)
            c.setFillColor(GREY); c.setFont('Body', 10.5); c.drawCentredString(cx, 10.5, str(i + 1))
        c.setFont('Body-I', 10); c.setFillColor(GREY); c.drawRightString(self.w, 12, self.high)

def Grid(headers, nrows, widths, rowh=24, first=None, font=11.5, hdrh=None):
    """Fillable table. first: list of first-column labels (optional)."""
    data = [[Paragraph('<b>%s</b>' % h, ParagraphStyle('gh', fontName='Body-B', fontSize=font, leading=font+2.5, textColor=WHITE, alignment=TA_CENTER)) for h in headers]]
    for r in range(nrows):
        row = []
        for ci in range(len(headers)):
            if ci == 0 and first and r < len(first): row.append(Paragraph(first[r], S['cell']))
            else: row.append('')
        data.append(row)
    tot = sum(widths); widths = [w*CW/tot for w in widths]
    t = Table(data, colWidths=widths, rowHeights=[hdrh or (rowh*0.9)] + [rowh]*nrows, repeatRows=1)
    t.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'Body'),('BACKGROUND',(0,0),(-1,0),GREEN),('GRID',(0,0),(-1,-1),0.7,RULE),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE, TINT])]))
    return [t, sp(8)]

def Cards(rows, widths, valign='TOP', pad=7):
    """Content table (paragraph cells), tinted header col."""
    data = [[Paragraph(c, S['cellb'] if i == 0 else S['cell']) if isinstance(c, str) else c for i, c in enumerate(r)] for r in rows]
    tot = sum(widths); widths = [w*CW/tot for w in widths]
    t = Table(data, colWidths=widths)
    t.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'Body'),('GRID',(0,0),(-1,-1),0.7,RULE),('BACKGROUND',(0,0),(0,-1),TINT),
        ('VALIGN',(0,0),(-1,-1),valign),('LEFTPADDING',(0,0),(-1,-1),pad),('RIGHTPADDING',(0,0),(-1,-1),pad),
        ('TOPPADDING',(0,0),(-1,-1),pad-1),('BOTTOMPADDING',(0,0),(-1,-1),pad)]))
    return [t, sp(8)]

class Mark(Flowable):
    log = {}
    def __init__(self, idx, tag=''): super().__init__(); self.idx=idx
    def wrap(self, aw, ah): return (0, 0)
    def draw(self): Mark.log[self.idx] = self.canv.getPageNumber()

class BoxF(Flowable):
    def wrap(self, aw, ah): return (18, 18)
    def draw(self):
        c = self.canv; c.setStrokeColor(GREEN); c.setLineWidth(1.3); c.setFillColor(WHITE); c.rect(0, 2, 13, 13, stroke=1, fill=1)
