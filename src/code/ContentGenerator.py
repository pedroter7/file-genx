'''
ContentGenerator classes

ContentGenerator is supposed to be an abstract class.
'''

import logging
import string
from random import shuffle, randint
import json
import urllib.request, urllib.error, urllib.parse
import math


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

#############################################################
#############################################################
# RANDOM GENERATOR
#############################################################
#############################################################

class RandomContentGenerator(ContentGenerator):

    def __init__(self):
        super().__init__()

        logging.info("RandomContentGenerator created.")

    def generate(self):
        chars = list(string.ascii_letters + string.digits)
        shuffle(chars)
        generated = list()

        if self.__mode == 'char':
            for i in range(self.__n):
                randIndex = randint(0, len(chars)-1)
                generated.append(chars[randIndex])
            logging.info("Generated {} random chars.".format(self.__n))
        
        elif self.__mode == 'par':
            MAX_CHAR_PAR = 1000 # Max n of chars within a paragraph
            MIN_CHAR_PAR = 300 # Min n of chars within a paragraph
            NEW_PAR_CHAR = "\n\n"
            chars.append(NEW_PAR_CHAR)
            shuffle(chars)
            wChars = 0 # Used to prevent empty/too small/too big paragraphs
            wPar = 0
            while wPar < self.__n:
                randIndex = randint(0, len(chars)-1)
                nextChar = chars[randIndex]
                if nextChar == NEW_PAR_CHAR:
                    if wChars < MIN_CHAR_PAR:
                        continue
                    generated.append(nextChar)
                    wPar += 1
                    wChars = 0
                elif wChars > MAX_CHAR_PAR:
                    generated.append(NEW_PAR_CHAR)
                    wChars = 0
                    wPar += 1
                else:
                    generated.append(nextChar)
                    wChars += 1
            logging.info("Generated {} random paragraphs.".format(wPar))

        elif self.__mode == 'line':
            MAX_CHAR_LINE = 120 # Max n of chars per line
            MIN_CHAR_LINE = 20 # Min n of chars per line
            NEW_LINE_CHAR = "\n"
            chars.append(NEW_LINE_CHAR)
            shuffle(chars)
            wChars = 0 # Used to prevent empty/too small/too big paragraphs
            wLines = 0
            while wLines < self.__n:
                randIndex = randint(0, len(chars)-1)
                nextChar = chars[randIndex]
                if nextChar == NEW_LINE_CHAR:
                    if wChars < MIN_CHAR_LINE:
                        continue
                    generated.append(nextChar)
                    wChars = 0
                    wLines += 1
                elif wChars > MAX_CHAR_LINE:
                    generated.append(NEW_LINE_CHAR)
                    wChars = 0
                    wLines += 1
                else:
                    generated.append(nextChar)
                    wChars += 1
            logging.info("Generated {} random lines.".format(wLines))

        return "".join(generated)

    def configure(self, options):
        self.__n = int(options["nContent"])
        self.__mode = options["mode"]

        logging.info("RandomContentGenerator configured.")

#############################################################
#############################################################
# WEB GENERATOR
#############################################################
#############################################################

class WebContentGenerator(ContentGenerator):

    __SOURCES = {
        "lipsum":"https://baconipsum.com/api/?"
    }

    def __init__(self):
        super().__init__()

        self.__source = str()

        logging.info("WebContentGenerator created.")

    def generate(self):
        parameters = {
            "type":"meat-and-filler",
            "start-with-lorem":"1",
            "format":"json"
        }
        generate = list()

        if self.__mode == 'char':
            parameters["paras"] = str(math.ceil(self.__n / 120)) # Supposing at least 120 chars per paragraph
            url = self.__source + urllib.parse.urlencode(parameters)
            response = urllib.request.urlopen(url)
            data = json.loads(response.read().decode())
            wChar = 0
            for par in data:
                for char in par:
                    if wChar >= self.__n: break
                    generate.append(char)
                    wChar += 1                
                if wChar > self.__n: break
            logging.info("Generated {} chars from {}.".format(wChar, self.__source))
        
        elif self.__mode == 'par':
            parameters["paras"] = str(self.__n)
            url = self.__source + urllib.parse.urlencode(parameters)
            response = urllib.request.urlopen(url)
            data = json.loads(response.read().decode())
            wPar = 0
            for par in data:
                generate.append(par+'\n\n')
                wPar += 1
            logging.info("Generated {} paragraphs from {}.".format(wPar, self.__source)) 

        elif self.__mode == 'line':
            MAX_CHAR_LINE = 120
            parameters["paras"] = str(self.__n) # Supposing at least MAX_CHAR_LINE chars per paragraph
            url = self.__source + urllib.parse.urlencode(parameters)
            response = urllib.request.urlopen(url)
            data = json.loads(response.read().decode())
            wLine = 0
            wChar = 0
            for par in data:
                for char in par:
                    if wLine >= self.__n:
                        break
                    elif wChar > MAX_CHAR_LINE:
                        generate.append('\n')
                        wLine += 1
                        wChar = 0
                    else:
                        generate.append(char)
                        wChar += 1
                if wLine > self.__n:
                        break
            logging.info("Generated {} lines form {}.".format(wLine, self.__source))

        return "".join(generate)


    def configure(self, options):
        self.__n = int(options["nContent"])
        self.__mode = options["mode"]
        self.__source = WebContentGenerator.__SOURCES[options["type"].split('-')[1]]

        logging.info("WebContentGenerator configured.")