Feature: Cart verify tests

  Scenario: Verify cart is empty
    Given Open Target main page
    When Click on cart
    Then Verify cart is empty


# Verify item is in the cart (HW 4)
  Scenario: Verify item is in the cart
    Given Open Target main page
    When Search for apple
    And Click on BTN "Add to cart"
    And Confirm BTN "Add to cart"
    And Open cart page
    Then Verify item is in the cart
