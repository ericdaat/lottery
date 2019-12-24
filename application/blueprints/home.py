import logging

import flask

from application.utils import get_issued_numbers, draw_number

bp = flask.Blueprint("home", __name__)


@bp.route("/")
def index():
    numbers = list(range(1, 100))
    issued_numbers = get_issued_numbers()

    return flask.render_template(
        "home/index.html",
        numbers=numbers,
        issued_numbers=issued_numbers
    )
