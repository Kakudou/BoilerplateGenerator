Feature: Delete a usecase.

    Scenario: Delete a Usecase.
        Given I have a <usecase> already created.
        When I use DeleteUsecase with <usecase_name>.
        Then The <usecase> was removed.

