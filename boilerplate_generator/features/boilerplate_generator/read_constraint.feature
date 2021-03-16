Feature: Get and show the constraint informations.

    Scenario: Read a Constraint.
        Given i have a <constraint> already created.
        When i use ReadConstraint with <constraint_name>.
        Then i see the information of my <constraint>.

