from flask import Blueprint, jsonify, request

from application import utils

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/draw", methods=["POST",])
def draw():
    issued_numbers = utils.get_issued_numbers()
    number = utils.draw_number(issued_numbers)

    return jsonify(number=number)


@bp.route("/insert", methods=["POST",])
def insert():
    data = request.json
    number_to_insert = utils.insert_number_in_db(data["number"])

    return jsonify(inserted=number_to_insert.value)


@bp.route("/get_numbers")
def get_numbers():
    numbers = utils.get_issued_numbers()

    return jsonify(numbers=numbers)
