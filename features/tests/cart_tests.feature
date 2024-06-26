Feature: Cart verify tests

# Verify cart is empty (HW_7)
  @smoke
  Scenario: Verify cart is empty
    Given Open Target main page
    When Click on cart
    Then Verify cart is empty


# Verify item is in the cart (HW 4, HW_7)
  @smoke
  Scenario: Verify item is in the cart
    Given Open Target main page
    When Search for soap
    And Click on BTN "Add to cart"
    And Confirm BTN "Add to cart"
    And Open Target Cart page
    Then Verify item is in the cart
