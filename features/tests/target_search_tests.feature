Feature: Search verify tests

  Scenario:
    Given Open Target main page
    When Search for coffee
    Then Verify search results are shown for coffee


  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <item>
    Then Verify search results are shown for <expected_item>
    Examples:
    |item     |expected_item  |
    |cup      |cup            |
    |key      |key            |
    |coffee   |coffee         |
    |flower   |flower         |


    #HW_5
  Scenario: Every product has Name and Image
    Given Open Target main page
    When Search for TV
    Then Verify that every product has Name
    And Verify that every product has Image

  # Version 2
  Scenario: Every product has Name and Image
    Given Open Target main page
    When Search for TV
    Then Verify that every product has Name and Image
