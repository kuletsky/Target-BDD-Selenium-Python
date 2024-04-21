from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Header(Page):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, '[data-test*="SearchButton"]')
    CART_ICON = (By.CSS_SELECTOR, "use[href*='Cart.svg#Cart']")

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_INPUT)
        self.wait_until_clickable_click(*self.SEARCH_BTN)
        sleep(8)

    def click_cart(self):
        self.wait_until_clickable_click(*self.CART_ICON)
