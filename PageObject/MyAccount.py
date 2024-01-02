from selenium.webdriver.common.by import By


class MyAccount():
    link_logout_xpath = "//a[@class='dropdown-item'][normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def clicklogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
