import logging

import flask

bp = flask.Blueprint("home", __name__)


@bp.route("/")
def index():
    numbers = list(range(1, 100))
    issued_numbers = {3, 4, 10, 50, 88}

    return flask.render_template(
        "home/index.html",
        numbers=numbers,
        issued_numbers=issued_numbers
    )
