from selenium.webdriver.common.by import By
from behave import then, when


VERIFY_ITEM = (By.CSS_SELECTOR, "[class*='styles__CartSummarySpan-sc-odscpb-3']")


# # HW_7
# @when('Open Target Cart page')
# def open_target_cart_page(context):
#     # context.driver.get('https://www.target.com/cart')
#     context.app.main_page.open_main()

@when('Open Target Cart page')
def open_target_cart_page(context):
    context.app.cart_page.open_target_cart_page()


# HW_6
# Verify cart is empty
@then('Verify cart is empty')
def verify_cart_is_empty(context):
    context.app.cart_page.verify_cart_is_empty()


# Verify item is in the cart
@then('Verify item is in the cart')
def verify_item_is_in_the_cart(context):
    context.app.cart_page.verify_item_is_in_the_cart()
    # expected_result = 'item'
    # actual_result = context.driver.find_element(*VERIFY_ITEM).text
    # assert expected_result in actual_result, f"Error! {actual_result}"
