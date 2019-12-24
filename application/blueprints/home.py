import logging

import flask

from application.model import User

bp = flask.Blueprint("home", __name__)


@bp.route("/")
def index():
    users = User.query.all()
    logging.info("{0} user(s) in the db".format(len(users)))

    return flask.render_template("home/index.html")
