Feature: Get and show the project informations.

    Scenario: Read a Project.
        Given i have a <project> already created.
        When i use ReadProject with <project_name>.
        Then i see the information of my <project>.

