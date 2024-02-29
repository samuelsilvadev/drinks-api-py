import pytest
import json
from application import app, db
import models


@pytest.fixture
def client():
    with app.test_request_context():
        with app.test_client() as client:
            yield client


@pytest.fixture
def init_database():
    with app.app_context():

        db.create_all()

        yield

        db.drop_all()


def test_get_drinks(client, init_database):
    response = client.get('/drinks')

    assert response.status_code == 200
    assert response.data == b'[]\n'


def test_get_drink(client, init_database):
    client.post(
        '/drinks',
        headers={"Content-Type": "application/json"},
        data=json.dumps(
            {"name": "beer", "description": "the best beer in the world"})
    )
    response = client.get('/drinks/1')
    parsed_response = models.DrinkSchema().loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert parsed_response['name'] == 'beer'
    assert parsed_response['description'] == 'the best beer in the world'


def test_get_unknown_drink(client, init_database):
    response = client.get('/drinks/1')

    assert response.status_code == 404
