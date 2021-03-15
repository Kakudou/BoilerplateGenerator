Feature: List all feature already created.

    Scenario: List all feature.
        Given I have 3 <feature> already created.
        When I use ListFeature.
        Then I have a list with the 3 <feature_name>.
