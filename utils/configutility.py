#This module contains config utility functions.


from traceback import print_stack
from configparser import ConfigParser
from utils import custom_loggers
import logging
import os
import time

from utils import custom_loggers as cl
class ConfigUtility:
    """
    #This class includes basic reusable config_helpers.
    """

    log = cl.customlogger(logging.DEBUG)

    def __init__(self):
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.config_path = os.path.join(self.cur_path, r"../utils/config.ini")

    def load_properties_file(self):

        config = None
        try:
            # noinspection PyBroadException
            config = ConfigParser()
            config.read(self.config_path)

        except Exception as ex:
            self.log.error("Failed to load ini/properties file.", ex)
            print_stack()

        return config

    def change_properties_file(self, section, property_name, property_value):
        #
        #This method is used to change the property value
        #:param section: property section in ini file
        #:param property_name: property name to change
        #:param property_value: property value to set
        #:return: it returns boolean value for successful change property operation
        ###    
        try:
            config = self.load_properties_file()
            config[section][property_name] = property_value

            with open(self.config_path, 'w') as configfile:
                config.write(configfile)

            time.sleep(1)

            return True

        except Exception as ex:
            self.log.error("Failed to change ini/properties file.", ex)
            print_stack()
            return False