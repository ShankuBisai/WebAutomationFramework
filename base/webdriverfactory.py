"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverFactory():

    def __init__(self, browser,headless="false"):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
        self.headless = headless
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://www.zoho.com/"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            if (self.headless == "false"):
                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            else:
                options = webdriver.FirefoxOptions()
                options.headless = True
                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

        elif self.browser == "chrome":
            if (self.headless == "false"):
                driver = webdriver.Chrome(ChromeDriverManager().install())
            else:
                options = Options()
                options.headless = True
                options.add_argument('--allow-running-insecure-content')
                options.add_argument('--ignore-certificate-errors')
                prefs = {"profile.default_content_setting_values.notifications": 2}
                options.add_experimental_option("prefs", prefs)
                driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        else:
            driver = webdriver.Firefox()

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver