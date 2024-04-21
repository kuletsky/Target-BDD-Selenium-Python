from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


SIGNIN = (By.XPATH, "//span[text()='Sign into your Target account']")
MAIN_SIGNIN = (By.XPATH, "//span[text()='Sign in']")
MENU_SIGNIN = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")


# Main page SignIn click
@when('Main page SignIn click')
def click_sign_in(context):
    context.app.header.wait_until_clickable_click(*MAIN_SIGNIN)


# Side menu Sign In click
@when('Side menu SignIn click')
def click_side_menu(context):
    context.app.side_navigation.side_navigation_sign_in_click()


@then('Verify SignIn page is open')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in_page_is_open()
