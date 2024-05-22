from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "[data-io-v='full'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class] [data-test='web\VariationComponent']:nth-of-type(2) [class='styles__StyledHeaderWrapperDiv-sc-tezx2e-1 jWgzho']")


@given('Open Target product {} page')
def open_product_details_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click through colors')
def verify_colors(context):

    expected_colors = ['dark khaki', 'black/gum', 'stone/grey', 'white/gum']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors:
        print(color)
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        selected_color = selected_color.split('\n')
        selected_color = selected_color[1]
        actual_colors.append(selected_color)
        # print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors}, did not match actual {actual_colors}'