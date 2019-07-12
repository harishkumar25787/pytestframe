import inspect
from allure_commons.types import AttachmentType
import pytest,os,moment,allure
from utils import utiles
browsename = utiles.browse
baseurl = utiles.baseurl

@pytest.fixture(scope="class")


def test_setup(request):
    from selenium import webdriver

    from utils import utiles
    from selenium.webdriver.ie.options import Options
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

    #global driver
    request.browsername = browsename

    if request.browsername == 'firefox':

        binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
        caps = DesiredCapabilities().FIREFOX
        caps["marionette"] = True
        driver = webdriver.Firefox(capabilities=caps, firefox_binary=binary,
                                   executable_path="D:\\Pythondriver\\geckodriver.exe")
        driver.implicitly_wait(3)
        request.cls.driver = driver
        driver.get(baseurl)
        print("Running on Firefox")

    elif request.browsername == 'chrome':
        driverLocation = "D:\\Pythondriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseurl)
        driver.maximize_window()
        request.cls.driver = driver
        driver.implicitly_wait(3)
        driver.get(baseurl)
        print("Running on Chrome")


    elif request.browsername == 'IE':
        driverLocation = "D:\\Pythondriver\\IEDriverServer.exe"
        opts  = Options()
        opts.IGNORE_ZOOM_LEVEL = True
        opts.IGNORE_PROTECTED_MODE_SETTINGS = True
        opts.require_window_focus = True
        driver = webdriver.Ie(driverLocation,opts)
        driver.get(baseurl)
        driver.maximize_window()
        request.cls.driver = driver
        driver.implicitly_wait(3)
        driver.get(baseurl)
        print("Running on IE")
    else:

        driverLocation = "D:\\Pythondriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation

        driver = webdriver.Chrome(executable_path="D:\\Pythondriver\\chromedriver.exe")

        driver.get(baseurl)
        driver.maximize_window()
        request.cls.driver = driver
        driver.implicitly_wait(3)
        driver.get(baseurl)
        print("Running on Chrome")
    yield
    driver.quit()
    print("testing completed ")
def whoami():
    return inspect.stack()[1][3]

