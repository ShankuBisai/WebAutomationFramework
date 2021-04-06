"""
@package base
SeleniumDriver class implementation
It implements wrappers for all the methods of selenium webdriver
This class needs to be inherited by the BasePage class
This should not be used by creating object instances
Example:
    Class BasePage(SeleniumDriver)
"""

import os

from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utilities import custom_logger as cl
import logging
import time

class SeleniumDriver:

    log = cl.customLogger(logging.DEBUG)


    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()


    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False


    def getTitle(self):
        """
        This method gets the Title of the Current Page
        :return: Title
        """
        return self.driver.title


    def getElement(self, locator):
        """
        This Method gets the Element from the Webpage
        :param locator:
        :return: Element
        """
        element = None
        try:
            for locatorType,locatorValue in locator.items():
                byType = self.getByType(locatorType)
                element = self.driver.find_element(byType, locatorValue)
            self.log.info("Element Found with locator: "+str(locator))
        except:
            self.log.info("Element not found with locator: "+str(locator))
        return element


    def getText(self,locator):
        element = None
        try:
            element=self.getElement(locator)
        except:
            self.log.error("Failed to get text on element ")
            print_stack()
            text = None
        return element.text


    def getElements(self, locator):
        elements = None
        try:
            for locatorType,locatorValue in locator.items():
                byType = self.getByType(locatorType)
                elements = self.driver.find_elements(byType, locatorValue)
            self.log.info("Element Found with locator: "+str(locator))
        except:
            self.log.info("Element not found with locator: "+str(locator))
        return elements


    def getElementList(self, locator):
        """

        :param locator:
        :param locatorType:
        :return:
        """
        element = None
        try:
            for locatorType, locatorValue in locator.items():
                byType = self.getByType(locatorType)
                elements = self.driver.find_elements(byType, locatorValue)
            self.log.info("Element List Found with locator: " + str(locator))
        except:
            self.log.info("Element List not Found with locator: " + str(locator))
        return element


    def elementClick(self, locator):
        try:
            element = self.getElement(locator)
            element.click()
            self.log.info("Clicked on element with locator: "+str(locator))
        except:
            self.log.info("Cannot click on the element with locator: "+str(locator))
            print_stack()

    def sendKeys(self, data, locator):
        try:
            element = self.getElement(locator)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: "+str(locator))
        except:
            self.log.info("Cannot send data on the element with locator: "+str(locator))
            print_stack()

    def isElementPresent(self, locator):
        try:
            element = self.getElement(locator)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False


    def isElementDisplayed(self, locator):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        element = None
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is Displayed with locator: " + str(locator))
            else:
                self.log.info("Element is not Displayed with locator: " + str(locator))
            return isDisplayed
        except:
            print("Element not found")
            return False


    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False


    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element


    def webScroll(self, direction):

        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")