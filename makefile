VENV=.venv
SHELL=/bin/bash

python=$(VENV)/bin/python3
pip=$(VENV)/bin/pip3
django=$(python) manage.py

HOST=127.0.0.1
PORT=8000

# Utility scripts to prettify echo outputs
bold := '\033[1m'
sgr0 := '\033[0m'


.PHONY: bootstrap
bootstrap: venv develop


.PHONY: clean
clean:
	@echo -e $(bold)Clean up old virtualenv and cache$(sgr0)
	rm -rf $(VENV)


.PHONY: venv
venv: clean
	@echo -e $(bold)Create virtualenv$(sgr0)
	python3 -m venv $(VENV)
	$(pip) install --upgrade pip


.PHONY: develop
develop:
	@echo -e $(bold)Install and update requirements$(sgr0)
	$(pip) install --upgrade isort black pytest
	$(pip) install --upgrade -r requirements.txt


.PHONY: bootstrap-django
bootstrap-django:
	rm db.sqlite3
	$(django) migrate
	$(django) createsuperuser --username=admin --email=info@conoscerelinux.org
	$(django) runscript load_data
	

.PHONY: import migrate serve

import:
	$(django) runscript load_data

migrate:
	$(django) migrate

serve:
	$(django) runserver $(HOST):$(PORT)
