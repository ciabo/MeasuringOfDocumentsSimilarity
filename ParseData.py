from PdfMining import rename_pdf
from PdfMining import tokenizePdf
from Shingling import generateShingles
from StringHashing import generateHash
import os


def parsedata(pdfdir, txtdir, matrix, startcount, m, docsinfo, doTokenShingle=False):
    dirpath = './' + pdfdir + '/'
    rename_pdf(pdfdir, startcount)
    numFiles = len([f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))])  # minHash()
    if doTokenShingle is True:
        print("Shingles and Tokens generation started")
        for i in range(startcount, startcount + numFiles):
            tokenizePdf("Doc" + str(i), txtdir, pdfdir, docsinfo)
            generateShingles("Doc" + str(i), txtdir)
        print("Shingles and Tokens generated")

    print("Matrix of hashes generation started")
    for i in range(startcount, startcount + numFiles):
        generateHash("Doc" + str(i), txtdir, m, matrix, i)
    print("Matrix of hashes generation ended")
    print(" ")
    return numFiles
