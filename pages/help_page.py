from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class HelpPage(Page):
    HEADER_RETURNS = (By.XPATH, '//h1[text()=" Returns"]')
    HEADER_PROMOTIONS = (By.XPATH, '//h1[text()=" Current promotions"]')
    TOPIC_SELECTION = (By.CSS_SELECTOR, 'select[id*="ViewHelpTopics"]')

    def open_help_returns(self):
        self.open('https://help.target.com/help/subcategoryarticle?childcat=Returns&parentcat=Returns+%26+Exchanges&searchQuery=search+help')

    def select_topic(self):
        topic_dd = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topic_dd)
        select.select_by_value('Promotions & Coupons')

    def verify_promotions_header(self):
        self.wait_until_visible(*self.HEADER_PROMOTIONS)

    def verify_returns_header(self):
        self.wait_until_visible(*self.HEADER_RETURNS)
