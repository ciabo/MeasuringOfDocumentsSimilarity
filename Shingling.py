def generateShingles(pdfname, txtdir):
    print("Shingles generation started")
    txtname = "./" + txtdir + "/" + pdfname + "token.txt"
    txtshingles = "./" + txtdir + "/" + pdfname + "Shingle.txt"
    shinglesFile = open(txtshingles, "w+", encoding='utf-8')

    k = 10
    i = 0

    with open(txtname, "r", encoding='utf-8') as f:
        for line in f:
            while len(line) > k:
                shinglesFile.write(line[i:k + 1] + "\n")
                i += 1
                k += 1
    shinglesFile.close()
    print("Shingles  generated")
