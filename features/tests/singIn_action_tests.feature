Feature: SignIn verify tests

  Scenario: Verify SignIn is shown
    Given Open Target main page
    When Main page SignIn click
    And Side menu SignIn click
    Then Verify SignIn page is open