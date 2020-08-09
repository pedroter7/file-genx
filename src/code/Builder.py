'''
Builder class
'''

import gi # PyGObject
gi.require_version("Gtk", "3.0") # Require that Gtk+3.0 is imported
from gi.repository import Gtk

import logging

class Builder(Gtk.Builder):

    def __init__(self):

        super().__init__()

        logging.info("Builder instance set.")
    
    # TODO
    def getOptions(self):
        # Return dictionary with GUI options]
        pass