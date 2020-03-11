import bs4


class Parser:

    __text = None

    def __init__(self, connection):
        self.__text = connection.getrequest().text

    def getsoup(self):
        return bs4.BeautifulSoup(self.__text, 'html.parser')


class HTMLWriter:

    __collections_to_print = None
    __filename = None
    __head_attr = []

    def __init__(self, collections, filename):
        self.__collections_to_print = collections
        self.__filename = filename

    def add_utf8(self):
        if self.__head_attr.count('<meta charset="UTF-8">\n'):
            print("UTF-8 already added. Skipping!")
        else:
            self.__head_attr.append('<meta charset="UTF-8">\n')
            print("UTF-8 added!")

    def create_htmlcode(self):
        with open(self.__filename, "w") as pdf:
            pdf.write("<!DOCTYPE html> \n <html> \n <head>\n" + "".join(self.__head_attr) + "</head> \n <body> \n")
            for part in self.__collections_to_print:
                pdf.write("<br><br><br>")
                for element in part:
                    pdf.write(element.getformat()["front-tag"] + element.getcontent() +
                              element.getformat()["end-tag"] + "<br>" + "\n")
            pdf.write("</body> \n </html>")