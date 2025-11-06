from fasthtml.common import *

app = FastHTML()


@app.get("/")
def index():
    body = Body(H1("Welcome to the Race Game!"), A("Start new game", href="/game"))
    page = Titled("Race Game", body)
    return page


@app.get("/game/{id}/")
def game_page(id: int = 0):
    if id == 0:
        body = Body(H1("No games started yet"))
        page = Titled(f"Race Game", body)
    else:
        body = Body(H1("Let's race!"))
        page = Titled(f"Race Game: {id}", body)
    return page


@app.get("/game/{id}/p/{player_id}")
def game_page_for_player(id: int = 0, player_id: int = 0):
    body = Body(
        H1("Let's race!", Div(P(f"Name: Player-{player_id}", id="player_name")))
    )
    page = Titled(f"Race Game: {id}", body)
    return page


serve()
