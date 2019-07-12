from Pages.homepage import Homepage
from Pages.loginpage import loginpage
import logging,conftest,pytest,unittest
from utils import test_status
from utils import custom_loggers as cl
from Pages.homepage import Homepage
from Pages.basepage import basepage
from utils.test_status import TestStatus
from utils.Data_Reader import  DataReader

@pytest.mark.usefixtures("test_setup")
class Testloginpage(unittest.TestCase):
     log = cl.customlogger(logging.DEBUG)
     data_reader = DataReader()
     @pytest.fixture(autouse=True)

     def classsetup(self,test_setup,request):
          self.HU    = Homepage(self.driver)
          self.login = loginpage(self.driver)
          self.base = basepage(self.driver)
          self.Teststatuser = TestStatus(self.driver)
          if self.data_reader.get_data(request.function.__name__,"Runmode")!="Y":
               pytest.skip("Excluded from current execution ")

     @pytest.mark.order1
     def test_login1(self):
          testname = conftest.whoami()
          self.login.click_loginlnk()

          result = self.login.verfiyloginscreen()
          self.Teststatuser.markFinal(testname,result,"Login element are present")
          self.login.enter_username("test@email.com")
          self.login.enter_password("abcabc")
          self.login.click_loginbutton()
          result2 =  self.HU.verifyloginsuccessfull()

          self.Teststatuser.mark(result2,"login sucess")
          result1 = self.HU.verifyloginsuccessfull()
          self.Teststatuser.markFinal(testname,result1,"login was scuess" )

     @pytest.mark.order2
     def test_logout(self):
          testname = conftest.whoami()
          #logout.click_mycousre()
          self.HU.click_userprofile()
          self.HU.click_logout()
          result3 = self.base.backbase()
          self.Teststatuser.mark(result3, "log out scuess")
          result2 = self.base.backbase()
          self.Teststatuser.markFinal(testname,result2, "log out sucess"  )











