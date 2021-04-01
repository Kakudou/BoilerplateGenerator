Feature: Generate a entity.

    Scenario: Generate a entity.
        Given I have a <entity>.
        When I execute GenerateEntity.
        Then I have the desired Entity and test generated.
