import logging

import flask

from application import utils

bp = flask.Blueprint("home", __name__)


@bp.route("/")
def index():
    numbers = list(range(1, 100))
    issued_numbers = utils.get_issued_numbers()
    last_number_issued = utils.get_last_number_issued()

    if last_number_issued:
        flask.flash("Dernier numéro pioché: {0}".format(last_number_issued.value))

    return flask.render_template(
        "home/index.html",
        numbers=numbers,
        issued_numbers=issued_numbers
    )
