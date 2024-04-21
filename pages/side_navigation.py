from pages.base_page import Page
from selenium.webdriver.common.by import By


class SideNavigation(Page):
    SIDE_SIGN_IN = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")

    def side_sign_in_click(self, *locator):
        self.wait_until_clickable_click(*self.SIDE_SIGN_IN)


# Side menu Sign In click
# @when('Side menu SignIn click')
# def click_side_menu(context):
#     context.driver.find_element(*SIDE_SIGN_IN).click()
#     sleep(6)