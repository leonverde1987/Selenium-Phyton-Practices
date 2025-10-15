import unittest

from helper.driver_factory import driver_factory
from pages.loginPage import LoginPage


class loginTestScripts(unittest.TestCase):

    def test_login_success(self):

        driver = driver_factory().open_chrome_driver()

        logpage = LoginPage(driver)
        logpage.goto(driver)
        logpage.login(driver, "customer@practicesoftwaretesting.com","welcome01")
        logpage.validate_session("My account")


