from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import then, when
from time import sleep


# SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
# BTN_ADD_TO_CART = (By.CSS_SELECTOR, "[id*='addToCartButton']")
# BTN_CONFIRM_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
# VIEW_CART_BTN = (By.CSS_SELECTOR, "a[href='/cart']")


# HW_5
ITEM_PICTURES = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage/primary'] img")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")
ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='product-title']")
ALL_PRODUCTS = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardVariantDefault']")


# Verify search results are shown for expected_item
@then("Verify search results are shown for {expected_item}")
def verify_search_results(context, expected_item):
    context.app.search_results_page.verify_search_results(expected_item)


# Verify that URL has coffee
@then("Verify that URL has {partial_url}")
def verify_search_page_url(context, partial_url):
    context.app.search_results_page.verify_partial_url(partial_url)


# Click on BTN "Add to cart"
@when('Click on BTN "Add to cart"')
def click_on_cart_product(context):
    context.app.search_results_page.click_btn_add_to_cart()


# Confirm BTN "Add to cart"
@when('Confirm BTN "Add to cart"')
def click_on_confirm_button(context):
    context.app.search_results_page.click_confirm_btn_add_to_cart()


# HW_5
# ======================================================================
# Verify that every product on Target search results page has:
# a product name
# a product image

# version 1
@then('Verify that every product has Name')
def verify_that_product_has_name(context):
    sleep(8)
    item_names = context.driver.find_elements(*ITEM_NAMES)

    for item in item_names:
        assert item.text, f'Error! Item does not have Name'


@then('Verify that every product has Image')
def verify_that_product_has_image(context):
    item_pictures = context.driver.find_elements(*ITEM_PICTURES)

    for picture in item_pictures:
        # print(picture.get_attribute('src'))
        assert picture.get_attribute('src'), f'Error! Picture not found for Item "{picture.get_attribute('alt')}'


# version 2
@then('Verify that every product has Name and Image')
def verify_that_product_has_name_and_title(context):
    # sleep(8)
    all_products = context.driver.find_elements(*ALL_PRODUCTS)
    for product in all_products:

        title = product.find_element(*ITEM_NAMES).text
        print(title)
        assert title, f'Error! Item does not have Name'
        product.find_element(*PRODUCT_IMG)
