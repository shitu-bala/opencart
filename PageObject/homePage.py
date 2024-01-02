from selenium.webdriver.common.by import By


class HomePage():
    link_myacoount_xpath ="//span[normalize-space()='My Account']"
    link_register_linktext = "Register"
    link_login_linktext = "Login"


    def __init__(self, driver):
        self.driver = driver
    def clickAccount(self):
        self.driver.find_element(By.XPATH, self. link_myacoount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.link_register_linktext).click()

    def clicklogin(self):
        self.driver.find_element(By.LINK_TEXT,self.link_login_linktext).click()
