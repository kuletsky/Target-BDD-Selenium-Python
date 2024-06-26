Feature: Search verify tests

  @smoke
  Scenario: User can search for a coffe
    Given Open Target main page
    When Search for coffee
    Then Verify search results are shown for coffee
    And Verify that URL has coffee

  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <item>
    Then Verify search results are shown for <expected_item>
    And Verify that URL has <item>
    Examples:
    |item     |expected_item  |
    |cup      |cup            |
    |key      |key            |
    |coffee   |coffee         |
    |flower   |flower         |


  #HW_5
  @smoke
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

  # User can see favorites tootlip for search results
  Scenario: User can see favorites tootlip for search results
    Given Open Target main page
    When Search for pen
    And Hover favorites icon
    Then Favorites tooltip is shown