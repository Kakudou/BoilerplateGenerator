Feature: Get and update a usecase.

    Scenario: Update a Usecase.
        Given i have a <usecase> already created.
        When i use UpdateUsecase with <usecase_name>.
        Then i see the updated information of my <usecase>.

