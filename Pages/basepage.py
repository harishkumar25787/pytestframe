import logging,inspect
from traceback  import print_stack
from utils import custom_loggers as cl
from utils.Seleniumdrivers import SeleniumDriver
class basepage(SeleniumDriver):
    log = cl.customlogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.practice_lintext = "Practice"
        self.login_lintext = "Login"
        self.Signup_lintxt = "Signup"
        self.class_welcom = " //h2[@class='headline']"

    def backbase(self):
        try:

            element = self.driver.find_element_by_xpath(self.class_welcom)

            elele = element.text
            if elele in "Welcome to Let's Kode It":

                self.log.info(elele)
                return True
            else:
                return False
        except:
            return False


    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

