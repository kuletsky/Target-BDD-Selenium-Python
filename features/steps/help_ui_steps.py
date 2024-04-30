from selenium.webdriver.common.by import By
from behave import given, then, when


HEADER_HELP = (By.CSS_SELECTOR, "[class='custom-h2']")
SEARCH_HELP = (By.CSS_SELECTOR, "[class='search-input']")
SEARCH_BTN = (By.CSS_SELECTOR, "[class='btn-sm search-btn']")
GRID_LINKS = (By.CSS_SELECTOR, "[class='grid_6']")
GRID_OTHER_LINKS = (By.CSS_SELECTOR, "[class*='grid_4']")
HEADER_BROWSE = (By.XPATH, "//h2[contains(text(), 'Browse')]")


# Open Target Help page
@given('Open Target Help page')
def open_help(context):
    context.driver.get("https://help.target.com/help")


# Verify header "Help" is displayed
@then('Verify header "Help" is displayed')
def verify_help(context):
    context.driver.find_element(*HEADER_HELP)


# Verify search Help is displayed
@then('Verify search Help is displayed')
def verify_search_help(context):
    context.driver.find_element(*SEARCH_HELP)


# Verify search BTN is displayed
@then('Verify search BTN is displayed')
def verify_search_btn(context):
    context.driver.find_element(*SEARCH_BTN)


# Verify Grid has correct amount links
@then('Verify Grid has {expected_amount} links')
def verify_grid_has_expected_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*GRID_LINKS)
    assert len(links) == expected_amount, f"Expected {expected_amount} but got {len(links)}"


# Verify Another Grid has correct amount links
@then('Verify another Grid has {expected_amount} links')
def verify_another_grid_has_expected_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*GRID_OTHER_LINKS)
    assert len(links) == expected_amount, f"Expected {expected_amount} but got {len(links)}"


# Verify header "Browse" is displayed
@then('Verify header "Browse" is displayed')
def verify_browse_is_displayed(context):
    context.driver.find_element(*HEADER_BROWSE)


@given('Open Help page for Returns')
def open_help_returns(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {option}')
def select_topic(context, option):
    context.app.help_page.select_topic(option)


@then('Verify {header} page opened')
def verify_returns_opened(context, header):
    context.app.help_page.verify_header(header)