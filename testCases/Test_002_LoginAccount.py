import os

import pytest

from PageObject.LoginPage import Login
from PageObject.homePage import HomePage
from utilities.CustomLogger import LogGen
from utilities.readProperties import readConfig


class Test_002_LoginAccount():
    BaseURL = readConfig.getApplicatiURL()
    logger = LogGen.loggen()
    username = readConfig.getUseremail()
    password = readConfig.getpassword()

    @pytest.mark.sanity
    def test_login_account(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.logger.info("url launching.....")
        self.driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior="auto"')
        self.hp = HomePage(self.driver)
        self.hp.clickAccount()
        self.hp.clicklogin()
        self.lg = Login(self.driver)
        self.lg.setusername(self.username)
        self.lg.setpassword(self.password)
        self.lg.clicklogin()
        self.targetpage = self.lg.isMyAccountPageExit()
        if self.targetpage == True:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\Screenshots\\" + "\\Test_Login_Page.png")
            self.driver.close()
            assert False

        self.logger.info("***Test_ login page Finished***")
