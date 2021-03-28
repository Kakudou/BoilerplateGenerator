Constraint: Generate a constraint.

    Scenario: Generate a constraint.
        Given I have a <constraint>.
        When I execute GenerateConstraint.
        Then I have the desired Constraint and test generated.
