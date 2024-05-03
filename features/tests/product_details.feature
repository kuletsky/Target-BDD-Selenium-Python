# Created by kuletsky at 16.04.2024
Feature: Test for product page
  # Enter feature description here

  @smoke
  Scenario: User can select colors
    Given Open Target product A-91511634 page
    Then Verify user can click through colors
