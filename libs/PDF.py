from xhtml2pdf import pisa


class PDFGenerator:
    __input = None
    __output = None

    def __init__(self, inputfile, outputfile):
        self.__input = inputfile
        self.__output = outputfile

    def create_pdf(self):
        with open(self.__input, "r") as html:
            with open(self.__output, "w+b") as pdf:
                pisaStatus = pisa.CreatePDF("".join(html), dest=pdf)
