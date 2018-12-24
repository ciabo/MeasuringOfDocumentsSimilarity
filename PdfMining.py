from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from nltk.corpus import stopwords
from io import StringIO  # for python 3.x use: from io import StringIO
import os
import re


def pdf_to_text(pdfname):
    rsrcmgr = PDFResourceManager()  # used to handle interpreter and device
    output = StringIO()  # destination of interpreter processing
    codec = 'utf-8'
    laparams = LAParams()  # params layout
    device = TextConverter(rsrcmgr, output, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Extract text
    fp = open(pdfname, 'rb')
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()

    # Get text from StringIO
    text = output.getvalue()

    # Cleanup
    device.close()
    output.close()

    return text


pdfname = "4Doc"  # number of document
filename = "./Document/" + pdfname + ".pdf"
# create a txt to tokenize
txt = pdf_to_text(filename)
txtname = "./txt/" + pdfname + ".txt"
txtFile = open(txtname, "w")
txtFile.write(txt)
text = []
txtFile.close()

tokenName = "./txt/" + pdfname + "2.txt"  # txt that contains token
tokenFile = open(tokenName, "w+")

punctuations = ['(', ')', ';', ':', '[', ']', ',', '']
stop_words = [word.encode('utf-8') for word in stopwords.words('english')]  # transform utf-8 str to byte str
with open(txtname, "r") as f:
    for line in f:
        for word in re.split(r',|\.|;|:|\s|\(|\)|\[|\]|\"|<|>|-|=', line):
            if word not in punctuations and word not in stop_words:
                text.append(word)
                tokenFile.write(word + "\n")
    print (text)
tokenFile.close()
os.remove("./txt/" + pdfname + ".txt")  # erase the txt used to tokenize
