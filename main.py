from libs import *


def main():
    Connection("http://127.0.0.1")

    #request = Connection("https://www.cdaction.pl/")
    #parser = Parser(request)
    #CDA = CDANewsExtractor(parser)
    #CDA_Raport = HTMLWriter(CDA.getsplitednews(), "file.html")
    #CDA_Raport.add_utf8()
    #CDA_Raport.add_utf8()
    #CDA_Raport.create_htmlcode()
    #CDA_PDF = PDFGenerator("file.html", "file.pdf")
    #CDA_PDF.create_pdf()


if __name__ == "__main__":
    main()
