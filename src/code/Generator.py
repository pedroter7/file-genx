'''
Generator class
'''

import logging
import ContentGenerator
import File
import time

class Generator:
    def __init__(self, inputs):

        self.__options = self.__translateInputs(inputs)
        self.__contentGenerator = ContentGenerator.ContentGenerator.factory(self.__options["type"])
        self.__configureContentGenerator()

        logging.info("Generator created.")
        
    def generate(self):
        
        PREFIX = "file"

        try:        
            file = File.File(self.__options["destPath"])
            for i in range(int(self.__options['nFiles'])):
                if self.__options["mode"].startswith("web"): time.sleep(0.25) # Try to prevent block by API
                content = self.__contentGenerator.generate()
                file.write(PREFIX, content)
            logging.info("All {} files written.".format(self.__options['nFiles']))
        except FileNotFoundError:
            logging.error("FileNotFoundError on Generator.generate().")
        except PermissionError:
            logging.error("PermissionError on Generator.generate().")

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
# logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.DEBUG)

# inputs = {
#     "nFilesSpinButton":"1",
#     "nContentSpinButton":"20",
#     "nContentComboBox":"line",
#     "contentTypeComboBoxText":"web-lipsum",
#     "destinationChooser":"/home/pedro/Documents/"
# }

# gen = Generator(inputs)
# gen.generate()