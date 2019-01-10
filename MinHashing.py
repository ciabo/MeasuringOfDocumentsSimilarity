from random import randint
import numpy as np
from SparseMatrix import SparseMatrix
from Save import *
primeNumber = 10000013  # this must be greater than the number of shingles(dieci milioni e 13)


# matrix is a vector of dim equals to the number of shingles and
# every element is an array that contains the column index
# of an element with value 1 in the sparse matrix

def minHash(matrix, numberOfDocuments, shingleNumber ,ab=None , permutationNumber=100, singleDocument=False ):
    minHashes = []
    ablist=[]
    keys=matrix.getKeys()
    for i in range(0, permutationNumber):
        print("permutation number "+str(i)+"...")
        minHash = np.full(numberOfDocuments, np.inf)  # vector with dimension equal to the number of documents
        if(singleDocument==True):
            a=ab[permutationNumber][0]
            b=ab[permutationNumber][1]
        else:
            a = randint(0, 100)
            b = randint(0, 100)
            e=[a,b]
            ablist.append(e)
        for key in keys:
            #ones = matrix[j]  # signature
            ones=matrix.getColumns(key)
            hashedIndex=hash(key, primeNumber, shingleNumber, a, b)
            for k in ones:
                if hashedIndex < minHash[k]:
                    minHash[k] = hashedIndex  # minHash contain the value of the row corresponding to the one
        minHashes.append(minHash)  # minHashes contain all the minhash
    if(singleDocument==False):
        Saveab(ablist)
    print("MinHashing ultimated")
    return minHashes


def hash(val, p, n, a, b):
    res = ((a * val + b) % p) % n
    return int(res)
