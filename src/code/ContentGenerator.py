'''
ContentGenerator classes

ContentGenerator is supposed to be an abstract class.
'''

import logging

class ContentGenerator:

    def __init__(self):
        self.__n = int()
        self.__mode = str()

    @staticmethod
    def factory(type):
        if type == "rand":
            return RandomContentGenerator()
        elif type.startswith("web"):
            return WebContentGenerator()

    def generate(self):
        pass
    
    def configure(self, options):
        pass

class RandomContentGenerator(ContentGenerator):

    def __init__(self):
        super().__init__()

        logging.info("RandomContentGenerator created.")

    # TODO
    def generate(self):
        pass 

    def configure(self, options):
        self.__n = int(options["nContent"])
        self.__mode = options["mode"]

        logging.info("RandomContentGenerator configured.")

class WebContentGenerator(ContentGenerator):

    __SOURCES = {
        "lipsum":"lorem ipsum source url",
        "wiki":"Wikipedia source url"
    }

    def __init__(self):
        super().__init__()

        self.__source = str()

        logging.info("WebContentGenerator created.")

    # TODO
    def generate(self):
        pass

    def configure(self, options):
        self.__n = int(options["nContent"])
        self.__mode = options["mode"]
        self.__source = WebContentGenerator.__SOURCES[options["type"].split('-')[1]]

        print(self.__n, self.__mode, self.__source)

        logging.info("WebContentGenerator configured.")