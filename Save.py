def SaveMinHash(minHash):
    txtname = "./StoredData/minHash.txt"
    with open(txtname, "w+", encoding='utf-8') as f:
        for list in minHash:
            for element in list:
                f.write(str(int(element)) + ",")
            f.write("\n")


def Saveab(ablist):
    txtname = "./StoredData/ab.txt"
    with open(txtname, "w+", encoding='utf-8') as f:
        for element in ablist:
            f.write(str(element[0]) + "," + str(element[1]) + "\n")
