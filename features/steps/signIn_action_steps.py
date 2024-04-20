from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


SIGNIN = (By.XPATH, "//span[text()='Sign into your Target account']")
MAIN_SIGNIN = (By.XPATH, "//span[text()='Sign in']")
MENU_SIGNIN = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")


# Main page SignIn click
@when('Main page SignIn click')
def click_sign_in(context):
    context.driver.find_element(*MAIN_SIGNIN).click()


# Side menu Sign In click
@when('Side menu SignIn click')
def click_side_menu(context):
    context.driver.find_element(*MENU_SIGNIN).click()
    sleep(6)


@then('Verify SignIn form is open')
def verify_sign_in(context):
    # Verification
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(*SIGNIN).text
    assert actual_result in expected_result, f"Error! {actual_result}"
    print("\nVerify Sign In is successful!")
