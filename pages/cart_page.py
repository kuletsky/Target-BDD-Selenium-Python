from pages.base_page import Page
from selenium.webdriver.common.by import By


# HW_6
class CartPage(Page):
    EMPTY_CART = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_cart_is_empty(self):
        expected_result = 'Your cart is empty'
        actual_result = self.find_element(*self.EMPTY_CART).text
        # print(actual_result)
        assert actual_result in expected_result, f"Error! {actual_result}"
        print("\nVerify cart is successful!")