from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


# HW_6
class SignInPage(Page):
    SIGNIN = (By.XPATH, "//span[text()='Sign into your Target account']")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login")
    TM_link = (By.XPATH, '//a[text()="Target terms and conditions"]')

    def open_sign_in_page(self):
        self.open('https://www.target.com/account')

    def verify_sign_in_page_is_open(self):
        self.wait_until_visible(*self.SIGNIN)
        self.verify_text('Sign into your Target account', *self.SIGNIN)

    def fill_in(self, username, password):
        self.input_text(username, *self.USERNAME)
        self.input_text(password, *self.PASSWORD)

    def click_sign_in(self):
        self.wait_until_clickable_click(*self.LOGIN)
        # sleep(10)

    def click_tm_link(self):
        self.click(*self.TM_link)

    def verify_sign_in_page_is_successful(self):
        self.wait_until_disappears(*self.SIGNIN)

    def verify_tm_opened(self):
        self.verify_partial_url('terms-conditions')
