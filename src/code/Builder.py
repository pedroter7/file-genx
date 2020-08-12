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
    
    def getInputs(self):
        '''
        {"widgetName":"value"}
        '''
        inputs = dict()
        # Get widgets objects
        objectsList = self.get_objects()

        for obj in objectsList:
            # Get widget name
            widgetName = None
            value = None
            try:
                widgetName = obj.get_name()
            except AttributeError: # object has no name attribute
                continue

            # Find method and get value
            if obj.__class__ == Gtk.SpinButton:
                value = str(int(obj.get_value()))
            elif obj.__class__ == Gtk.ComboBoxText:
                value = str(obj.get_active_id())
            elif obj.__class__ == Gtk.FileChooserButton:
                value = str(obj.get_filename())

            if value is None:
                logging.error("Builder could not get input value for {} widget.".format(widgetName))
            else:
                # Append to dict
                inputs[widgetName] = value
        
        return inputs
            