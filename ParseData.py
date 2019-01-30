from PdfMining import rename_pdf
from PdfMining import tokenizePdf
from Shingling import generateShingles
from StringHashing import generateHash
import os


def parsedata(pdfdir, txtdir, matrix, startcount, m, doTokenShingle=False):
    dirpath = './' + pdfdir + '/'
    rename_pdf(pdfdir, startcount)
    docsinfo = {}
    numFiles = len([f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))])  # minHash()
    if doTokenShingle is True:

        for i in range(startcount, startcount + numFiles):
            tokenizePdf("Doc" + str(i), txtdir, pdfdir, docsinfo)
            generateShingles("Doc" + str(i), txtdir)

        docsinfoFile = open("./StoredData/docsinfo.txt", "w+", encoding='utf-8')
        for i in docsinfo:
            docsinfoFile.write(i + ",")
            docsinfoFile.write(str(docsinfo[i][0]) + ",")
            docsinfoFile.write(str(docsinfo[i][1]) + "\n")
    for i in range(startcount, startcount + numFiles):
        generateHash("Doc" + str(i), txtdir, m, matrix, i)
    print(" ")
    return numFiles
