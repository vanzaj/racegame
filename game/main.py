from fasthtml.common import *

app = FastHTML()


@app.get("/")
def index():
    page = Html(
        Head(Title("Race Game")),
        Body((H1("Welcome to the Race Game!"), A("Start new game", href="/game"))),
    )
    return page


@app.get("/game")
def game():
    page = Html(
        Head(Title("New Race Game")),
        Body(Div(H1("Let's race!"))),
    )
    return page


serve()
