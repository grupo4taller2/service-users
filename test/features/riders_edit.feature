Feature: Riders edit

    Scenario: Edit first name
        Given I choose "mateocalvo" for username
            And I choose "wrong first name" for first name
            And I choose "lname" for last name
            And I choose "mateo@mateo.com" for email
            And I choose "1236" for phone number
            And I choose -34.0 as preferred location latitude
            And I choose -34.0 as preferred location longitude
            And I choose "some name" as preferred location name
            And I register as a rider
        When I change the first name of rider with email "mateo@mateo.com" to "mateo"
        Then The first name of rider with email "mateo@mateo.com" is updated to "mateo"
