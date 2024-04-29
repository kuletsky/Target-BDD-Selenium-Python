# Created by kuletsky at 08.04.2024
Feature: Tests for help page

  Scenario: Verify Help page
    Given Open Target Help page
    Then Verify header "Help" is displayed
    And Verify search Help is displayed
    And Verify search BTN is displayed
    And Verify Grid has 7 links
    And Verify Another Grid has 2 links
    And Verify header "Browse" is displayed

  Scenario: User can select Help topic
    Given Open Help page for Returns
    Then Verify Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify Current promotions page opened