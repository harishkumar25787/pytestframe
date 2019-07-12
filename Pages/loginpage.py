import logging,inspect
from utils import custom_loggers as cl
from Pages.basepage import basepage
from utils.Seleniumdrivers import SeleniumDriver
class loginpage(SeleniumDriver):
    log = cl.customlogger(logging.DEBUG)


    def __init__(self,driver):
        self.driver = driver

        self.allcourse_linktxt = "All Courses"
        self.username_id = "user_email"
        self.password_id = "user_password"
        self.loginbutton_xpath ="//input[@name='commit']"
        self.login_linktxt = "Login"
        self.usericon_xpath = "//img[@class='gravatar']"


    def click_loginlnk(self):
        self.elementclick(self.login_linktxt, locatorType="link")

    def enter_username(self , username):
        self.sendKeys(username,self.username_id)

    def enter_password(self , password):
        self.sendKeys(password,self.password_id)

    def click_loginbutton(self):
        self.elementclick(self.loginbutton_xpath,"xpath")

    def verfiylogintitle(self):
        return self.verifyPageTitle("Let's Kode It")


    def verfiyloginscreen(self):

        locator_dict = {self.username_id:"id",self.password_id :"id",
                        self.loginbutton_xpath: "xpath",}
        result = self.verify_element_located(locator_dict)
        return result