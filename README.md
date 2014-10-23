# Introduction 

## What is this thing? 

It's a very hacky python script that takes a PDF (usually an academic article) and 
creates a plain text document (specifically, markdown) with sections for each page of the PDF. 
Each section has a hi-res image of that page, the extracted text from that page (to facilitate searching) 
and space for entering notes about that page. 
The idea is to make it easy to take "in-situ" plain text notes interwoven
with the content of an article. This makes it easy to share notes with co-authors and keep everything version-controlled. 

The script also creates a folder with all the plaintext snippets from the passed pdf (if they can be
extracted). If each PDF is your pdf library gets this treatment, it
would easy to grep over the plain text of the doc and extract what you need.  
And because each text file is named after the page it came from, finding the exact location in the text is straightforward. 

[Example here](litfisk.md) 

## Why do you make this? 

It scratches and itch---taking notes on PDFs is terrible and sharing
literature notes with co-authors is a pain. I would *love* if someone
worked this and turned it into a more reasonable python pacakge. I
know there are lots of poor practices in here (e.g., my use of
`os.system` calls). 

## How does it work? 

1. Take a passed PDF file like so on the command line (`split.py <test.pdf`)
1. Splits out each page 
1. Converts that page to an image file 
1. Tries to extract that text 
1. Stores the images and text files in `./images` and `./texts/` folders
1. Weaves it all back together in a markdown document `litfisk.md`
which you can use pandoc to turn into html, a word document, a pdf and
so on. 

## Example usage: grep over the text from an article 

`grep 'cost' *_ascii.txt` 

    file_15_ascii.txt:with little effort required on our part. The cost was also far less than that of standard
    file_15_ascii.txt:lab experiments, at an average cost of less than $1 per subject. However, even this low
    file_15_ascii.txt:per-subject cost vastly understates the comparative efficiency of online experiments.
    file_15_ascii.txt:We entirely avoided both the costs associated with hiring full-time assistants and the
    file_15_ascii.txt:costs of maintaining a laboratory. We also avoided the high initial costs of setting up
    file_15_ascii.txt:Of course, low costs would be irrelevant if the results were not informative. And
    file_16_ascii.txt:or flat fees for fund transfers, both of which raise the costs of keeping multiple accounts.
    file_17_ascii.txt:cost of a more elaborate experimental design.
    file_18_ascii.txt:13 Physical laboratory experiments essentially create the same pattern of costs, implying incentives not to
    file_20_ascii.txt:are needed, which gives the online laboratory an advantage due to its low costs and
    file_24_ascii.txt:norms could raise the cost of bad behavior, with the effect of both fostering honesty
    file_24_ascii.txt:is that it would reduce costly duplication of programming effort and design. As a
    file_24_ascii.txt:set.20 The Internet makes such sharing a low-cost chore, since the data are invariably
    file_25_ascii.txt:as valid as other kinds of experiments, while greatly reducing cost, time and inconvenience. Our replications of well-known experiments relied on MTurk, as MTurk
    file_6_ascii.txt:scammers cannot amortize script-writing costs over a larger volume of work). With
    file_9_ascii.txt:kinds of experiments that would be very difficult and costly to conduct in offline

The names of the files correspond to the page number, which makes
finding the exact usage easy. 

## What does it depend on? 
1. `imagemagick` 
1. `pypdf` library for python
1. `pdftotext` 
1. `iconv` 

## How has this been tested? 

1. Nowhere but my own personal linux 12.00 LTS machine. 
