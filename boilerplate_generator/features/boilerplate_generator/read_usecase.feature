Feature: Get and show the usecase informations.

    Scenario: Read a Usecase.
        Given i have a <usecase> already created.
        When i use ReadUsecase with <usecase_name>.
        Then i see the information of my <usecase>.

