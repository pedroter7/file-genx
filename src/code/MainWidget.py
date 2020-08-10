'''
MainWidget class. An instance of this class starts everything.
'''

import gi # PyGObject
gi.require_version("Gtk", "3.0") # Require that Gtk+3.0 is imported
from gi.repository import Gtk

import Builder
import Handler
import Res

import logging

class MainWidget:

    __GLADEPATH = "layout/AppLayout.glade"

    def __init__(self):

        self.__builder = Builder.Builder()
        self.__handler = Handler.Handler.getInstance(self.__builder)
        self.__res = Res.Res.getInstace()

        if self.__builder.add_from_file(MainWidget.__GLADEPATH) == 0:
            logging.error("Something happened when trying to add AppLayout.glade to Builder.")

        self.__bindHandler()
        self.__bindRes()

        logging.info("MainWidget instance set.")

    def __bindRes(self):
        # Bind strings
        '''
        self.__res.Strings template:
            { “object-name”: [ “method-to-call-name”, “string-value” ] }
        '''
        for obj in self.__builder.get_objects():
            try:
                objName = obj.get_name() # Using widget name and not ID!!!!!!!
                if objName in self.__res.Strings.keys():
                    toCall = getattr(obj, self.__res.Strings[objName][0])
                    for callParameters in self.__res.Strings[objName][1]:
                        toCall(*callParameters) # Using splat operator
            except AttributeError: # obj has no get_name() method
                pass

    def __bindHandler(self):

        self.__builder.connect_signals(self.__handler)

        logging.info("Event handlers binding done.")
    
    def launch(self):

        window = self.__builder.get_object("mainWindow")
        window.show_all()

        Gtk.main()

    def getBuilder(self):
        return self.__builder