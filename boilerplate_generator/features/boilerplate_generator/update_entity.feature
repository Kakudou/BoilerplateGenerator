Feature: Get and update a entity.

    Scenario: Update a Entity.
        Given i have a <entity> already created.
        When i use UpdateEntity with <entity_name>.
        Then i see the updated information of my <entity>.

