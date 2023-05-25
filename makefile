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

.PHONY: clean venv requirements

clean:
	@echo -e $(bold)Clean up virtualenv and cache directories$(sgr0)
	rm -rf $(VENV) *.egg-info

venv: clean
	@echo -e $(bold)Create a new virtualenv$(sgr0)
	python3 -m venv $(VENV)
	$(pip) install --upgrade pip pip-tools

requirements:
	@echo -e $(bold)Update requirements.txt file$(sgr0)
	$(python) -m piptools compile --upgrade --resolver backtracking -o requirements.txt \
			  --extra dev --extra test pyproject.toml


# Development environment
.PHONY: bootstrap develop bootstrap-django serve

bootstrap: venv develop

develop:
	@echo -e $(bold)Install requirements and main package$(sgr0)
	$(python) -m pip install -r requirements.txt
	$(python) -m pip install --editable .

bootstrap-django:
	@echo -e $(bold)Initialize Django db and admin superuser$(sgr0)
	rm -f db.sqlite3
	$(django) migrate
	$(django) createsuperuser --email=info@conoscerelinux.org

secret_key:
	@$(python) scripts/generate_secret_key.py

serve:
	@echo -e $(bold)Launch Django development server$(sgr0)
	DEBUG=True $(django) runserver $(HOST):$(PORT)
	

# Database Management
.PHONY: migrate migrations

migrate:
	$(django) migrate

migrations:
	$(django) makemigrations

