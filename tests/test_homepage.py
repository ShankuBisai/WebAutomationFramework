import  pytest
from pages.actions.homepage.homepage import HomePage
from pages.locators.customerpagelocator.customerpagelocators import CustomerPageLocators as locator
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("setUp")
class TestHomePage:

    @pytest.fixture(autouse=True)
    def classSetup(self, setUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_CustomerLinkClick(self):
        self.cp=self.hp.clickCustomersLink()
        elementPresent=self.cp.isElementPresent(locator.customersTrust)
        result=bool(elementPresent == True)
        self.ts.mark("test_CustomerLinkClick", result,  "CustomerLinkClickVerification")

    @pytest.mark.run(order=2)
    def test_SignInLink(self):
        self.lp=self.hp.clickSignInLink()
        result = bool(self.lp.verifyEmailIDTextBox() == True)
        self.ts.mark("test_SignInLink", result, "SignInVerification")












