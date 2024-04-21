from pages.base_page import Page
from selenium.webdriver.common.by import By


# HW_6
class CartPage(Page):
    EMPTY_CART_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_cart_is_empty(self):
        self.verify_text('Your cart is empty', *self.EMPTY_CART_MSG)
        # self.verify_partial_text('cart is empty', *self.EMPTY_CART_MSG)
