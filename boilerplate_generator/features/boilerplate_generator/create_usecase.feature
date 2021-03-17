Feature: Create a usecase.

    Scenario: Create a usecase.
        Given I have a <usecase> with <name>, <description>, <type_>, <input_atts>, <output_attrs>, a <entity> and a <project>.
        When I execute CreateUsecase.
        Then I have the desired Usecase created.
