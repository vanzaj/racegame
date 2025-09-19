Feature: Emerson's Race Game

  Scenario: Single player
    Given The game with ID 123 is running
    When I join the game 123
    Then There should be 1 car with named "Player 1"
    And The car named "Player 1" should have 0 damage
