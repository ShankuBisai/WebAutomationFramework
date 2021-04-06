import pytest

from pages.actions.homepage.homepage import HomePage
from pages.actions.loginpage import LoginPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("setUp")
class TestClientHomePage:

    @pytest.fixture(autouse=True)
    def classSetup(self, setUp):
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_UserIcon(self):
        self.hp.clickSignInLink()
        self.chp = self.lp.login("shankubisai3333@gmail.com", "shanku12345#")
        result = bool(self.chp.verifyUserIcon() == True)
        self.ts.mark("test_UserIcon", result, "UserIconVerification")






