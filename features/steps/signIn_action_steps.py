from selenium.webdriver.common.by import By
from behave import when, then, given
from time import sleep

MAIN_SIGNIN = (By.XPATH, "//span[text()='Sign in']")


# Open sign in page
@given('Open sign in page')
def open_sign_in(context):
    context.app.sign_in_page.open_sign_in_page()


# Store original window
@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()


# Click on Target terms and conditions link
@when('Click on Target terms and conditions link')
def click_on_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_tm_link()


# Switch to the newly opened window
@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.app.sign_in_page.switch_to_new_window()


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


# Verify Terms and Conditions page is opened
@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.sign_in_page.verify_tm_opened()


# Verify User can close new window and switch back to original
@then('Verify User can close new window and switch back to original')
def verify_user_can_close_window_and_switch(context):
    context.app.sign_in_page.close()
    context.app.sign_in_page.switch_to_window_by_id(context.original_window)
