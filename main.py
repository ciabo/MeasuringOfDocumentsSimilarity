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
from Test import test
import os


def cleanResults(results, n):
    toBeRemoved = []
    for i in range(0, len(results)):
        ok1 = False
        ok2 = False
        for element in results[i]:
            if element < n:
                ok1 = True
            if element >= n:
                ok2 = True
        if ok1 is False or ok2 is False:
            toBeRemoved.append(i)
    toBeRemoved.reverse()
    for i in toBeRemoved:
        results.pop(i)
    newList = []
    for i in range(0, len(results)):
        if len(results[i]) > 2:
            j = 0
            target = 0
            while results[i][j] < n and j < len(results[i]):
                k = len(results[i]) - 1
                while results[i][k] >= n:
                    newItem = [results[i][j], results[i][k]]
                    newList.append(newItem)
                    k = k - 1
                j = j + 1
    toBeRemoved = []
    for i in range(0, len(results)):
        if len(results[i]) > 2:
            toBeRemoved.append(i)
    toBeRemoved.reverse()
    for i in toBeRemoved:
        results.pop(i)
    return results + newList


def main():
    numberOfPermutations = 100  # number of permutation in the minHashing phase
    numberOfBands = 20  # number of bands in LSH phase
    m = 1000003
    createMinHashDatabaseMatrix = True
    compareBlocksOfDocs = False
    searchOneDocumentSimilarDocs = False  # if a minHash matrix has been already created
    doTokenShingle = True
    if createMinHashDatabaseMatrix:
        matrix = SparseMatrix()
        if compareBlocksOfDocs:
            numFiles = parsedata("data2017", "txtdata", matrix, 0, m, doTokenShingle)
            n = numFiles
            numFiles += parsedata("data2018", "txtdata", matrix, numFiles, m, doTokenShingle)
        else:
            numFiles = parsedata("Document", "txt", matrix, 0, m, doTokenShingle)
        minHashes = minHash(matrix, numFiles, m, None, numberOfPermutations)
        SaveMinHash(minHashes)
        results = LSH(minHashes, numberOfBands, numFiles)
        # print(results)
        if compareBlocksOfDocs:
            results = cleanResults(results, n)
        print(results)

    if searchOneDocumentSimilarDocs:
        matrice = SparseMatrix()
        docsimilar("./Doc4", "./OneDocSimilar/", matrice, m, numberOfPermutations, numberOfBands,
                   "./minHashes/minHash.txt", "./minHashes/ab.txt")

    test("txt", 2, 6, 75)


if __name__ == '__main__':
    main()
