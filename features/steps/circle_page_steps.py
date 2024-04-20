from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CIRCLE_LINKS = (By.CSS_SELECTOR, "[data-component-id='WEB-397697'] [data-test='@web/slingshot-components/CellsComponent/Link']")


# Open Target Circle page
@given('Open Target Circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')


# Verify Circle page has correct amount links
@then("Verify circle page has {expected_amount} links")
def verify_header_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*CIRCLE_LINKS)
    assert len(links) == expected_amount, f"Expected {expected_amount} links but got {len(links)}"
