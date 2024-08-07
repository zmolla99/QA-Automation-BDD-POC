@security
Feature: Security Testing of Login Page on SwagLabs using ZAP

  @security
  Scenario: Security Scan for Login Page
    Given I am on the SwagLabs login page for security assessment
    When I execute a security scan with ZAP
    Then I should not discover any critical security vulnerabilities
