from playwright.sync_api import Page, expect
from pytest_bdd import (
    given,
    when,
    then,
    scenarios,
)


scenarios("../race-game.feature")


@given("The game with ID 123 is running")
def test_game_running(page: Page):
    rsp = page.goto('/game/123')
    assert rsp.status == 200


@when("I join the game 123")
def test_join_game(page: Page):
    page.goto("/game/123")
    expect(page).to_have_title("Race Game: 123")


@then('The car named "Player 1" should have 0 damage')
def _():
    pass


@then('There should be 1 car with named "Player 1"')
def _():
    pass
