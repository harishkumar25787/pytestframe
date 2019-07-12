from selenium.webdriver.support.ui import Select
import time ,logging
from utils.Seleniumdrivers import SeleniumDriver
from utils import custom_loggers as cl
from utils import test_status
from Pages.basepage import basepage
class practicepage(SeleniumDriver):
    log = cl.customlogger(logging.DEBUG)
    def __init__(self, driver):
        self.driver = driver
        self.login_linktxt = "Login"
        self.iframe_xpath = "//iframe[@id='courses-iframe']"
        self.iframe_search_button_id= "search-course-button"
        self.iframe_txt_search_xpath = "//input[@id='search-courses']"
        self.entername_id = "name"
        self.alertpoper_id = "alertbtn"
        self.alertdismiss_id = "confirmbtn"
        self.checkbox_xpath = "//input[(@type='checkbox') and (@value = '%s')]"
        self.radio_xpath=  "//input[(@type= 'radio') and (@value = '%s')]"
        self.dropdown  = "//select[@id = 'carselect']"
        self.practic_linktxt = "Practice"

    def click_practice(self):
        self.elementclick(self.practic_linktxt,"link")


    def select_check(self,value , to_select= True):
        #xpath = self.checkbox_xpath % value
        #check_ele =self.driver.find_element_by_xpath(xpath).click()
        self.xpath = self.checkbox_xpath % value
        self.elementclick(self.xpath,"xpath")

    def select_radio(self, value, to_select=True):
        #xpath1 = self.radio_xpath % value
        #check_ele = self.driver.find_element_by_xpath(xpath1).click()
        self.xpath1 = self.radio_xpath % value
        self.elementclick(self.xpath1,"xpath")
    def select_dropdown(self,value):
        Sel =Select(self.driver.find_element_by_xpath(self.dropdown ))
        Sel.select_by_visible_text(value)


    def alert_accept(self,entername):
        self.sendKeys(entername,self.entername_id)
        self.elementclick(self.alertpoper_id,"id")
        time.sleep(2)
        self.driver.switch_to_alert().accept()

    def alert_dismiss(self):
        self.elementclick(self.alertdismiss_id,"id")
        time.sleep(2)
        self.driver.switch_to_alert().dismiss()

    def iframe_acion_Search(self , value):
        iframe = self.driver.find_element_by_xpath(self.iframe_xpath)
        self.driver.switch_to.frame(iframe)
        #self.driver.find_element_by_xpath(self.iframe_txt_search_xpath).send_keys(value)
        self.sendKeys(value,self.iframe_txt_search_xpath,"xpath")
        #self.driver.find_element_by_id(self.iframe_search_button_id).click()
        self.elementclick(self.iframe_search_button_id,"id")

    def verfiypracticepage(self):
        locator_dict = {self.entername_id: "id", self.alertpoper_id: "id",
                        self.alertdismiss_id:"id",self.practic_linktxt: "link"}
        result = self.verify_element_located(locator_dict)
        return result

    def logintxt(self):
        result = self.driver.find_element_by_link_text(self.login_linktxt).is_displayed()
        return