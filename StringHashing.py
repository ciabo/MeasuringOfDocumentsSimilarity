import math
import string

pdfname = "4Doc"  # number of document
txtshingles = "./txt/" + pdfname + "Shingle2.txt"

m = 100000
alphabet = {chr(i + 96): i for i in range(1, 27)}
alphabet.update({1: 0})


def hashShingle(line, m):
    encode = 0
    i = 2
    while len(line) > i:
        encode += alphabet[1 if line[i].lower() not in alphabet.keys() else line[i].lower()] * math.pow(31, i)
        i += 1
    return encode % m


hashes = [0] * m
with open(txtshingles, "r", encoding='utf-8') as f:
    for line in f:
        hashShingle(line, m)
