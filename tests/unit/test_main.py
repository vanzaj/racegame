from starlette.testclient import TestClient
from game.main import app

client = TestClient(app)


def test_index():
    r = client.get("/")
    assert r.status_code == 200
