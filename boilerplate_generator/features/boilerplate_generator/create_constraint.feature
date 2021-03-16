Feature: Create a constraint.

    Scenario: Create a constraint.
        Given I have a <constraint> with <scenario>, <given>, <when>, <then> and a <project>.
        When I execute CreateConstraint.
        Then I have the desired Constraint created.
