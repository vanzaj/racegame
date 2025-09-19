start:
	uv run game/main.py

e2etest:
	uv run pytest -v --gherkin-terminal-reporter
