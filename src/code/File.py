'''
File class.
'''

import logging

class File:

    __suffix = 0

    def __init__(self, path):
        
        self.__path = path

    def write(self, prefix, content):

        fileName = "{}/{}-{}".format(self.__path, prefix, File.__suffix)
        logging.info("Writting to {}.".format(fileName))        
        outFile = open(fileName, 'w')
        outFile.write(content)
        outFile.close()
        logging.info("File {} wrote.".format(prefix+str(File.__suffix)))
        File.__suffix += 1