import math
import string

pdfname = "4Doc"  # number of document
txtshingles = "./txt/" + pdfname + "Shingle2.txt"

m = 100000
alphabet = {chr(i + 96): i for i in range(1, 27)}
print(alphabet)
sss = "casa"
print(alphabet.get('a'))


def hashShingle(line, m):
    encode = 0
    i = 1
    while len(line) > i:
        encode += alphabet[line[i].lower()] * math.pow(31, i)
        i += 1
    return encode % m


hashes = [0] * m
with open(txtshingles, "r", encoding='utf-8') as f:
    for line in f:
        hashShingle(line, m)
