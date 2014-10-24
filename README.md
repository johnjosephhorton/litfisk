litfisk
=======
It's a python script that takes a PDF (usually an academic article)
and creates a plain text document (specifically, markdown) with sections for each page of the PDF. 
Each section has a hi-res image of that page, the extracted text from that page (to facilitate searching) 
and space for entering notes about that page. 
The idea is to make it easy to take "in-situ" plain text notes interwoven
with the content of an article. This makes it easy to share notes with co-authors and keep everything version-controlled. 

The script also creates a folder with all the plaintext snippets from the passed pdf (if they can be
extracted). If each PDF is your pdf library gets this treatment, it
would easy to grep over the plain text of the doc and extract what you need.  
And because each text file is named after the page it came from, finding the exact location in the text is straightforward. 

[Example here](litfisk.md) 

This is a Python program for creating the directory structure and some of the files needed for a new project. 
[Here](https://dl.dropboxusercontent.com/u/420874/permanent/testproject.pdf) is an example of the PDF created by `create_project.py`. 

What is does
-----------
1. Creates a high-res image from every page in the passed pdf and
crops it to remove whitespace 
1. Extracts the text from that page 
1. Creates a markdown document with the same name as your passed pdf,
but the markdown extension, `.md` with the images, text and space for
notes interwoven in the document.  

To install
----------

You need to have the following command line tools accessible: 
1. `imagemagick` 
1. `imagemagick` 
1. `pdftotext` 
1. `iconv` 

To set it up, download the package 
	
	git clone git@github.com:johnjosephhorton/litfisk.git
	cd litfisk
	sudo python setup.py install 

Once you save your changes, you can simply run: 

	litfisk test.pdf  

The script will create a new directory `test` with the subdirectories
`images` and `texts`. 


License
-------

See the `licence` file. 

Example usage: grep over the text from an article 
-------------------------------------------------

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

How has this been tested? 
-------------------------

1. Nowhere but my own personal linux 12.00 LTS machine. 
