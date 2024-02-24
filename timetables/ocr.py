import easyocr, sys

reader = easyocr.Reader(['en'])
blob = reader.readtext(sys.argv[1], detail=0, allowlist='0123456789Scout')


print(blob)