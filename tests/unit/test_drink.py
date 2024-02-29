from models import Drink


def test_drink_is_created_without_id():
    drink = Drink(name="beer", description="best beer in the world")

    assert drink.name == "beer"
    assert drink.description == "best beer in the world"
    assert drink.id == None


def test_drink_is_created_with_id():
    drink = Drink(id=1, name="beer", description="best beer in the world")

    assert drink.name == "beer"
    assert drink.description == "best beer in the world"
    assert drink.id == 1
