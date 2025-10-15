import unittest

from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def test_hello_world(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        driver.quit()


