def generateShingles(pdfname):
    txtname = "./txt/" + pdfname + "token.txt"
    txtshingles = "./txt/" + pdfname + "Shingle.txt"
    shinglesFile = open(txtshingles, "w+", encoding='utf-8')

    k = 10
    i = 0
    shingles = []

    with open(txtname, "r", encoding='utf-8') as f:
        for line in f:
            while len(line) > k:
                shinglesFile.write(line[i:k + 1] + "\n")
                i += 1
                k += 1
    print("Shingles generated")
