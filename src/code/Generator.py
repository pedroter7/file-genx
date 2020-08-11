'''
Generator class
'''

import logging
import ContentGenerator

class Generator:
    def __init__(self, inputs):

        self.__options = self.__translateInputs(inputs)
        print(self.__options["type"])
        self.__contentGenerator = ContentGenerator.ContentGenerator.factory(self.__options["type"])
        self.__configureContentGenerator()

        logging.info("Generator created.")
        

    # TODO
    def generate(self):
        pass

    def __translateInputs(self, inputs):
        TRANSLATION_TABLE = {
            "nFilesSpinButton":"nFiles",
            "nContentSpinButton":"nContent",
            "nContentComboBox":"mode",
            "contentTypeComboBoxText":"type",
            "destinationChooser":"destPath"
        }

        translated = dict()

        for key in inputs.keys():
            translated[TRANSLATION_TABLE[key]] = inputs[key]

        return translated

    def __configureContentGenerator(self):
        self.__contentGenerator.configure(self.__options)

###########################################
'''         TEST LINES      IGNORE      '''
###########################################
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.DEBUG)

inputs = {
    "nFilesSpinButton":"15",
    "nContentSpinButton":"30",
    "nContentComboBox":"line",
    "contentTypeComboBoxText":"rand",
    "destinationChooser":"/home/pedro/Documents/"
}

gen = Generator(inputs)