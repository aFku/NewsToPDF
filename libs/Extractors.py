from .Elements import *
import collections


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