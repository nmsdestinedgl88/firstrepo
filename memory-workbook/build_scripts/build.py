import sys
from lib import *
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame
import content_front, content_weeks, content_back

def all_pages(ebook=False):
    pg = content_front.front_pages(ebook)
    for n in range(1, 7): pg += content_weeks.week_pages(n)
    pg += content_back.back_pages(ebook)
    return pg

def build(path, pages, numbered=True):
    Mark.log = {}
    FT, FB = 0.8*inch, 0.75*inch
    def deco(canv, doc):
        canv.saveState()
        idx = doc.page - 1
        sec = doc._secs[idx] if idx < len(doc._secs) else ''
        canv.setStrokeColor(RULE); canv.setLineWidth(0.7)
        canv.line(M, PH - 0.55*inch, PW - M, PH - 0.55*inch)
        canv.setFont('Body-B', 10.5); canv.setFillColor(GREEN)
        canv.drawString(M, PH - 0.5*inch, 'The 5-Minute Memory Workbook')
        canv.setFont('Body', 10.5); canv.setFillColor(GREY)
        canv.drawRightString(PW - M, PH - 0.5*inch, sec)
        canv.line(M, 0.55*inch, PW - M, 0.55*inch)
        canv.setFont('Body', 10); canv.drawString(M, 0.37*inch, 'Cimple Books')
        canv.drawRightString(PW - M, 0.37*inch, 'www.cimpledigital.com/books')
        if numbered:
            canv.setFont('Body-B', 11); canv.setFillColor(INK); canv.drawCentredString(PW/2, 0.37*inch, str(doc.page))
        canv.restoreState()
    doc = BaseDocTemplate(path, pagesize=letter, leftMargin=M, rightMargin=M, topMargin=FT, bottomMargin=FB,
                          initialFontName='Body', initialFontSize=12, title='The 5-Minute Memory Workbook', author='Cimple Books', subject='Tiny Daily Habits for a Sharper, More Reliable Mind After 40')
    doc._secs = [p['section'] for p in pages]
    fr = Frame(M, FB, CW, PH - FT - FB, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='f')
    doc.addPageTemplates([PageTemplate(id='p', frames=[fr], onPage=deco)])
    story = []
    for i, p in enumerate(pages):
        fl = list(p['flow'])
        if p.get('fill', True) and not (fl and isinstance(fl[-1], FillLines)):
            fl.append(sp(8)); fl.append(FillLines(p.get('label', 'My Notes'), 24))
        story.append(Mark(i)); story += fl
        if i < len(pages) - 1: story.append(PageBreak())
    doc.build(story)
    bad = [(i, Mark.log.get(i)) for i in range(len(pages)) if Mark.log.get(i) != i + 1]
    return bad, doc.page

if __name__ == '__main__':
    out = sys.argv[1]
    pages = all_pages()
    bad, n = build(out, pages)
    print('pages:', len(pages), 'built:', n, 'first mismatch:', bad[:5])
