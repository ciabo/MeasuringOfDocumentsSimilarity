from PdfMining import rename_pdf
from PdfMining import tokenizePdf
from LSH import LSH
from Shingling import generateShingles
from MinHashing import minHash
from StringHashing import generateHash


def main():
    m = 1000000009
    pdfdir = "Document"  # pdf directory
    txtdir = "txt"  # select txt directory
    pdfname = input("Insert pdf name: ")
    rename_pdf(pdfdir)
    tokenizePdf(pdfname, txtdir)
    generateShingles(pdfname, txtdir)
    hashes = generateHash(pdfname, txtdir, m)
    # minHash()
    # LSH()


if __name__ == '__main__':
    main()
