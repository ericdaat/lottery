# Lottery Drawing

A lottery drawing application that randomly draws numbers from 1 to 99, and displays them on a table.

## Install

Create a virtual environment and install the requirements.

``` bash
source venv/bin/activate
pip install -r requirements.txt
```

## Run

Init the database and run the application.

``` bash
export FLASK_APP="application.app"
export FLASK_DEBUG=True
export DATABASE_URL=sqlite:///../db.sqlite3
flask init-db
flask run
```
