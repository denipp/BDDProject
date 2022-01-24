

Feature: Check App Center Page

  Scenario: See category add-ons in homepage
    Given Open App Center homepage
    When User in homepage
    Then verify have add-ons in homepage
#
  Scenario: User click contact us
    When in App Center homepage click contact us
    Then verify if user in contact us page


