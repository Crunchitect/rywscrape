import sys, fitz
fname = sys.argv[1]
doc = fitz.open(fname)
for page in doc:
    pix = page.get_pixmap()
    pix.save("M2/page-%i.png" % page.number)
