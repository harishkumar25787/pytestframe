import inspect
import logging ,os,sys
from datetime import datetime

def customlogger(logLevel = logging.INFO):

# Gets the name of the class / method from where this method is called
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    #get all log message
    logger.setLevel(logging.DEBUG)

    filehandler = logging.FileHandler("Automation.log",mode='a')
    filehandler.setLevel(logLevel)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger