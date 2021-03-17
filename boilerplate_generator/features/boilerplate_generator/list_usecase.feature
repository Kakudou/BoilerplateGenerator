Feature: List all usecase already created.

    Scenario: List all usecase.
        Given I have 3 <usecase> already created.
        When I use ListUsecase.
        Then I have a list with the 3 <usecase_name>.
