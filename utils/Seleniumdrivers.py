from selenium.webdriver.common.by import By
from traceback import print_stack
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utils import custom_loggers as cl
import logging,time,os,unittest
import moment,allure,os,time,logging,random,string
from utils import utiles

class SeleniumDriver(unittest.TestCase):

    log = cl.customlogger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver

    def screenshots(self,testname):
        try:



                x = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
                y = testname + x
                print("Captured the Screenshot named::", y)
                self.driver.get_screenshot_as_file(
                    y + ".PNG")
        except:
            self.log.info("Exception Occured while taking screenshot")
        # Below line works fine with allure adopter
        # allure.MASTER_HELPER.attach(name=y, contents=self.driver.get_screenshot_as_png(),
        #                             type=allure.MASTER_HELPER.attach_type.PNG)

        # Below line works fine with allure-pytest
        allure.attach(self.driver.get_screenshot_as_png(), name=y, attachment_type=allure.attachment_type.PNG)



    def wait_for_element_to_be_clickable(self,  locator, locatorType="xpath", max_time_out=10):

        """
        This function is used for explicit waits till element clickable
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns the boolean value according to the element located or not
        """

        try:
            WebDriverWait(self.driver, max_time_out, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.element_to_be_clickable((self.get_locator_type(locatorType), locator)))
            return True
        except:
            self.log.error("Exception occurred while waiting for element to be clickable.")
            return False

    def getTitle(self):
        return self.driver.title

    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string

        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False



    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType =="xpath":
            return By.XPATH
        elif locatorType =="css":
            return By.CSS_SELECTOR
        elif locatorType =="class":
            return By.CLASS_NAME
        elif locatorType =="name":
            return By.NAME
        elif locatorType =="link":
            return By.LINK_TEXT
        else:
            self.log.info(" Locator type " + locatorType +
                          "not correct/supported")

    def getlelement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            self.log.info("Element found with locator : " + locator +
                          "  and locator type " + locatorType)
        except:
            self.log.info("Element not found with locator : " + locator +
                          "  and locator type " + locatorType)
        return element

    def elementclick(self,locator,locatorType ="id"):
        try:

            element = self.getlelement(locator,locatorType)
            element.click()
            self.log.info("clicked on element with locator :" + locator +
                          " locatorType :" + locatorType)
        except:
            self.log.info(" Cannot clicked on element with locator :" + locator +
                          " locatorType :" + locatorType)
            print_stack()

    def sendKeys(self,data,locator,locatorType= "id"):
        try:
            element = self.getlelement(locator,locatorType)
            element.send_keys(data)
            self.log.info("Send data on element with :" + locator
                          + "locatorType :" + locatorType)
        except:
            self.log.info(" Cannot Send data on element with :" + locator +
                          "locatorType :" + locatorType)
            print_stack()

    def wait_for_element_to_be_present(self,locator_properties,locatorType = "id", max_time_out = 10):
        try:
            WebDriverWait(self.driver, max_time_out, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.presence_of_element_located((self.getByType(locatorType), locator_properties)))
            return True
        except:
            return False



    def verify_element_located(self,locator_dict,max_timeout=10):
        flag = False
        result = []
        try:
            for locator_prop in locator_dict.keys():
                prop_type = locator_dict[locator_prop]
                if self.wait_for_element_to_be_present(locator_prop, prop_type, max_timeout):
                    self.log.info(
                        "Element found with locator_properties " +  locator_prop +  " and locator_type :: " + locator_dict[
                            locator_prop])
                    flag = True
                else:
                    self.log.error(
                        "Element not found with locator_properties" + locator_prop + " and locator_type" + locator_dict[
                            locator_prop])
                    flag = False
                result.append(flag)
        except Exception as Ex:
            self.log.error("Exception Occured during element identification", Ex)

        if False in result:
            return  False
        else:
            return  True








