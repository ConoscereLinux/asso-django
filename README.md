# asso-django
An open source Django Framework to manage Events, Member and basic Accounting for an Italian Association

## Installation instructions
To install environment, db and migrations
```shell
# If you use an OS with make installed (usually linux)
$ make bookstrap
$ make bootstrap-django

# If you want to launch single commands (require python3 installed)
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv)$ pip install --upgrade pip
(.venv)$ pip install --upgrade -r requirements.txt # project requirements

(.venv)$ rm -f db.sqlite3  # If you want to reset db
(.venv)$ python asso/manage.py migrate
(.venv)$ python asso/manage.py createsuperuser --username=admin
```

## Run server
```shell
# using make
$ make serve

# using command line
$ source .venv/bin/activate
(.venv)$ python asso/manage.py runserver
```