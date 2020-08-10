'''
Resources management class.

Notice:
    This is a very bad implementation of the singleton design pattern.
    Nothing prevents more than one instance of Res to be created, thus always call Res.getInstace().

    Maybe in the future this will change :D.
'''

import logging
import json
from inspect import currentframe, getouterframes

class Res:

    __uniqueInstace = None
    __PATH = "resources/resources.json"

    def __init__(self):

        # Find who is calling
        currFrame = currentframe()
        callFrame = getouterframes(currFrame, 2)
        callerName = callFrame[1][3]

        # List all defined methods in this class
        # This assures that we get the correct name in the next if statement.
        definedMethods = list(filter(lambda x: not x.startswith("_"), dir(Res)))

        if callerName == definedMethods[0]:
            self.Strings = dict()
            self.__loadResources()
            logging.info("Res instance created.")
        else:
            pass
        
    @staticmethod
    def getInstace():
        
        if Res.__uniqueInstace == None:
            Res.__uniqueInstace = Res()
            
        return Res.__uniqueInstace

    def __loadResources(self):
        
        try:
            jsonFile = open(Res.__PATH, 'r')
            data = json.load(jsonFile)
            
            # Populate Strings dictionary
            self.Strings = data['Strings']
        except FileNotFoundError:
            logging.error("Could not find resources.json file.")
        except json.decoder.JSONDecodeError:
            logging.error("Something is wrong with the resources.json content.")
        finally:
            jsonFile.close()
