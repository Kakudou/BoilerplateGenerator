Feature: List all entity already created.

    Scenario: List all entity.
        Given I have 3 <entity> already created.
        When I use ListEntity.
        Then I have a list with the 3 <entity_name>.
