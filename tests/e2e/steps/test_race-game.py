from playwright.sync_api import Page, expect
from pytest_bdd import (
    given,
    when,
    then,
    scenarios,
)


scenarios("../race-game.feature")


@given("The game is running")
def _():
    pass


@when("I join the game")
def _(page: Page):
    page.goto("http://localhost:5001/game")
    expect(page).to_have_title("New Race Game")



@then('The car named "Player 1" should have 0 damage')
def _():
    pass


@then('There should be 1 car with named "Player 1"')
def _():
    pass
