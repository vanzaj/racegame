from fasthtml.common import *

app = FastHTML()


@app.get("/")
def index():
    page = Html(
        Head(Title("Race Game")),
        Body((H1("Welcome to the Race Game!"), A("Start new game", href="/game"))),
    )
    return page


@app.get("/game/{id}")
def game(id:str):
    page = Html(
        Head(Title(f"Race Game: {id}")),
        Body(Div(H1("Let's race!"))),
    )
    return page


serve()
