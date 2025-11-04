PY?=python
PIP?=pip

.PHONY: setup test lint run clean

setup:
	$(PY) -m pip install --upgrade pip
	@if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi
	$(PIP) install -U ruff pytest

test:
	pytest -q

lint:
	ruff check .

run:
	@echo "Define a run target for this project (e.g., python -m app)"

clean:
	rm -rf .pytest_cache __pycache__ dist build .ruff_cache

