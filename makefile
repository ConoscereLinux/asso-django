VENV=.venv
SHELL=/bin/bash

python=$(VENV)/bin/python3
pip=$(VENV)/bin/pip3
django=$(python) manage.py

# Utility scripts to prettify echo outputs
bold := '\033[1m'
sgr0 := '\033[0m'

HOST=127.0.0.1
PORT=8000

.PHONY: clean venv freeze

clean:
	@echo -e $(bold)Clean up old virtualenv and cache$(sgr0)
	rm -rf $(VENV) *.egg-info

venv: clean
	@echo -e $(bold)Create virtualenv$(sgr0)
	python3 -m venv $(VENV)
	$(pip) install --upgrade pip pip-tools

freeze:
	$(python) -m piptools compile --upgrade --resolver backtracking -o requirements.txt pyproject.toml
	$(python) -m piptools compile --upgrade --resolver backtracking -o requirements.dev.txt --extra dev --extra test pyproject.toml


# Development environment
.PHONY: bootstrap develop bootstrap-django serve

bootstrap: venv develop

develop:
	@echo -e $(bold)Install and update requirements$(sgr0)
	$(python) -m pip install -r requirements.dev.txt
	$(python) -m pip install --editable .

bootstrap-django:
	rm db.sqlite3
	$(django) migrate
	$(django) createsuperuser --username=admin --email=info@conoscerelinux.org

serve:
	DEBUG=True $(django) runserver $(HOST):$(PORT)
	

# Database Management
.PHONY: import migrate

import:
	$(django) runscript load_data

migrate:
	$(django) migrate

migrations:
	$(django) makemigrations

