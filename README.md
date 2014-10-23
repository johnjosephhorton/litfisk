# Introduction 

## What is this thing? 

It's a very hacky python script that takes a PDF (usually an academic article) and 
creates a plain text document (specifically, markdown) with sections for each page of the PDF. 
Each section has a hi-res image of that page, the extracted text from that page (to facilitate searching) 
and space for entering notes about that page. 
The idea is to make it easy to take in-site plain text notes interwoven
with the content of an article. This makes it easy to share notes with co-authors and keep everything version-controlled. 

The script also creates a folder with all the plaintext snippets from the passed pdf (if they can be
extracted). If each PDF is your pdf library gets this treatment, it
would easy to grep over the plain text of the doc and extract what you need.  
And because each text file is named after the page it came from, finding the exact location in the text is straightforward. 

[Example here](litfisk.md) 

## Why do you make this? 

It scratches and itch---taking notes on PDFs is terrible and sharing
literature notes with co-authors is a pain. 

## How does it work? 

1. Take a passed PDF file like so on the command line (`split.py <test.pdf`)
1. Splits out each page 
1. Converts that page to an image file 
1. Tries to extract that text 
1. Stores the images and text files in `./images` and `./texts/` folders
1. Weaves it all back together in a markdown document `litfisk.md`
which you can use pandoc to turn into html, a word document, a pdf and
so on. 

## What does it depend on? 
1. `imagemagick` 
1. `pypdf` library for python
1. `pdftotext` 
1. `iconv` 

## How has this been tested? 

1. Nowhere but my own personal linux 12.00 LTS machine. 
