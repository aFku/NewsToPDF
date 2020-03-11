import requests


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