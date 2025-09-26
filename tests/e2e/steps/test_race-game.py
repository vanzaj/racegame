from playwright.sync_api import Page, expect
from pytest_bdd import (
    given,
    when,
    then,
    scenarios,
)


scenarios("../race-game.feature")


@given("I am admin")
def _():
    pass


@when("I create a new game with ID 123")
def _():
    pass


@then("URL for game 123 should be accessible")
def _():
    pass


@given("The game with ID 123 is running")
def test_game_running(page: Page):
    rsp = page.goto("/game/123")
    assert rsp.status == 200


@when("I join the game 123")
def test_join_game(page: Page):
    page.goto("/game/123/p/1")
    expect(page).to_have_title("Race Game: 123")
    expect(page.locator("id=player_name")).to_have_text("Name: Player-1")


@then('I should see that my name is "Player 1"')
def _():
    pass


@then("My current position is 0")
def _():
    pass


@then("My current damage is 0")
def _():
    pass
