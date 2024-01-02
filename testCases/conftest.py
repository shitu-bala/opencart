import os

import pytest
from selenium import webdriver
from datetime import datetime




@pytest.fixture()  # decoration
def setup(browser):
    if browser== "edge":
         driver = webdriver.Edge()
         print ("Launching Edge browser..... ")

    elif browser== "firefox":
         driver = webdriver.Firefox()
         print("Launching Firfox browser..... ")

    else:
        driver= webdriver.Chrome()
        print("Launching Chrome browser..... ")
    return driver


def pytest_addoption(parser):
       parser.addoption("--browser")

@pytest.fixture()
def browser(request)  :
    return request.config.getoption("--browser")

def pytest_configure(config):
    config.metadata["project name"]="opencart "
    config.metadata["modual  name"] = " first opencart "
    config.metadata["tester name"] = "Shitu"
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("java_home", None)
    metadata.pop("plugins", None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\"+ datetime.now().strftime("%m/%d/%y %H-%M-%S")+".html"


