Feature: Emerson's Race Game

  @ignore
  Scenario: Organizer can start a new game
    Given I am an organizer
    When I create a new game with ID 123
    Then URL for game 123 should be accessible

  @ignore
  Scenario: Single player joins a game
    Given The game with ID 123 is running
    When I join the game 123
    Then I should see that my name is "Player 1"
    And My current position is 0
    And My current damage is 0
