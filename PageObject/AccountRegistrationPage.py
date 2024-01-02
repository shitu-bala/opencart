from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountReg:
    textbox_Fname_ID = "input-firstname"
    textbox_Lname_ID = "input-lastname"
    textbox_Email_ID = "input-email"
    text_Password_ID = "input-password"
    chk_Agree_Name = "//input[@name='agree']"
    btn_continue_Xpath = "//button[normalize-space()='Continue']"
    text_msg_conf_Xpath = "//a[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def setfirstname(self, Fname):
        firstname = self.driver.find_element(By.ID, self.textbox_Fname_ID)
        firstname.send_keys(Fname)

    def setlastname(self, Lname):
        lastname = self.driver.find_element(By.ID, self.textbox_Lname_ID)
        lastname.send_keys(Lname)

    def setemail(self, Email):
        email = self.driver.find_element(By.ID, self.textbox_Email_ID)
        email.send_keys(Email)

    def setpassword(self, pwd):
        password = self.driver.find_element(By.ID, self.text_Password_ID)
        password.send_keys(pwd)

    def setprivatepolicy(self):
        self.driver.find_element(By.XPATH, self.chk_Agree_Name).click()

    def clickcontinue(self):
        self.driver.find_element(By.XPATH, self.btn_continue_Xpath).click()

    def getconformationmsg(self):

        try:
            return self.driver.find_element(By.XPATH, self.text_msg_conf_Xpath).text
        except:
            None
