from PdfMining import tokenizePdf
from Shingling import generateShingles
from StringHashing import generateHash
from MinHashing import minHash
from LSH import LSH


def docsimilar(docName, docdir, matrix, m, numberOfPermutations, numberOfBands, minHashesFile,
               abfile):
    minHashes = []
    with open(minHashesFile, "r", encoding='utf-8') as f:
        for line in f:
            l = []
            for el in line.split(","):
                if el != "\n":
                    l.append(int(el))
            minHashes.append(l)
    docnumber=len(minHashes[0])
    ablist = []
    with open(abfile, "r", encoding='utf-8') as f:
        for line in f:
            ab = []
            for el in line.split(","):
                if el != "\n" and el != ",":
                    ab.append(int(el))
            ablist.append(ab)
    tokenizePdf(docName, docdir, docdir, True)
    generateShingles(docName, docdir)
    print("Mining ended")
    print("Shingles generated")

    generateHash(docName, docdir, m, matrix, docnumber)
    print("Matrix of hashes generated")
    minHashesCol = minHash(matrix, 1, m, ablist, numberOfPermutations, True)

    for i in range(0, len(minHashes)):
        minHashes[i].append(int(minHashesCol[i]))
    results = LSH(minHashes, numberOfBands, docnumber + 1)
    toBeRemoved = []
    for i in range(0, len(results)):
        ok = False
        for element in results[i]:
            if element == docnumber:
                ok = True
        if ok is False:
            toBeRemoved.append(i)
    toBeRemoved.reverse()
    for i in toBeRemoved:
        results.pop(i)
    
    print(results)
