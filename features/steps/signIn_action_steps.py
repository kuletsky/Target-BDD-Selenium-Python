from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

MAIN_SIGNIN = (By.XPATH, "//span[text()='Sign in']")


# Main page SignIn click
@when('Main page SignIn click')
def click_sign_in(context):
    context.app.header.wait_until_clickable_click(*MAIN_SIGNIN)


# Side menu Sign In click
@when('Side menu SignIn click')
def click_side_menu(context):
    context.app.side_navigation.side_navigation_sign_in_click()


@when('Fill in the {username} and {password} fields')
def fill_in_login_and_password(context, username, password):
    context.app.sign_in_page.fill_in(username, password)


@when('Click the Sign In')
def click_sign_in(context):
    context.app.sign_in_page.click_sign_in()


@then('Verify SignIn page is open')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in_page_is_open()


@then('Verify SignIn is successful')
def verify_sign_in_success(context):
    context.app.sign_in_page.verify_sign_in_page_is_successful()