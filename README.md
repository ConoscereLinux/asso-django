# asso-django
An open source Django Framework to manage Events, Member and basic Accounting for an Italian Association

## Installation instructions
To install enviroment, db and migrations
```shell
# If you use an OS with make installed (usually linux)
$ make bookstrap
$ make bootstrap-django

# If you want to launch single commands (require python3 installed)
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv)$ pip install --upgrade pip
(.venv)$ pip install --upgrade isort black pytest  # development requirements
(.venv)$ pip install --upgrade -r requirements.txt # project requirements
```

## Run server
```shell
# using make
$ make serve

# using command line
$ source .venv/bin/activate
(.venv)$ python manage.py runserver
```