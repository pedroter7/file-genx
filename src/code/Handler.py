'''
Event handlers class.

Notice:
    This is a very bad implementation of the singleton design pattern.
    Nothing prevents more than one instance of Handler to be created, thus always call Handler.getInstace().

    Maybe in the future this will change :D.
'''

import gi # PyGObject
gi.require_version("Gtk", "3.0") # Require that Gtk+3.0 is imported
from gi.repository import Gtk

import logging
from inspect import currentframe, getouterframes

import Generator

class Handler:

    __uniqueInstace = None

    def __init__(self, builder):
        
        # Find who is calling
        currFrame = currentframe()
        callFrame = getouterframes(currFrame, 2)
        callerName = callFrame[1][3]

        # List all defined methods in this class
        # This assures that we get the correct name in the next if statement.
        definedMethods = list(filter(lambda x: not x.startswith("_"), dir(Handler)))

        if callerName == definedMethods[0]:
            self.__builder = builder
            logging.info("Handler instance created.")
        else:
            pass

    @staticmethod
    def getInstance(builder):

        if Handler.__uniqueInstace == None:
            Handler.__uniqueInstace = Handler(builder)
        
        return Handler.__uniqueInstace

    # Event handlers

    def onDestroy(self, *args):
        Gtk.main_quit()
        logging.info("onDestroy.")

    # TODO: freeze buttons and display dialog window
    def onGenerateClick(self, *args):
        logging.info("onGenerateClick.")
        inputs = self.__builder.getInputs()
        generator = Generator.Generator(inputs)
        generator.generate()
