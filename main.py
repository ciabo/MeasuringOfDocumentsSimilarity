from PdfMining import rename_pdf
from PdfMining import tokenizePdf
from LSH import LSH
from Shingling import generateShingles
from MinHashing import minHash
from StringHashing import generateHash


def main():
    m = 1000000009
    pdfname = input("Insert pdf name: ")
    rename_pdf()
    tokenizePdf(pdfname)
    generateShingles(pdfname)
    generateHash(pdfname, m)
    # minHash()
    # LSH()


if __name__ == '__main__':
    main()
