from base.basepage import BasePage
from utilities import custom_logger as cl
import logging

class CustomerPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)



