@mobile
Feature: Mobile App Testing on SwagLabs App using Appium

  @mobile
  Scenario: Perform actions on the SwagLabs mobile app
    Given I have the SwagLabs mobile app open
    When I interact with the mobile app
    Then I should see the main page of the app
