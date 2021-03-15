Feature: Get and update a feature.

    Scenario: Update a Feature.
        Given i have a <feature> already created.
        When i use UpdateFeature with <feature_name>.
        Then i see the updated information of my <feature>.

