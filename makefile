VENV=.venv
SHELL=/bin/bash

python=$(VENV)/bin/python3
pip=$(VENV)/bin/python -m pip
django=$(python) manage.py

# Utility scripts to prettify echo outputs
bold := '\033[1m'
sgr0 := '\033[0m'

HOST=127.0.0.1
PORT=8000

.PHONY: bootstrap clean develop requirements venv

bootstrap: venv develop

clean:
	@echo -e $(bold)Clean up virtualenv and cache directories$(sgr0)
	@rm -rf $(VENV) *.egg-info .pytest_cache

venv: clean
	@echo -e $(bold)Create a new virtualenv$(sgr0)
	@python3 -m venv $(VENV)
	@$(pip) install --upgrade pip pip-tools

develop:
	@echo -e $(bold)Install and update development requirements$(sgr0)
	$(python) -m pip install -r requirements.txt

production:
	@echo -e $(bold)Install and update production requirements$(sgr0)
	@$(pip) install -r requirements.txt

requirements:
	@echo -e $(bold)Update requirements with pip-tools$(sgr0)
	$(VENV)/bin/pip-compile -vU \
		--resolver backtracking \
		--output-file requirements.txt \
		--extra dev --extra test \
		pyproject.toml


# Django development commands
.PHONY: serve shell test

serve:
	@echo -e $(bold)Launch Django development server$(sgr0)
	@$(django) runserver $(HOST):$(PORT)

shell:
	@$(django) shell

test:
	@$(python) -m pytest


# Django DataBase commands
.PHONY: migrate migrations secret_key superuser

migrate:
	@echo -e $(bold)Apply migration to database$(sgr0)
	@$(django) migrate

migrations:
	@echo -e $(bold)Create migration files$(sgr0)
	@$(django) makemigrations

secret_key:
	@$(python) scripts/generate_secret_key.py

superuser:
	@echo -e $(bold)Creating superuser account 'admin'$(sgr0)
	@$(django) createsuperuser --email=info@conoscerelinux.org

demo:
	@$(django) loaddata member/demo
	@$(django) loaddata academy/demo


# Database commands
db-bootstrap: db-flush migrate db-default superuser

db-default:
	@$(django) loaddata website/default
	@$(django) loaddata member/default

db-flush:
	@echo -e $(bold)Deleting all data from database$(sgr0)
	@$(django) flush

# TailwindCSS
.PHONY: watch
watch: 
	npx tailwindcss -i ./tailwind/main.tw.css -o ./asso/static/main.tw.css --watch


# Internationalization
.PHONY: messages translations

messages:
	@$(django) makemessages -l it

translations: messages
	@$(django) compilemessages