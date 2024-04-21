from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search_results(self, expected_item):
        # actual_text = self.find_element(*self.SEARCH_RESULT_HEADER).text
        # assert expected_item in actual_text, f'Error! Text "{expected_item}" not in actual text "{actual_text}"'
        self.verify_partial_text(expected_item, *self.SEARCH_RESULT_HEADER)