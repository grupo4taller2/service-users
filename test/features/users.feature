Feature: Users

    Scenario: Create first user
        Given There are 0 users
        When I create the user "mateocalvo"
        Then The user "mateocalvo" exists in the platform
