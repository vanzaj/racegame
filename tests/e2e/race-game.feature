Feature: Emerson's Race Game

  Scenario: Admin can start a new game
    Given I am admin
    When I create a new game with ID 123
    Then URL for game 123 should be accessible

  Scenario: Single player
    Given The game with ID 123 is running
    When I join the game 123
    Then There should be 1 car with named "Player 1"
    And The car named "Player 1" should have 0 damage
