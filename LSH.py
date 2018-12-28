import numpy as np

def LSH(minHashes,numberOfBands,numberOfDocuments,newHashDim):
    bandDim=len(minHashes)//numberOfBands #For python 2 change // with /
    documentCandidates=[]
    for i in range(0,numberOfBands):
        bandedMinHashes=[]
        checkCandidates=[]
        for i in range(0,newHashDim):
            newList=[]
            checkCandidates.append(newList)
        for j in range(0,numberOfDocuments):
            bandedMinHash = []
            for k in range(0,bandDim):
                bandedMinHash.append(minHashes[k][j]) #in bandedHash there is the minhash for the document j
            bandedMinHashes.append(bandedMinHash) #bandedHashes is the list of all minhashes of all documnets
            #check if two or more newHashes are equals
            checkCandidates[listHash(bandedMinHash)].append(documentIdx)
        for i in range(0,len(checkCandidates)):
            if len(checkCandidates[i])>=2:
                documentCandidates.append(checkCandidates[i])
    return documentCandidates


def listHash(list):
    newHash=[]
    return newHash