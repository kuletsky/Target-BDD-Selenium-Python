Feature: SignIn verify tests

  Scenario: Verify SignIn is shown
    Given Open Target main page
    When Main page SignIn click
    And Side menu SignIn click
    Then Verify SignIn page is open


  # HW_7 Verify successful login with valid credentials
  @smoke
  Scenario: Verify successful login with valid credentials
    Given Open Target main page
    When Main page SignIn click
    And Side menu SignIn click
    And Fill in the audids@boranora.com and qwertyuiop[] fields
    And Click the Sign In
    Then Verify SignIn is successful


# HW_8 User can open and close Terms and Conditions from the class
  Scenario: User can open and close Terms and Conditions from the class
    Given Open sign in page
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And Verify User can close new window and switch back to original

  # HW_9 Verify unsuccessful login with invalid credentials
  Scenario: Verify unsuccessful login with invalid credentials
    Given Open Target main page
    When Main page SignIn click
    And Side menu SignIn click
    And Fill in the audids@boranora.com and qwf121132re fields
    And Click the Sign In
    Then Verify SignIn is unsuccessful