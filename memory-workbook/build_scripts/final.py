import build, io
from lib import *
from pypdf import PdfReader, PdfWriter
from PIL import Image
OUT = '/home/user/firstrepo/memory-workbook/'
# 1. print interior (no cover)
pages = build.all_pages()
bad, n = build.build(OUT + 'memory-workbook_interior_print.pdf', pages)
assert not bad and n == 128, (bad[:3], n)
# 2. ebook edition: core pages only, TOC without page numbers, cover first
core = [p for p in build.all_pages(ebook=True) if p['tag'] == 'core']
bad2, n2 = build.build('/tmp/ebook_body.pdf', core, numbered=True, skip_first=True)
assert not bad2
# cover page (trim art to 8.5x11 ratio)
im = Image.open(OUT + 'cover_memory-workbook.png').convert('RGB')
w, h = im.size; tw = round(h * 8.5 / 11); x0 = (w - tw) // 2
im = im.crop((x0, 0, x0 + tw, h)); im.save('/tmp/cover_trim.png')
from reportlab.pdfgen import canvas
c = canvas.Canvas('/tmp/cover_page.pdf', pagesize=letter, initialFontName='Body', initialFontSize=12); c.drawImage('/tmp/cover_trim.png', 0, 0, PW, PH); c.save()
wr = PdfWriter()
for src in ('/tmp/cover_page.pdf', '/tmp/ebook_body.pdf'):
    for pg in PdfReader(src).pages: wr.add_page(pg)
wr.add_metadata({'/Title': 'The 5-Minute Memory Workbook', '/Author': 'Cimple Books'})
wr.write(OUT + 'memory-workbook_ebook.pdf')
print('print pages', n, '| ebook pages', len(wr.pages))
