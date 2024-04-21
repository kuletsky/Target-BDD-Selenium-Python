from pages.base_page import Page
from selenium.webdriver.common.by import By


class SideNavigation(Page):
    SIDE_SIGN_IN = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")

    def side_navigation_sign_in_click(self):
        self.wait_until_clickable_click(*self.SIDE_SIGN_IN)
