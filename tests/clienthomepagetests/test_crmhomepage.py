import pytest
import time
from pages.actions.clienthomepage.clienthomepage import ClientHomePage
from pages.actions.clienthomepage.crmhomepage import CRMHomePage
from pages.actions.homepage.homepage import HomePage
from pages.actions.loginpage.loginpage import LoginPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("setUp")
class TestCRMHomePage:

    @pytest.fixture(autouse=True)
    def classSetup(self, setUp):
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.chp = ClientHomePage(self.driver)
        self.crmhomepage = CRMHomePage(self.driver)
        self.ts = TestStatus(self.driver)


    pytest.mark.run(order = 1)
    def test_addContacts(self):
        self.hp.clickSignInLink()
        self.chp = self.lp.login("shankubisai3333@gmail.com", "shanku12345#")
        self.chp.clickCRMOption()
        time.sleep(10)
        self.crmhomepage.clickCreateIcon()
        time.sleep(10)
        self.crmhomepage.clickContacts()


