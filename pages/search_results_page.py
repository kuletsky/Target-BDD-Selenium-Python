from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    BTN_CONFIRM_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
    FAVORITES_BTN = (By.CSS_SELECTOR, '[data-test="FavoritesButton"]')
    FAVORITES_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")

    def hover_fav_icon(self):
        fav_btn = self.find_element(*self.FAVORITES_BTN)

        actions = ActionChains(self.driver)
        actions.move_to_element(fav_btn)
        actions.perform()

    def verify_fav_tooltip(self):
        self.verify_text('Click to sign in and save', *self.FAVORITES_TOOLTIP_TXT)

    def click_btn_add_to_cart(self):
        self.wait_until_clickable_click(*self.BTN_ADD_TO_CART)

    def click_confirm_btn_add_to_cart(self):
        self.wait_until_clickable_click(*self.BTN_CONFIRM_ADD_TO_CART)

    def verify_search_results(self, expected_item):
        self.verify_partial_text(expected_item, *self.SEARCH_RESULT_HEADER)
