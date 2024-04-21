from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    BTN_CONFIRM_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")

    def click_btn_add_to_cart(self):
        self.wait_until_clickable_click(*self.BTN_ADD_TO_CART)

    def click_confirm_btn_add_to_cart(self):
        self.wait_until_clickable_click(*self.BTN_CONFIRM_ADD_TO_CART)

    def verify_search_results(self, expected_item):
        self.verify_partial_text(expected_item, *self.SEARCH_RESULT_HEADER)
