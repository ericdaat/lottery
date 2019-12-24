import random

from flask import Blueprint, jsonify, request

from application.model import Number, session

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/draw")
def draw_random_number():
    random_number = random.choice(range(1, 100))

    return jsonify(number=random_number)


@bp.route("/insert", methods=["POST",])
def insert_number_in_db():
    data = request.json
    number_to_insert = Number(value=data["number"])
    session.add(number_to_insert)
    session.commit()

    return jsonify(inserted=number_to_insert.value)


@bp.route("/get_numbers")
def get_issued_numbers():
    issued_numbers = Number.query.all()
    numbers = [n.value for n in issued_numbers]

    return jsonify(numbers=numbers)
