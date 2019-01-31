from LSH import LSH
from MinHashing import minHash
from SparseMatrix import SparseMatrix
from Save import SaveMinHash
from OneDocSimilar import docsimilar
from ParseData import parsedata
from Test import executeTests


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


def storeinformation(docsinfo):
    docsinfoFile = open("./StoredData/docsinfo.txt", "w+", encoding='utf-8')
    for i in docsinfo:
        docsinfoFile.write(str(i) + ",")
        docsinfoFile.write(str(docsinfo[i][0]) + ",")
        docsinfoFile.write(str(docsinfo[i][1]) + "\n")
    print("Docs' information stored")


def main():
    numberOfPermutations = 100  # number of permutation in the minHashing phase
    numberOfBands = 20  # number of bands in LSH phase
    m = 1000003
    createMinHashDatabaseMatrix = False
    compareBlocksOfDocs = False
    searchOneDocumentSimilarDocs = False  # if a minHash matrix has been already created
    doTokenShingle = False
    extest = True
    if createMinHashDatabaseMatrix:
        matrix = SparseMatrix()
        docsinfo = {}
        if compareBlocksOfDocs:
            numFiles = parsedata("data2017", "txtdata", matrix, 0, m, docsinfo, doTokenShingle)
            n = numFiles
            numFiles += parsedata("data2018", "txtdata", matrix, numFiles, m, docsinfo, doTokenShingle)
            storeinformation(docsinfo)  # always after parsedata
        else:
            numFiles = parsedata("Document", "txt", matrix, 0, m, docsinfo, doTokenShingle)
            storeinformation(docsinfo)  # always after parsedata
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
                   "./StoredData/minHash.txt", "./StoredData/ab.txt")
    if extest:
        executeTests(numberOfPermutations, numberOfBands, m)


if __name__ == '__main__':
    main()
