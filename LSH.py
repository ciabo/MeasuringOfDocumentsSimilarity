import math


# --------FEATURE: se ci sono 7righe nei minhash e divido per 3 mi da 2 bande da 3 e schianta perchè la terza banda è da 1
def LSH(minHashes, numberOfBands, numberOfDocuments):
    print("LSH started")
    bandDim = len(minHashes) // numberOfBands  # For python 2 change // with /
    # newHashDim = int(math.pow(10,bandDim)) #10^bandDim
    newHashDim = numberOfDocuments * 1000  # there are only numberOfDocuments bands in the same hash table so we multiply this value to be sure of no collisions
    if newHashDim % 2 == 0:
        newHashDim += 1  # Here we try to avoid number that are power of 2 that can lead to problem in the hash table
    documentCandidates = []
    for i in range(0, numberOfBands):
        bandedMinHashes = []
        checkCandidates = []
        for l in range(0, newHashDim):
            newList = []
            checkCandidates.append(newList)
        for j in range(0, numberOfDocuments):
            bandedMinHash = []
            for k in range(0, bandDim):
                bandedMinHash.append(minHashes[k + (bandDim * i)][j])  # in bandedHash there is the minhash for the document j
            bandedMinHashes.append(bandedMinHash)  # bandedHashes is the list of all minhashes of all documnets
            # check if two or more newHashes are equals
            checkCandidates[listHash(bandedMinHash, newHashDim)].append(j)  # j is the current document index
        for z in range(0, len(checkCandidates)):
            if len(checkCandidates[z]) >= 2:
                documentCandidates.append(checkCandidates[z])
    print("LSH ended")
    return documentCandidates


def listHash(list, m):
    encode = ""
    for i in range(0, len(list)):
        intList = int(list[i])
        strList = str(intList)
        encode = encode + strList
    val = int(encode)
    newHash = val % m
    return newHash
