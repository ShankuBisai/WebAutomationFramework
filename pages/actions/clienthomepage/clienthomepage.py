from base.basepage import BasePage
from pages.actions.clienthomepage.crmhomepage import CRMHomePage
from pages.locators.clienthomepagelocaotors.clienthomepagelocators import ClientHomePageLocators as locator
from utilities import custom_logger as cl
import logging

class ClientHomePage(BasePage):


    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def verifyUserIcon(self):
        return self.isElementPresent(locator.clientImage)

    def clickUserIcon(self):
        self.elementClick(locator.clientImage)

    def verifyUserName(self):
        return self.getText(locator.clientName)

    def clickCRMOption(self):
        self.elementClick(locator.crmoption)
        return CRMHomePage(self.driver)





