serve:
	uv run game/main.py

teste2e:
	uv run pytest -v --gherkin-terminal-reporter tests/e2e

testunit:
	uv run pytest -v tests/unit
