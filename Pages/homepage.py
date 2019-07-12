import logging,time
from utils.Seleniumdrivers import SeleniumDriver
from selenium.webdriver.common.by import By
from utils import custom_loggers as cl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Homepage(SeleniumDriver):
    log = cl.customlogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

        self.userprofileicon_path = "//img[@class='gravatar']"
        self.logout_link = "Log Out"
        self.mycourse_linktext =  "My Courses"
        self.allcourse_lnktxt = "All Courses"



    def click_userprofile(self):

        self.driver.find_element_by_xpath(self.userprofileicon_path).click()

    def verifyloginsuccessfull(self):
        try:
             mycourse = self.driver.find_element_by_link_text(self.mycourse_linktext)
             ccourstxt = mycourse.text
             if ccourstxt in  "My Courses":
                 self.log.info(ccourstxt)
                 return True
             else:
                 return False

        except:
            return False

    def click_allcourse(self):
        self.driver.find_element_by_link_text(self.allcourse_lnktxt).click()


    def click_logout(self):
        time.sleep(5)
        self.driver.find_element_by_link_text(self.logout_link).click()

    def scrolledup_userprofile(self):
        target = self.driver.find_element_by_xpath(self.userprofileicon_path)
        target.location_once_scrolled_into_view

    def click_mycousre(self):
        self.driver.find_element_by_link_text(self.mycourse_linktext).click()
