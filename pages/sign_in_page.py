from pages.base_page import Page
from selenium.webdriver.common.by import By


# HW_6
class SignInPage(Page):
    SIGNIN = (By.XPATH, "//span[text()='Sign into your Target account']")

    def verify_sign_in_page_is_open(self):
        self.wait_until_visible(*self.SIGNIN)
        self.verify_text('Sign into your Target account', *self.SIGNIN)
