from selenium.webdriver.common.by import By

from pages.base_page import Page


class TargetAppPage(Page):
    PP_Link = (By.XPATH, '//a[text()="Privacy policy"]')

    def open_target_app(self):
        self.open('https://www.target.com/c/target-app')
