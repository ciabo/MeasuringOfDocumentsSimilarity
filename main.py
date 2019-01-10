from PdfMining import rename_pdf
from PdfMining import tokenizePdf
from LSH import LSH
from Shingling import generateShingles
from MinHashing import minHash
from StringHashing import generateHash
from SparseMatrix import SparseMatrix
from Save import SaveMinHash
from OneDocSimilar import docsimilar
from ParseData import parsedata
import time
import os


def main():
    numberOfPermutations = 100  # number of permutation in the minHashing phase
    numberOfBands = 25  # number of bands in LSH phase
    m = 1000003

    t0 = time.time()
    matrix = SparseMatrix()
    numFiles = parsedata("data2017", "txtdata", matrix, 0, m)
    numFiles += parsedata("data2018", "txtdata", matrix, numFiles, m)
    print(numFiles)
    minHashes = minHash(matrix, numFiles, m, numberOfPermutations)
    SaveMinHash(minHashes)
    results = LSH(minHashes, numberOfBands, numFiles)
    print(results)
    print(time.time() - t0)
    print(" ")

    t1 = time.time()
    matrice = SparseMatrix()
    docsimilar("./Doc4", "./OneDocSimilar/", matrice, m, numFiles, numberOfPermutations, numberOfBands,
               "./minHashes/minHash.txt", "./minHashes/ab.txt")
    print(time.time() - t1)


if __name__ == '__main__':
    main()
