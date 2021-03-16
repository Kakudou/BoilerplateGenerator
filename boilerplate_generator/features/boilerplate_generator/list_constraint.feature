Feature: List all constraint already created.

    Scenario: List all constraint.
        Given I have 3 <constraint> already created.
        When I use ListConstraint.
        Then I have a list with the 3 <constraint_name>.
