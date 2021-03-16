Feature: Delete a constraint.

    Scenario: Delete a Constraint.
        Given I have a <constraint> already created.
        When I use DeleteConstraint with <constraint_name>.
        Then The <constraint> was removed.

