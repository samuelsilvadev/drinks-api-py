from flask import request
from config import app, db
from models import Drink, DrinkSchema
from marshmallow import ValidationError
from sqlalchemy import exc


@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()

    return DrinkSchema(many=True).dump(drinks), 200


@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)

    if drink == None:
        return "", 404

    return DrinkSchema().dump(drink), 200


@app.route('/drinks', methods=['POST'])
def create_drink():
    try:
        drink = DrinkSchema().load(request.json)
        body = request.json

        db.session.add(
            Drink(name=body['name'], description=body['description']))
        db.session.commit()

        return DrinkSchema().dump(drink), 201
    except ValidationError as validation_error:
        print(validation_error)

        return {'message': 'Invalid payload'}, 400
    except exc.IntegrityError as integrity_error:
        print(integrity_error)

        return {'message': 'Invalid data'}, 400


@app.route('/drinks/<id>', methods=['DELETE'])
def remove_drink(id):
    drink = Drink.query.get_or_404(id)

    if drink == None:
        return "", 404

    db.session.delete(drink)
    db.session.commit()
    return "", 204


@app.route('/drinks/<id>', methods=['PUT'])
def update_drink(id):
    registered_drink = Drink.query.get_or_404(id)

    if registered_drink == None:
        return "", 404

    try:
        body = request.json
        drink = DrinkSchema().load(body)

        drink_name = drink.get('name')
        drink_description = drink.get('description')

        if drink_name is not None:
            registered_drink.name = drink_name

        if drink_description is not None:
            registered_drink.description = drink_description

        db.session.commit()

        return DrinkSchema().dump(registered_drink), 200
    except ValidationError as validation_error:
        print(validation_error)

        return {'message': 'Invalid payload'}, 400
