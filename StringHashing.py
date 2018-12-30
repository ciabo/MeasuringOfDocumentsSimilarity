import math
from SparseMatrix import SparseMatrix

def hashShingle(line, m, alphabet):
    encode = 0
    i = 2
    while len(line) > i:
        encode += alphabet[1 if line[i].lower() not in alphabet.keys() else line[i].lower()] * math.pow(31, i)
        i += 1
    return encode % m


def generateHash(pdfname, txtdir, m, matrix, docnumber):
    alphabet = {chr(i + 96): i for i in range(1, 27)}
    alphabet.update({1: 0})
    txtShingles = "./" + txtdir + "/" + pdfname + "Shingle.txt"
    with open(txtShingles, "r", encoding='utf-8') as f:
        for line in f:
            index = int(hashShingle(line, m, alphabet))
            matrix.addValueWithCheck(index,docnumber)


