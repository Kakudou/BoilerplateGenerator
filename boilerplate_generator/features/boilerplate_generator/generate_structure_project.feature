Feature: Generate structure of the project

    Scenario: Generate the project structure.
        Given I have a <project>.
        When I execute GenerateStructure with <project_name>.
        Then I have the structure of the project generated.

