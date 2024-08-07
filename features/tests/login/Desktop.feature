@desktop
Feature: Login to SwagLabs with Selenium

  @desktop
  Scenario: Successful Login
    Given I am ready to log into SwagLabs
    When I log in with valid credentials
    Then I should see the products page
