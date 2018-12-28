import math
from bitarray import bitarray

pdfname = "4Doc"  # number of document
txtshingles = "./txt/" + pdfname + "Shingle2.txt"

m = 1000000009
alphabet = {chr(i + 96): i for i in range(1, 27)}
alphabet.update({1: 0})


def hashShingle(line, m):
    encode = 0
    i = 2
    while len(line) > i:
        encode += alphabet[1 if line[i].lower() not in alphabet.keys() else line[i].lower()] * math.pow(31, i)
        i += 1
    return encode % m


def generateHash(path, m):
    hashes = bitarray(m)
    hashes.setall(0)
    with open(path, "r", encoding='utf-8') as f:
        for line in f:
            hashes[int(hashShingle(line, m))] = 1


generateHash(txtshingles, m)
