from selenium.webdriver.common.by import By



class Login():

    textbox_email_ID ="input-email"
    textbox_password_ID= "input-password"
    btn_login_Xpath= "//button[@type='submit']"
    msg_myaccount_Xpath ="//h2[normalize-space()='My Account']"

    def __init__(self, driver):
        self.driver = driver


    def setusername(self , email):
      user = self.driver.find_element(By.ID,self.textbox_email_ID)
      user.send_keys(email)

    def setpassword(self,pwd):
        password = self.driver.find_element(By.ID,self.textbox_password_ID)
        password.send_keys(pwd)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self. btn_login_Xpath).click()

    def isMyAccountPageExit(self):
        try:
           return self.driver.find_element(By.XPATH,self.msg_myaccount_Xpath).is_displayed()

        except:
            return False

