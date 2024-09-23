install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

format:
	black *.py

lint:
	ruff check test_*.py && ruff check *.py
	ruff check *.ipynb

test:
	python -m pytest -vv --nbval --cov=lib *.py test_*.py *.ipynb


all: install lint test format
