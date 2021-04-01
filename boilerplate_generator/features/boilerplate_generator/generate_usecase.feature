Feature: Generate a usecase.

    Scenario: Generate a usecase.
        Given I have a <usecase>.
        When I execute GenerateUsecase.
        Then I have the desired Usecase and test generated.
