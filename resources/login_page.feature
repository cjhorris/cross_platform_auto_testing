Feature: Login Page Test Cases


  Scenario Outline: As a user, I would like to reach landing screen after login successfully with a valid credential.
    * LoginPage initialize platform "<platform>"
    Given LoginPage I enter username "username"
    And LoginPage I enter password "password"
    When LoginPage I press login button
    Then LoginPage I can login successfully
    Examples:
      | platform |
      | ios      |
      | android  |
      | web      |

  Scenario Outline: As a user, I would like to be prompt with error message if I enter password and username length greater than 8 and invalid credential entre.
    * LoginPage initialize platform "<platform>"
    Given LoginPage I enter username "invalid_username"
    And LoginPage I enter password "invalid_password"
    When LoginPage I press login button
    Then LoginPage I check error message "Login Failed"
    Examples:
      | platform |
      | ios      |
      | android  |
      | web      |

  Scenario Outline: As a user, I would like to see submit button disable if either one of the fields(username/password) is empty.
    * LoginPage initialize platform "<platform>"
    Given LoginPage I enter username "valid_username"
    Then LoginPage I can see submit button is disabled
    Examples:
      | platform |
      | ios      |
      | android  |
      | web      |