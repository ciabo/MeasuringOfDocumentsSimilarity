from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from nltk.corpus import stopwords
from io import StringIO  # for python 3.x use: from io import StringIO
import os
import re


# if executed more than 1 time delete files!!
def rename_pdf(pdfdir, startcount):
    answer = input("Do you want rename " + pdfdir + " 's pdfs?(Do it just one time) [y][n] ")
    if answer == "y":
        i = startcount
        basepath = "./" + pdfdir + "/"
        for fname in os.listdir(basepath):
            os.rename(os.path.join(basepath, fname), os.path.join(basepath, "Doc" + str(i) + ".pdf"))
            i += 1
        print("pdf renaming complete")
    print(" ")


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


def tokenizePdf(pdfname, txtdir, pdfdir, docsinfo, singleDocument=False):
    rownumber = 0
    tokennumber = 0
    filename = pdfname + ".pdf" if singleDocument else "./" + pdfdir + "/" + pdfname + ".pdf"
    # create a txt to tokenize
    txt = pdf_to_text(filename)
    txtname = "./" + txtdir + "/" + pdfname + ".txt"
    txtFile = open(txtname, "w", encoding='utf-8')
    txtFile.write(txt)
    text = []
    txtFile.close()

    tokenName = "./" + txtdir + "/" + pdfname + "token.txt"  # txt that contains token
    tokenFile = open(tokenName, "w+", encoding='utf-8')

    punctuations = ['(', ')', ';', ':', '[', ']', ',', '', '@', '{', '}']
    # stop_words = [word.encode('utf-8') for word in stopwords.words('english')]
    stop_words = stopwords.words('english')
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    greekLetters = ['Α', 'α', 'Β', 'β', 'Γ', 'γ', 'Δ', 'δ', 'Ε', 'ε', 'Ζ', 'ζ', 'Η', 'η', 'Θ', 'θ', 'Ι', 'ι', 'Κ', 'κ',
                    'Λ',
                    'λ', 'Μ', 'μ'
        , 'Ν', 'ν', 'Ξ', 'ξ', 'Ο', 'ο', 'Π', 'π', 'Ρ', 'ρ', 'Σ', 'σ', 'ς', 'Τ', 'τ', 'Υ', 'υ', 'Φ', 'φ', 'Χ', 'χ', 'Ψ',
                    'ψ',
                    'Ω', 'ω', '⎠', '|', '∈', '⎜']
    mathSymbols = ['exp', '^', '+', '-']
    with open(txtname, "r", encoding='utf-8') as f:
        for line in f:
            rownumber += 1
            for word in re.split(r',|\.|;|:|\s|\(|\)|\[|\]|\"|<|>|=|@|\||\{|\}', line):
                if word not in punctuations and word not in stop_words:
                    notEndedWordFlag = False
                    numberFlag = False
                    mathFlag = False
                    if word.endswith('-'):
                        notEndedWordFlag = True
                    for character in word:
                        if character == '“' or character == '\u2018' or character == '\u2019' or character == 'ˆ':
                            word = word.replace('“', '')
                            word = word.replace('ˆ', '')
                            word = word.replace('\u2018', '')
                            word = word.replace('\u2019', '')
                        elif character == '”':
                            word = word.replace('”', '')
                        elif character == 'ﬂ':
                            word = word.replace('ﬂ', 'fl')
                        elif character == 'ﬁ':
                            word = word.replace('ﬁ', 'fi')
                        elif character == '-' or character == '\u2014':
                            word = word.replace('-', '')
                            word = word.replace('\u2014', '')
                        elif character in numbers:
                            numberFlag = True
                        elif character in greekLetters or character in mathSymbols:
                            mathFlag = True
                    if len(word) > 2 and numberFlag is False and mathFlag is False:
                        text.append(word)
                        if notEndedWordFlag:
                            tokenFile.write(word)
                        else:
                            tokenFile.write(word + " ")
                            tokennumber += 1
    docsinfo[pdfname[len(pdfname) - 1:]] = [tokennumber, rownumber]  # fill the dictionary with the documents' infos
    tokenFile.close()
    os.remove("./" + txtdir + "/" + pdfname + ".txt")  # erase the txt used to tokenize
