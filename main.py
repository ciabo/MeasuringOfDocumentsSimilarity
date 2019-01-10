from PdfMining import rename_pdf
from PdfMining import tokenizePdf
from LSH import LSH
from Shingling import generateShingles
from MinHashing import minHash
from StringHashing import generateHash
from SparseMatrix import SparseMatrix
from Save import SaveMinHash
from OneDocSimilar import docsimilar
import time
import os


def main():
    pdfdir = "Document"  # pdf directory
    rename_pdf(pdfdir)
    t0 = time.time()
    numberOfPermutations = 100  # number of permutation in the minHashing phase
    numberOfBands = 25  # number of bands in LSH phase
    m = 1000003
    matrix = SparseMatrix()
    txtdir = "txt"  # select txt directory
    path = './' + pdfdir + '/'
    numFiles = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])  # minHash()
    for i in range(0, numFiles):
        tokenizePdf("Doc" + str(i), txtdir, pdfdir)
        generateShingles("Doc" + str(i), txtdir)
    print("Mining ended")
    print("Shingles generated")
    for i in range(0, numFiles):
        generateHash("Doc" + str(i), txtdir, m, matrix, i)
    print("Matrix of hashes generated")
    minHashes = minHash(matrix, numFiles, m, numberOfPermutations)
    SaveMinHash(minHashes)
    results = LSH(minHashes, numberOfBands, numFiles)
    print(results)
    print(time.time()-t0)
    matr = SparseMatrix()
    print(" ")
    docsimilar("./prova.pdf", "./OneDocSimilar/", matr, m, numFiles, numberOfPermutations, numberOfBands,
               "./minHashes/minHash.txt", "./minHashes/ab.txt")


if __name__ == '__main__':
    main()


