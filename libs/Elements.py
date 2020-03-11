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