from PdfMining import rename_pdf
from PdfMining import tokenizePdf
from LSH import LSH
from Shingling import generateShingles
from MinHashing import minHash
from StringHashing import generateHash
import os


def main():
    #pdfdir = "Document"  # pdf directory
    #rename_pdf(pdfdir)

    m = 1000000  # dieci milioni e 9
    matrix = [[] for i in range(0, m)]
    minHashes = [[] for i in range(0, 100)]

    txtdir = "txt"  # select txt directory
    path = './Document/'
    numFiles = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])  # minHash()

    for i in range(0, numFiles):
        tokenizePdf("Doc" + str(i), txtdir)
        generateShingles("Doc" + str(i), txtdir)
    print("Mining ended")
    print("Shingles generated")
    for i in range(0, numFiles):
        generateHash("Doc" + str(i), txtdir, m, matrix, i)
    print("Matrix of hashes generated")
    minHashes = minHash(matrix, numFiles, m,100)
    results=LSH(minHashes,5,numFiles)
    print(results)


if __name__ == '__main__':
    main()
