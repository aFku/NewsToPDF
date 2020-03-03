import bs4, requests
import collections
import pdfkit

class Element:

    __content = None

    def __init__(self, part_of_news):
        self.__content = part_of_news

    def getcontent(self):
        return self.__content

    def getformat(self):
        #interface
        pass


class Title(Element):

    def getformat(self):
        return {"front-tag": "<h1>", "end-tag": "</h1>"}

    def __str__(self):
        return "Title"


class Description(Element):

    def getformat(self):
        return {"front-tag": "<p>", "end-tag": "</p>"}

    def __str__(self):
        return "Description"


class Image(Element):

    __urlimg = None

    def __init__(self, part_of_news):
        super().__init__("")
        self.__urlimg = part_of_news


    def getformat(self):
        return {"front-tag": "<img src=" + self.getimgurl() + " >", "end-tag": ""}

    def getimgurl(self):
        return self.__urlimg

    def __str__(self):
        return "Image"


class Connection:

    __url = None
    __request = None

    def __init__(self, url):
        self.__url = url
        self.__request = requests.get(url)

    def geturl(self):
        return self.__url

    def getrequest(self):
        return self.__request


class Parser:

    __text = None

    def __init__(self, connection):
        self.__text = connection.getrequest().text

    def getsoup(self):
        return bs4.BeautifulSoup(self.__text, 'html.parser')


class CDANewsExtractor:
    __soup = None

    def __init__(self, parser):
        self.__soup = parser.getsoup()

    def __scrapallnews(self):
        container = self.__soup.find("div", id="newsy")
        container = container.find_all("div", {"class": "news"})
        return container

    def ___getalltitles(self):
        content = []
        for div in self.__scrapallnews():
            content.append(div.a.text)
        return content

    def __getalldescrp(self):
        content = []
        for div in self.__scrapallnews():
            content.append(div.find("table").find("p").text)
        return content

    def __getallimages(self):
        content = []
        for div in self.__scrapallnews():
            content.append("https://www.cdaction.pl" + div.find("table").find("img").get("src"))
        return content

    def getsplitednews(self):
        News = collections.namedtuple("News", ["title", "descrp", "image"])
        return [News(Title(title), Description(descrp), Image(image)) for title, descrp, image in zip(
                                                                                                self.___getalltitles(),
                                                                                                self.__getalldescrp(),
                                                                                                self.__getallimages())]


class HTMLWriter:

    __collections_to_print = None
    __filename = None

    def __init__(self, collections, filename):
        self.__collections_to_print = collections
        self.__filename = filename

    def create_htmlcode(self):
        with open(self.__filename, "w") as pdf:
            pdf.write("<!DOCTYPE html> \n <html> \n <head></head> \n <body> \n")
            for part in self.__collections_to_print:
                pdf.write("<br><br><br>")
                for element in part:
                    pdf.write(element.getformat()["front-tag"] + element.getcontent() +
                              element.getformat()["end-tag"] + "<br>" + "\n")
            pdf.write("</body> \n </html>")


class PDFGenerator:
    __input = None
    __output = None

    def __init__(self, inputfile, outputfile):
        self.__input = inputfile
        self.__output = outputfile

    def create_pdf(self):
        with open(self.__input, "r") as html:
            pdfkit.from_file(html, self.__output)


def main():
    request = Connection("https://www.cdaction.pl/")
    parser = Parser(request)
    CDA = CDANewsExtractor(parser)
    CDA_Raport = HTMLWriter(CDA.getsplitednews(), "file.html")
    CDA_Raport.create_htmlcode()
    CDA_PDF = PDFGenerator("file.html", "file.pdf")
    CDA_PDF.create_pdf()




if __name__ == "__main__":
    main()
