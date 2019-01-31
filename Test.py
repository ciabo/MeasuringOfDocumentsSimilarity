import random
from SparseMatrix import SparseMatrix
from OneDocSimilar import docsimilar


def executeTests(numberOfPermutations, numberOfBands, m):
    extest = True
    numFiles = 392
    similarities = [75, 50, 25]

    editdoc = random.randint(0, numFiles - 1)
    for similarity in similarities:
        print("Start " + str(similarity) + "% similarity of Doc" + str(editdoc))
        docName = test(editdoc, "txt", numFiles, similarity)
        matrice = SparseMatrix()
        docsimilar(docName, "./Test/", matrice, m, numberOfPermutations, numberOfBands,
                   "./StoredData/minHash.txt", "./StoredData/ab.txt", extest)
        print("End " + str(similarity) + "% similarity of Doc" + str(editdoc))
        print(" ")


def test(editdoc, docdir, numFiles, similarity):
    # documents information retrieval
    docsinfo = {}
    with open("./StoredData/docsinfo.txt", "r", encoding='utf-8') as f:
        for line in f:
            row = []
            for word in line.split(','):
                row.append(int(word.replace("\n", "")))
            docsinfo[row[0]] = [row[1], row[2]]

    docToEdit = []
    with open("./" + docdir + "/Doc" + str(editdoc) + "token.txt", "r", encoding='utf-8') as f:
        for line in f:
            for word in line.split(" "):
                docToEdit.append(word)
    docToEdit.pop()  # remove the space at the end

    numberOfToken = docsinfo[editdoc][0] / float(docsinfo[editdoc][1])  # token per row of the document

    # probably swap for each document's rows
    for j in range(0, docsinfo[editdoc][1]):
        prob = random.randint(0, 100)  # probability to swap rows with another pdf
        if prob >= similarity:
            swapdoc = random.randint(0, numFiles - 1)  # document random choosed
            while swapdoc == editdoc:  # check if the document is the same
                swapdoc = random.randint(0, numFiles - 1)
            rowToSwap = random.randint(0, docsinfo[swapdoc][1] - 1)  # row random choosed in random doc

            # retrieve list of tokens
            docToSwap = []
            with open("./" + docdir + "/Doc" + str(swapdoc) + "token.txt", "r", encoding='utf-8') as f:
                for line in f:
                    for word in line.split(" "):
                        docToSwap.append(word)
            docToSwap.pop()  # remove the space at the end

            # token swap
            numberOfTokenSW = docsinfo[swapdoc][0] / float(docsinfo[swapdoc][1])  # token per row of the random document
            for token, swtoken in zip(range(int(j * numberOfToken), int(j * numberOfToken + numberOfToken)),
                                      range(int(rowToSwap * numberOfTokenSW),
                                            int(rowToSwap * numberOfTokenSW + numberOfToken))):
                docToEdit[token] = docToSwap[swtoken]

    # save new token in another file
    with open("./Test/Doc" + str(editdoc) + "-" + str(similarity) + "token.txt", "w+", encoding="utf-8") as f:
        for token in docToEdit:
            f.write(token + " ")
    return "/Doc" + str(editdoc) + "-" + str(similarity)
