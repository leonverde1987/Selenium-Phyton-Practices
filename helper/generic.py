from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Generic:


    def __init__(self, driver):
        self.driver = driver

    def make_click(self, element):
        self.wait_displayed_element(element)
        self.driver.find_element(*element).click()

    def type_keys(self, driver, element, keys):
        self.wait_displayed_element(element)
        self.driver.find_element(*element).send_keys(keys)

    def get_text_of_element(self, element):
        self.wait_displayed_element(element)
        print('text: '+self.driver.find_element(*element).text)
        return self.driver.find_element(*element).text

    def wait_displayed_element(self, element):
        wait = WebDriverWait(self.driver, timeout = 3)
        wait.until(lambda _ : self.driver.find_element(*element).is_displayed())

    def wait_element_exception(self, element):
        errors = [NoSuchElementException]
        wait = WebDriverWait(self.driver, timeout = 10, poll_frequency=.2, ignored_exceptions=errors)
        wait.until(EC.presence_of_element_located((By.XPATH, element)))

