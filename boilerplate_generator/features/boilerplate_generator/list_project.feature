Feature: List all project already created.

    Scenario: List all project.
        Given I have 3 <project> already created.
        When I use ListProject.
        Then I have a list with the 3 <project_name>.
