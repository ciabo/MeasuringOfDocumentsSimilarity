from random import randint
import numpy as np

primeNumber = 10000013  # this must be greater than the number of shingles(dieci milioni e 13)


# matrix is a vector of dim equals to the number of shingles and
# every element is an array that contains the column index
# of an element with value 1 in the sparse matrix

def minHash(matrix, numberOfDocuments, shingleNumber, permutationNumber=100):
    minHashes = []
    for i in range(0, permutationNumber):
        hashedIndex = []  # hashedIndex is a vector that contains a permutation: hashedIndex[0]=3 means that the row 0 will be the row 3
        minHash = np.full(numberOfDocuments, np.inf)  # vector with dimension equal to the number of documents
        a = randint(0, 100)
        b = randint(0, 100)
        for j in range(0, shingleNumber):
            hashedIndex.append(hash(j, primeNumber, shingleNumber, a, b))
            ones = matrix[j]  # signature
            for k in ones:
                if hashedIndex[j] < minHash[k]:
                    minHash[k] = hashedIndex[j]  # minHash contain the value of the row corresponding to the one
        minHashes.append(minHash)  # minHashes contain all the minhash
    print("MinHashing ultimated")
    return minHashes


def hash(val, p, n, a, b):
    res = ((a * val + b) % p) % n
    return res
