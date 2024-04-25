from selenium.webdriver.common.by import By

from pages.base_page import Page


class TargetAppPage(Page):
    PP_Link = (By.XPATH, '//a[text()="Privacy policy"]')

    def open_target_app(self):
        self.open('https://www.target.com/c/target-app')

    def click_pp_link(self):
        self.click(*self.PP_Link)

    def verify_pp_opened(self):
        self.verify_partial_url('target-privacy-policy')

