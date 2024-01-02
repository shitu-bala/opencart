import os
import time

import pytest
from PageObject.MyAccount import MyAccount
from PageObject.LoginPage import Login
from PageObject.homePage import HomePage
from utilities.CustomLogger import LogGen
from utilities.readProperties import readConfig
from utilities import XLUtils


class Test_LoginAccout_DDT():
    BaseURL = readConfig.getApplicatiURL()
    logger = LogGen.loggen()
    path = (os.path.abspath(os.curdir) + "\\testData\\opencart_logindata.xlsx")
    @pytest.mark.regression
    def test_loginact_ddt(self, setup):
        self.logger.info("stating test_0003_data driven testing ......")
        self.rows = XLUtils.GetRowCount(self.path, "Sheet1")
        lst_status = []

        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.logger.info("url launching.....")
        self.hp = HomePage(self.driver)
        self.lg = Login(self.driver)
        self.ma = MyAccount(self.driver)
        for r in range(2, self.rows + 1):

            self.hp.clickAccount()
            self.hp.clicklogin()

            self.email = XLUtils.ReadData(self.path, "Sheet1", r, 1)
            self.pwd = XLUtils.ReadData(self.path, "Sheet1", r, 2)
            self.result = XLUtils.ReadData(self.path, "Sheet1", r, 3)
            self.lg.setusername(self.email)
            self.lg.setpassword(self.pwd)
            self.lg.clicklogin()
            time.sleep(2)

            self.targetpage = self.lg.isMyAccountPageExit()
            if self.result == "valid":
                if self.targetpage == True:

                    lst_status.append("pass")
                    self.ma.clicklogout()
                else:
                    lst_status.append("fail")

            elif self.result == "invalid":
                if self.targetpage == True:
                    lst_status.append("fail")
                    self.ma.clicklogout()
                else:
                    lst_status.append("pass")

        self.driver.close()
        if "fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("***Test_ login page Finished***")
