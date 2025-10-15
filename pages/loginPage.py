from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from helper.generic import Generic


class LoginPage(Generic):
    def __init__(self, driver):
        self.driver = driver
        self.username_field =  (By.ID, "email")
        self.password_field =  (By.ID, "password")
        self.login_button =  (By.XPATH, "//*[contains(@class,'btnSubmit')]")
        self.title_page =  (By.XPATH, "//h1[@data-test='page-title']")

    def goto(self, driver):
        driver.get("https://practicesoftwaretesting.com/auth/login")

    def login(self, driver, name, password):
        self.type_keys(self.driver, self.username_field, name)
        self.type_keys(self.driver, self.password_field, password)
        self.make_click(self.login_button)

    def validate_session(self, name):
        assert self.get_text_of_element(self.title_page) == name, "Name of title not correct"