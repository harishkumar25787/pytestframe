import allure,logging
from Pages.basepage import basepage
from utils.test_status import TestStatus
from Pages.homepage import Homepage
from Pages.loginpage import loginpage
from Pages.practicepage import practicepage

from selenium import  webdriver
import  os,moment,conftest,sys
import pytest,unittest
from utils import custom_loggers as cl
from utils.Data_Reader import  DataReader
@pytest.mark.usefixtures("test_setup")
class Testpractic(unittest.TestCase):
    log = cl.customlogger(logging.DEBUG)
    data_reader = DataReader()
    @pytest.fixture(autouse=True)
    def classsetup(self,test_setup,request):

        self.login = loginpage(self.driver)
        self.practice = practicepage(self.driver)
        self.HU = Homepage(self.driver)
        self.base = basepage(self.driver)
        self.Teststatuser = TestStatus(self.driver)
        if self.data_reader.get_data(request.function.__name__, "Runmode") != "Y":
            pytest.skip("Excluded from current execution ")
    @pytest.mark.order1
    def test_login2(self):
        self.login.click_loginlnk()
        self.login.enter_username("test@email.com")
        self.login.enter_password("abcabc")
        self.login.click_loginbutton()
        print("login was successfull")

    @pytest.mark.order2
    def test_prac(self):
        testname = conftest.whoami()
        self.practice.click_practice()
        result = self.practice.verfiypracticepage()
        self.Teststatuser.markFinal(testname,result,"Practicage page verified ")
        self.practice.select_check("bmw")
        self.practice.select_check("benz")
        self.driver.implicitly_wait(3)
        self.practice.select_radio("benz")
        self.practice.select_dropdown("Honda")

    @pytest.mark.order3
    def test_pract2(self):
        self.practice.alert_accept("harish")
        self.practice.alert_dismiss()

    @pytest.mark.order4
    def test_pract3(self):
        self.practice.iframe_acion_Search("java")

    @pytest.mark.order5
    def test_pract4logout(self):
        self.driver.switch_to.default_content()
        # self.HU.scrolledup_userprofile()
        self.HU.click_userprofile()
        self.HU.click_logout()
        result = self.base.backbase()
        testname = conftest.whoami()
        self.Teststatuser.mark(result, "log was sucessful")
        result1 = self.base.backbase()
        self.Teststatuser.markFinal(testname, result1, "log out sucess")










