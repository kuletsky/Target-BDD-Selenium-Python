from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


# HW_6
class CartPage(Page):
    EMPTY_CART_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    VERIFY_ITEM = (By.CSS_SELECTOR, "[class*='styles__CartSummarySpan-sc-odscpb-3']")

    def open_target_cart_page(self):
        self.driver.get("https://www.target.com/cart")

    def verify_cart_is_empty(self):
        self.verify_text('Your cart is empty', *self.EMPTY_CART_MSG)

    def verify_item_is_in_the_cart(self):

        self.verify_partial_text('item', *self.VERIFY_ITEM)
