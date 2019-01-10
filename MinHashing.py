from random import randint
import numpy as np
from SparseMatrix import SparseMatrix
from Save import *

primeNumber = 10000013  # this must be greater than the number of shingles(dieci milioni e 13)


# matrix is a vector of dim equals to the number of shingles and
# every element is an array that contains the column index
# of an element with value 1 in the sparse matrix

def minHash(matrix, numberOfDocuments, shingleNumber, ab=None, permutationNumber=100, singleDocument=False):
    minHashes = []
    ablist = []
    keys = matrix.getKeys()
    for i in range(0, permutationNumber):
        print("permutation number " + str(i) + "...")
        minHash = np.full(numberOfDocuments, np.inf)  # vector with dimension equal to the number of documents
        if singleDocument is True:
            a = ab[i][0]
            b = ab[i][1]
        else:
            a = randint(0, 100)
            b = randint(0, 100)
            e = [a, b]
            ablist.append(e)
        for key in keys:
            # ones = matrix[j]  # signature
            ones = matrix.getColumns(key)
            hashedIndex = hash(key, primeNumber, shingleNumber, a, b)
            if singleDocument is False:
                for k in ones:
                    if hashedIndex < minHash[k]:
                        minHash[k] = hashedIndex  # minHash contain the value of the row corresponding to the one
            else:
                if hashedIndex < minHash[0]:
                    minHash[0] = hashedIndex
        minHashes.append(minHash[0] if singleDocument else minHash)  # minHashes contain all the minhash
    if singleDocument is False:
        Saveab(ablist)
    print("MinHashing ultimated")
    return minHashes


def hash(val, p, n, a, b):
    res = ((a * val + b) % p) % n
    return int(res)
