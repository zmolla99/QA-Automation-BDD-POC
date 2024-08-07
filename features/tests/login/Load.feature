@load
Feature: Load Testing of Login Page using Locust and Selenium

  @load
  Scenario: Load Test for Login Page
    Given I have set up for load testing the login page
    When I perform login actions using Selenium
    And I simulate concurrent user logins
    Then the login page should handle the simulated load without issues
