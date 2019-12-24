import json
from http import HTTPStatus

from flask import url_for

from application.model import Number, session


def test_draw(client):
    response = client.get(url_for('api.draw'))

    assert response.status_code == HTTPStatus.OK
    assert "number" in response.json

    number = response.json["number"]
    assert isinstance(number, int)
    assert 0 < number < 100


def test_insert(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "number": "3"
    }

    response = client.post(
        url_for("api.insert"),
        data=json.dumps(data),
        headers=headers
    )

    assert response.status_code == HTTPStatus.OK
    assert "inserted" in response.json

    number = response.json["inserted"]
    assert isinstance(number, int)
    assert number == int(data["number"])

    assert Number.query.filter_by(value=number).first()

    Number.query.delete()
    session.commit()


def test_get_issued_numbers(client):
    session.add(Number(value=5))
    session.add(Number(value=6))
    session.add(Number(value=7))
    session.commit()

    response = client.get(url_for('api.get_numbers'))

    assert response.status_code == HTTPStatus.OK
    assert "numbers" in response.json

    numbers = response.json["numbers"]
    assert isinstance(numbers, list)
    assert len(numbers)
    assert numbers == [5, 6, 7]

    Number.query.delete()
    session.commit()
