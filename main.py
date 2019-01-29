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

def cleanResults(results,n):
    toBeRemoved = []
    for i in range(0, len(results)):
        ok1 = False
        ok2 = False
        for element in results[i]:
            if element < n:
                ok1 = True
            if element >= n:
                ok2 = True
        if ok1 == False or ok2 == False:
            toBeRemoved.append(i)
    toBeRemoved.reverse()
    for i in toBeRemoved:
        results.pop(i)
    return results


def main():
    numberOfPermutations = 100  # number of permutation in the minHashing phase
    numberOfBands = 20  # number of bands in LSH phase
    m = 1000003
    createMinHashDatabaseMatrix=False
    compareBlocksOfDocs=False
    searchOneDocumentSimilarDocs=True #if a minHash matrix has been already created
    doTokenShingle=False
    if(createMinHashDatabaseMatrix):
        matrix = SparseMatrix()
        if(compareBlocksOfDocs):
            numFiles = parsedata("data2017", "txtdata", matrix, 0, m, doTokenShingle)
            n=numFiles
            numFiles += parsedata("data2018", "txtdata", matrix, numFiles, m, doTokenShingle)
        else:
            numFiles = parsedata("Document", "txt", matrix, 0, m, doTokenShingle)
        minHashes = minHash(matrix, numFiles, m, numberOfPermutations)
        SaveMinHash(minHashes)
        results = LSH(minHashes, numberOfBands, numFiles)
        print(results)
        if (compareBlocksOfDocs):
            results = cleanResults(results,n)
        print(results)

    if(searchOneDocumentSimilarDocs):
        matrice = SparseMatrix()
        docsimilar("./Doc4", "./OneDocSimilar/", matrice, m, numberOfPermutations, numberOfBands,
                   "./minHashes/minHash.txt", "./minHashes/ab.txt")



if __name__ == '__main__':
    main()

