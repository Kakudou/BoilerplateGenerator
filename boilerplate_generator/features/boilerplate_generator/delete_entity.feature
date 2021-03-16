Feature: Delete a entity.

    Scenario: Delete a Entity.
        Given I have a <entity> already created.
        When I use DeleteEntity with <entity_name>.
        Then The <entity> was removed.

