'''
Title: File Genx
License: MIT
GitHub: https://github.com/pedroter7/file-genx

This script is the starting point of the application. Call this from src directory.
'''

import MainWidget
import logging
import pathlib

# Define log file path
logPath = str(pathlib.Path(__file__).parent.absolute()) + "/file-genx-log.txt"

# Logging configuration
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.DEBUG, filename=logPath)

mainInstance = MainWidget.MainWidget()
mainInstance.launch()
logging.info("Application exited.")