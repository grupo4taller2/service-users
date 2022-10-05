Feature: Drivers

    Scenario: Create first driver
        Given There are 0 drivers
        When I create a driver with username "mateocalvo"
        Then The driver "mateocalvo" exists in the platform
