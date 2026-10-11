import os, re, subprocess, uuid, zipfile, shutil, datetime
from xml.sax.saxutils import escape
import build
from lib import *
OUT = '/home/user/firstrepo/memory-workbook/'
W = '/tmp/epubwork'; shutil.rmtree(W, ignore_errors=True); os.makedirs(W)
# 1. cover-less ebook interior PDF
core = [p for p in build.all_pages(ebook=True) if p['tag'] == 'core']
bad, n = build.build(OUT + 'memory-workbook_ebook_interior_nocover.pdf', core, numbered=False)
assert not bad, bad[:3]
print('ebook interior pages', n)
# 2. page images + text
subprocess.run(['pdftoppm', '-r', '150', '-jpeg', '-jpegopt', 'quality=86', OUT + 'memory-workbook_ebook_interior_nocover.pdf', W + '/pg'], check=True)
imgs = sorted(f for f in os.listdir(W) if f.endswith('.jpg'))
assert len(imgs) == n
def title_of(p):
    for fl in p['flow']:
        if isinstance(fl, Paragraph) and fl.style.name == 'h1':
            return re.sub('<[^>]+>', '', fl.text).replace('&rsquo;', '’').replace('&amp;', '&')
    return p['section']
titles = [title_of(p) for p in core]
def page_text(i):
    t = subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), '-layout', OUT + 'memory-workbook_ebook_interior_nocover.pdf', '-'], capture_output=True, text=True).stdout
    t = re.sub(r'\s+', ' ', t).strip()
    return t[:1500]
from PIL import Image
w, h = Image.open(W + '/' + imgs[0]).size
print('page image size', w, h)
bookid = 'urn:uuid:' + str(uuid.uuid4())
now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
TITLE = 'The 5-Minute Memory Workbook: Tiny Daily Habits for a Sharper, More Reliable Mind After 40'
files = {}
files['mimetype'] = 'application/epub+zip'
files['META-INF/container.xml'] = '<?xml version="1.0" encoding="UTF-8"?>\n<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>'
files['OEBPS/style.css'] = 'html,body{margin:0;padding:0;background:#fff;} img{display:block;width:100%;height:100%;margin:0;padding:0;}'
manifest = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>', '<item id="css" href="style.css" media-type="text/css"/>']
spine = []; navitems = []
for i, (img, ttl) in enumerate(zip(imgs, titles), 1):
    pid = 'p%03d' % i
    alt = escape(page_text(i), {'"': '&quot;'})
    files[f'OEBPS/{pid}.xhtml'] = (f'<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en"><head><meta charset="utf-8"/>'
        f'<title>{escape(ttl)}</title><meta name="viewport" content="width={w}, height={h}"/><link rel="stylesheet" type="text/css" href="style.css"/></head>'
        f'<body><img src="img/{pid}.jpg" alt="{alt}" width="{w}" height="{h}"/></body></html>')
    manifest.append(f'<item id="{pid}" href="{pid}.xhtml" media-type="application/xhtml+xml"/>')
    manifest.append(f'<item id="i{pid}" href="img/{pid}.jpg" media-type="image/jpeg"/>')
    spine.append(f'<itemref idref="{pid}"/>')
    navitems.append(f'<li><a href="{pid}.xhtml">{escape(ttl)}</a></li>')
    files[f'OEBPS/img/{pid}.jpg'] = open(W + '/' + img, 'rb').read()
files['OEBPS/nav.xhtml'] = ('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en"><head><meta charset="utf-8"/><title>Contents</title></head><body>'
    '<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>' + ''.join(navitems) + '</ol></nav></body></html>')
files['OEBPS/content.opf'] = ('<?xml version="1.0" encoding="UTF-8"?>\n<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" prefix="rendition: http://www.idpf.org/vocab/rendition/#">'
    '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
    f'<dc:identifier id="bookid">{bookid}</dc:identifier><dc:title>{escape(TITLE)}</dc:title><dc:language>en</dc:language><dc:creator>Cimple Books</dc:creator><dc:publisher>Cimple Books</dc:publisher>'
    '<dc:description>A six-week programme of five-minute daily habits for everyday memory and focus, with self-checks, planners, daily logs and trackers. Not medical advice.</dc:description>'
    f'<meta property="dcterms:modified">{now}</meta>'
    '<meta property="rendition:layout">pre-paginated</meta><meta property="rendition:orientation">portrait</meta><meta property="rendition:spread">none</meta>'
    '</metadata><manifest>' + ''.join(manifest) + '</manifest><spine>' + ''.join(spine) + '</spine></package>')
path = OUT + 'memory-workbook_fixedlayout.epub'
with zipfile.ZipFile(path, 'w') as z:
    z.writestr(zipfile.ZipInfo('mimetype'), files['mimetype'], compress_type=zipfile.ZIP_STORED)
    for k, v in files.items():
        if k == 'mimetype': continue
        z.writestr(k, v, compress_type=zipfile.ZIP_DEFLATED)
print('epub', os.path.getsize(path) // 1024, 'KB', len(imgs), 'pages')
