from fasthtml.common import *

app = FastHTML()


@app.get("/")
def index():
    page = Html(
        Head(Title("Race Game"), picolink),
        Body((H1("Welcome to the Race Game!"), A("Start new game", href="/game"))),
    )
    return page


@app.get("/game/{id}")
def game(id: int = 0):
    if id == 0:
        page = Html(
            Head(Title(f"Race Game")),
            Body(Div(H1("No games started yet"))),
        )
    else:
        page = Html(
            Head(Title(f"Race Game: {id}")),
            Body(Div(H1("Let's race!"))),
        )
    return page


serve()
