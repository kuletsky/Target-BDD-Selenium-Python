Feature: SignIn verify tests

  Scenario: Verify SignIn is shown
    Given Open Target main page
    When Main page SignIn click
    And Side menu SignIn click
    Then Verify SignIn page is open


  # HW_7 Verify successful login with valid credentials
  Scenario: Verify successful login with valid credentials
    Given Open Target main page
    When Main page SignIn click
    And Side menu SignIn click
    And Fill in the audids@boranora.com and ********* fields
    And Click the Sign In
    Then Verify SignIn is successful