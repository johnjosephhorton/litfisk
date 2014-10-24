#!/usr/bin/env python
from __future__ import print_function 
import argparse 
import copy 
import sys
import os 
from pyPdf import PdfFileWriter, PdfFileReader

__author__ = 'John Joseph Horton'
__copyright__ = 'Copyright (C) 2012 John Joseph Horton'
__license__ = 'GPL v3'
__maintainer__ = 'johnjosephhorton'
__email__ = 'john.joseph.horton@gmail.com'
__status__ = 'Development'
__version__ = '0.1'

def fisk_pdf(pdffile, directory):
    name = pdffile[:-4]
    g = open(os.path.join(directory, name, name + ".md"), "w")
    print("# Notes on: ", file = g)
    input = PdfFileReader(file(pdffile, "rb"))
    print("Number of pages %s" % input.getNumPages())
    j = 0 
    for p in [input.getPage(i) for i in range(0,input.getNumPages())]:
        j = j + 1
        output = PdfFileWriter()
        output.addPage(p)
        print("### Page " + str(j), file = g)
        imagefile = os.path.join(directory, name, "images", "file_" + str(j) + ".pdf")
        imagefilePNG = os.path.join(directory, name, "images", "file_" + str(j) + ".png")
        f = open(imagefile, "w")
        output.write(f)
        f.close()
        textfile = os.path.join(directory, name, "texts", "file_" + str(j) + ".txt")
        textfileASCII = os.path.join(directory, name, "texts", "file_" + str(j) + "_ascii.txt")
        cmd = "pdftotext " + imagefile + " " + textfile # extracts text from the pdffile
        os.system(cmd)
        cmd = "iconv -c -f utf8 -t ascii " + textfile + " > " + textfileASCII 
        # ./texts/file_" + str(j) + ".txt" + " > ./texts/file_" + str(j) + "_ascii.txt"
        os.system(cmd)
        cmd = "convert -density 100 " + imagefile + " -quality 100 " + imagefilePNG
        os.system(cmd)
        print("![](./images/file_" + str(j) + ".png)", file = g)
        print("", file = g)
        print("### Text from page " + str(j), file = g)
        t = open(os.path.join(directory, name, "texts", "file_" + str(j) + "_ascii.txt"), "r")
        txt = t.read() 
        txt = txt.replace('\n', ' ').replace('\r', '').replace('', '')
        n = 80 
        chunks = [txt[i:i+n] for i in range(0, len(txt), n)]
        for c in chunks:
             print("    " + c, file = g)
             print("", file = g)
        print("### Notes on page " + str(j), file = g)

    g.close() 

def create_file_structure(pdffile, directory):
    name = pdffile[:-4]
    os.mkdir(os.path.join(directory, name))
    os.mkdir(os.path.join(directory, name, "images"))
    os.mkdir(os.path.join(directory, name, "texts"))

def main(): 
    parser = argparse.ArgumentParser(description = "Create a 'fisked' version of a pdf")
    parser.add_argument("file", help = "path to file")
    args = parser.parse_args()
    pdffile = args.file 
    create_file_structure(pdffile, os.getcwd())
    fisk_pdf(pdffile, os.getcwd())

if __name__ == '__main__':
    main() 
