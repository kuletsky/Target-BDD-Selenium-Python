from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, '[data-test*="SearchButton"]')

    def search_product(self):
        self.input_text('tea', *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)