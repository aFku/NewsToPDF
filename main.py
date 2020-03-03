import bs4, requests
import collections

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
        #write some format after setting up pdf printer
        return "Title format"

    def __str__(self):
        return "Title"


class Description(Element):

    def getformat(self):
        #write some format after setting up pdf printer
        return "Description format"

    def __str__(self):
        return "Description"


class Image(Element):

    def getformat(self):
        #write some format after setting up pdf printer
        return "Image format"

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


class RaportPDFGenerator:

    __collections_to_print = None

    def __init__(self, collections):
        self.__collections_to_print = collections

    def test_print_collection(self):
        for News in self.__collections_to_print:
            for element in News:
                try:
                    print(str(element))
                except:
                    pass
                print("\n")
                print(element.getcontent())
                print("\n\n")
                print(element.getformat())
                print("\n\n ############### \n\n")



def main():
    request = Connection("https://www.cdaction.pl/")
    parser = Parser(request)
    CDA = CDANewsExtractor(parser)
    CDA_Raport = RaportPDFGenerator(CDA.getsplitednews())
    CDA_Raport.test_print_collection()


if __name__ == "__main__":
    main()
