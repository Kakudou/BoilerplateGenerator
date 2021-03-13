Feature: Delete a project.

    Scenario: Delete a Project.
        Given I have a <project> already created.
        When I use DeleteProject with <project_name>.
        Then The <project> was removed.

