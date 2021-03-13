Feature: Get and update a project.

    Scenario: Update a Project.
        Given i have a <project> already created.
        When i use UpdateProject with <project_name>.
        Then i see the updated information of my <project>.

