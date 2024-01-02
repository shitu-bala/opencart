import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + "\\configurations\\config.ini")


class readConfig:
    @staticmethod
    def getApplicatiURL():
        url = (config.get('commonInfo', 'baseURL'))
        return url

    @staticmethod
    def getUseremail():
        email = (config.get('commonInfo', 'email'))
        return email

    @staticmethod
    def getpassword():
        password = (config.get('commonInfo', 'password'))
        return password
