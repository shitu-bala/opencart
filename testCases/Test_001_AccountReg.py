import os.path
import time

import pytest

from PageObject.AccountRegistrationPage import AccountReg
from PageObject.homePage import HomePage
from utilities import randomstring
from utilities.readProperties import readConfig
from utilities.CustomLogger import LogGen


class Test_001_AccountReg():
    BaseURL = readConfig.getApplicatiURL()
    logger = LogGen.loggen()
    @pytest.Mark.sanity
    def test_account_reg(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)

        self.logger.info("***Test_ApplicarionRegistrationStarted***")
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior="auto"')
        # self.driver.implicitly_wait(10)
        self.hp = HomePage(self.driver)
        self.hp.clickAccount()
        self.hp.clickRegister()
        self.logger.info("applicant information form ")
        self.acpg = AccountReg(self.driver)
        self.driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior="auto"')
        self.acpg.setfirstname("Ayaana")
        self.acpg.setlastname("Vermaa")
        self.email = randomstring.random_string_gener() + "@gamil.com"
        self.logger.info("email entered")

        self.acpg.setemail(self.email)

        self.acpg.setpassword("aanbhhgtyu@1234")

        self.acpg.setprivatepolicy()
        self.acpg.clickcontinue()

        self.msg = self.acpg.getconformationmsg()

        if self.msg == "Your Account Has Been Created!":
            self.logger.info("*** registration Account  created ***")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\Screenshots\\" + "\\Test_account_Reg.png")
            self.logger.error(" Account registration failed")
            self.driver.close()
            assert False
            self.logger.info("***Test_ApplicarionRegistrationFinished***")
