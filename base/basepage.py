"""
@package base
Base Page class implementation
It implements methods which are common to all the pages throughout the application
This class needs to be inherited by all the page classes
This should not be used by creating object instances
Example:
    Class LoginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class
        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver

    def verifyPageTitle(self):
        """
        Verify the page Title
        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            return self.getTitle()
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def verifyPageText(self,locator):
        """
        Verify the text on Page
        """
        try:
            return self.getText(locator)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
