Feature: Get and update a constraint.

    Scenario: Update a Constraint.
        Given i have a <constraint> already created.
        When i use UpdateConstraint with <constraint_name>.
        Then i see the updated information of my <constraint>.

