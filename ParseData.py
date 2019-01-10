from PdfMining import rename_pdf
from PdfMining import tokenizePdf
from Shingling import generateShingles
from StringHashing import generateHash
import os


def parsedata(pdfdir, txtdir, matrix, startcount, m, doTokenShingle=False):
    dirpath = './' + pdfdir + '/'
    txtpath = './' + txtdir + '/'
    rename_pdf(dirpath, startcount)
    numFiles = len([f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))])  # minHash()
    if doTokenShingle is True:
        for i in range(startcount, startcount + numFiles):
            tokenizePdf("Doc" + str(i), txtpath, dirpath)
            generateShingles("Doc" + str(i), txtpath)
        print("Mining " + pdfdir + " ended")
        print("Shingles " + pdfdir + " generated")
    for i in range(startcount, startcount + numFiles):
        generateHash("Doc" + str(i), txtpath, m, matrix, i)
    print("Matrix of hashes " + pdfdir + " generated")
    print(" ")
    return numFiles
