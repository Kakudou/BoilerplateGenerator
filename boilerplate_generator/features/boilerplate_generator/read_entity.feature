Feature: Get and show the entity informations.

    Scenario: Read a Entity.
        Given i have a <entity> already created.
        When i use ReadEntity with <entity_name>.
        Then i see the information of my <entity>.

