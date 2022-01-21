

Feature: Check App Center Page
  Background:
    Given Launch Chrome Browser
    Then Open App Center homepage

  Scenario: See category add-ons in homepage
    Then verify have add-ons in homepage

  Scenario: User click contact us
    When in App Center homepage click contact us
    Then verify if user in contact us page


