Feature: Create the project.

    Scenario: Create a project.
        Given I have <project_name>, <project_path> and <project_types>.
        When i execute CreateProject.
        Then I have the desired project created.

