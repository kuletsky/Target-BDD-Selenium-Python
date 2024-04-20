Feature: SignIn verify tests

  Scenario: Verify SignIn is shown
    Given Open Target main page
    When Main page SignIn click
    When Side menu SignIn click
    Then Verify SignIn form is open