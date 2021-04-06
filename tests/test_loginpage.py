from pages.actions.homepage.homepage import HomePage
from pages.actions.loginpage import LoginPage
import pytest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("setUp")
class TestLoginPage:

    @pytest.fixture(autouse=True)
    def classSetup(self,setUp):
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=1)
    def test_Login(self):
        self.hp.clickSignInLink()
        self.chp=self.lp.login("shankubisai3333@gmail.com", "shanku12345#")
        result=bool(self.chp.verifyUserIcon() == True)
        self.ts.mark("test_Login",result,"LoginVerification")



    @pytest.mark.run(order=2)
    def test_InvalidLogin(self):
        self.hp.clickSignInLink()
        self.lp.clickNextButton()
        result=bool(self.lp.getErrorSignText() == "Please enter your email address or mobile number")
        self.ts.mark("test_InvalidLogin", result, "InvalidLoginVerification")



    @pytest.mark.run(order=3)
    def test_LoginPageTitle(self):
        self.hp = HomePage(self.driver)
        self.hp.clickSignInLink()
        self.lp = LoginPage(self.driver)
        result = bool(self.lp.verifyLoginPageTitle() == "Zoho Accounts")
        self.ts.mark("test_LoginPageTitle", result, "LoginPageTitle")























