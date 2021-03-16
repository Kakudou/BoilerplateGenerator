Feature: Create a entity.

    Scenario: Create a entity.
        Given I have a <entity_name>, <entity_domain>, <attributes> and a <project>.
        When I execute CreateEntity.
        Then I have the desired Entity created.
