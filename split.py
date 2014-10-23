#!/usr/bin/env python
from __future__ import print_function 
import copy 
import sys
import os 


os.mkdir("images")
os.mkdir("texts") 


g = open("litfisk.md", "w")

print("### Notes on: ", file = g)



from pyPdf import PdfFileWriter, PdfFileReader
input = PdfFileReader(sys.stdin)
output = PdfFileWriter()
j = 0 
for p in [input.getPage(i) for i in range(0,input.getNumPages())]:
    j = j + 1
    q = copy.copy(p)
    (w, h) = p.mediaBox.upperRight
    #p.mediaBox.upperRight = (w, h/2)
    #q.mediaBox.upperLeft = (w, h/2)
    p.mediaBox.upperRight = (w, h/2)
    q.mediaBox.lowerRight = (w, h/2)
    output = PdfFileWriter()
    output.addPage(q)
    print("### Page " + str(j), file = g)
    f = open("./images/file_" + str(j) + ".pdf", "w")
    output.write(f)
    f.close()
    cmd = "pdftotext " + "./images/file_" + str(j) + ".pdf ./texts/file_" + str(j) + ".txt"
    os.system(cmd)
    cmd = "iconv -c -f utf8 -t ascii ./texts/file_" + str(j) + ".txt" + " > ./texts/file_" + str(j) + "_asii.txt"
    os.system(cmd)
    cmd = "convert ./images/file_" + str(j) + ".pdf ./images/file_" + str(j) + ".png"
    os.system(cmd)
    cmd = "convert ./images/file_" + str(j) + ".png -fuzz 1% -trim +repage ./images/file_" + str(j) + "_cropped.png"
    os.system(cmd)
    print("![Alt text](./images/file_" + str(j) + "_cropped.png)", file = g)
    #output.addPage(p)
    #output.addPage(q)
#output.write(sys.stdout)


g.close() 

# Specs 
# Extracts all the plain text from a PDF to make it grep able  
# Creates a version-controlled folder where people can make comments 

# - make a directory for the file; create subdirectories with ./images ./text 
# - Takes a PDF - splits each page in half - stores splits in ./images as pdf & png
# -    Enhancement: Ideally tightly bounds each images to eliminate whitepspace   
# - Extracts text from each split (pdftotext) - writes to ./text subdirectory  
# - Includes in a verbatim environment 
#       Enhancement: Line wraps & smaller sizes 
# - Adds a comment box 

# split.py <test.pdf >output.pdf
