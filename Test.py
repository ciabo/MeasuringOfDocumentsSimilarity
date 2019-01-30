import random
import math
from shutil import copyfile


def test(docdir, documentToChange, numFiles, similarity):
    for i in range(0, documentToChange - 1):
        editdoc = random.randint(0, numFiles - 1)
        docToEdit = []
        with open("./txt/Doc" + str(editdoc) + "token.txt", "r", encoding='utf-8') as f:
            for line in f:
                for word in line.split(" "):
                    docToEdit.append(word)
        # copyfile("./" + docdir + "/Doc" + str(editdoc) + "token.txt",
        #         "./Test/Doc" + str(editdoc) + "-" + str(similarity) + "token.txt")
        print(editdoc)

        # documents information retrieval
        docsinfo = {}
        with open("./StoredData/docsinfo.txt", "r", encoding='utf-8') as f:
            for line in f:
                row = []
                for word in line.split(','):
                    row.append(int(word.replace("\n", "")))
                docsinfo[row[0]] = [row[1], row[2]]

        numberOfToken = math.ceil(docsinfo[editdoc][0] / float(docsinfo[editdoc][1]))

        # test for each document's rows
        for j in range(docsinfo[editdoc][1]):
            prob = random.randint(0, 100)  # probability to swap rows with another pdf
            if prob >= similarity:
                swapdoc = random.randint(0, numFiles - 1)
                while swapdoc == editdoc:  # check if the document is the same
                    swapdoc = random.randint(0, numFiles - 1)
                rowToSwap = random.randint(0, docsinfo[swapdoc][1])
                docToSwap = []
                with open("./txt/Doc" + str(swapdoc) + "token.txt", "r", encoding='utf-8') as f:
                    for line in f:
                        for word in line.split(" "):
                            docToSwap.append(word)
                print(docToSwap)
