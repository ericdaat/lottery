from http import HTTPStatus

from flask import url_for


def test_home(client):
    response = client.get(url_for('home.index'))
    assert response.status_code == HTTPStatus.OK
