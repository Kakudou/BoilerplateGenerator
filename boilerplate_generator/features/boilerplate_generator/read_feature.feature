Feature: Get and show the feature informations.

    Scenario: Read a Feature.
        Given i have a <feature> already created.
        When i use ReadFeature with <feature_name>.
        Then i see the information of my <feature>.

