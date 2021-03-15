Feature: Delete a feature.

    Scenario: Delete a Feature.
        Given I have a <feature> already created.
        When I use DeleteFeature with <feature_name>.
        Then The <feature> was removed.

