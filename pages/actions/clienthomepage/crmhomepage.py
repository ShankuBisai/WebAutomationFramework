from base.basepage import BasePage
from utilities import custom_logger as cl
import logging
from pages.locators.clienthomepagelocaotors.crmhomepagelocator import CRMHomePageLocator as locator


class CRMHomePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def clickCreateIcon(self):
        self.elementClick(locator.createIcon)


    def clickContacts(self):
        self.elementClick(locator.contacts)






