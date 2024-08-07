@accessibility
Feature: Accessibility of Login Page on SwagLabs using Axe-Core

  @accessibility
  Scenario: Check Accessibility for Login Page
    Given I am on the SwagLabs login page for accessibility testing
    When I run an accessibility scan on the login page
    Then I should not find any accessibility issues
