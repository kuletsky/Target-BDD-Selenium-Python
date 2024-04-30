from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class HelpPage(Page):
    # HEADER_HELP = (By.XPATH, "[class='custom-h2']")
    # HEADER_RETURNS = (By.XPATH, '//h1[text()=" Returns"]')
    # HEADER_PROMOTIONS = (By.XPATH, '//h1[text()=" Target GiftCard balance"]')
    HEADER = (By.XPATH, '//*[text()=" {HEADER_STR}"]')
    TOPIC_SELECTION = (By.CSS_SELECTOR, 'select[id*="ViewHelpTopics"]')

    def _get_locator(self, text):
        # HEADER = (By.XPATH, '//h1[text()=" {HEADER_STR}"]')
        return [self.HEADER[0], self.HEADER[1].replace('{HEADER_STR}', text)]

    def open_help_returns(self):
        self.open('https://help.target.com/help/subcategoryarticle?childcat=Returns&parentcat=Returns+%26+Exchanges&searchQuery=search+help')

    def select_topic(self, option):
        topic_dd = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topic_dd)
        select.select_by_value(option)

    def verify_header(self, header):
        locator = self._get_locator(header)
        self.wait_until_visible(*locator)
