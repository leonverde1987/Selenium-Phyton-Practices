from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class driver_factory:

    def open_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("start-maximized")
        return webdriver.Chrome(chrome_options)