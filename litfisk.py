#!/usr/bin/env python
from __future__ import print_function 
import copy 
import sys
import os 

os.mkdir("images")
os.mkdir("texts") 

g = open("litfisk.md", "w")

print("# Notes on: ", file = g)

from pyPdf import PdfFileWriter, PdfFileReader
input = PdfFileReader(sys.stdin)
output = PdfFileWriter()
j = 0 
for p in [input.getPage(i) for i in range(0,input.getNumPages())]:
    j = j + 1
    output = PdfFileWriter()
    output.addPage(p)
    print("### Page " + str(j), file = g)
    f = open("./images/file_" + str(j) + ".pdf", "w")
    output.write(f)
    f.close()
    cmd = "pdftotext " + "./images/file_" + str(j) + ".pdf ./texts/file_" + str(j) + ".txt"
    os.system(cmd)
    cmd = "iconv -c -f utf8 -t ascii ./texts/file_" + str(j) + ".txt" + " > ./texts/file_" + str(j) + "_ascii.txt"
    os.system(cmd)
    cmd = "convert -density 100 ./images/file_" + str(j) + ".pdf -quality 100 ./images/file_" + str(j) + "_cropped.png"
    os.system(cmd)
    print("![](./images/file_" + str(j) + "_cropped.png)", file = g)
    print("", file = g)
    print("### Text", file = g)
    t = open("./texts/file_" + str(j) + "_ascii.txt", "r")
    txt = t.read() 
    txt = txt.replace('\n', ' ').replace('\r', '').replace('', '')
    n = 80 
    chunks = [txt[i:i+n] for i in range(0, len(txt), n)]
    for c in chunks:
        print("    " + c, file = g)
    print("", file = g)
    print("### Notes on page " + str(j), file = g)


g.close() 

