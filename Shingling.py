pdfname = "4Doc"  # number of document
txtname = "./txt/" + pdfname + "2.txt"

txtshingles = "./txt/" + pdfname + "Shingle2.txt"
shinglesFile = open(txtshingles, "w+", encoding='utf-8')

k = 10
i = 0
shingles = []

with open(txtname, "r", encoding='utf-8') as f:
    for line in f:
        while len(line) > k:
            # shingles.append(line[i:k + 1])
            shinglesFile.write(line[i:k + 1] + "\n")
            i += 1
            k += 1
# print(shingles)
