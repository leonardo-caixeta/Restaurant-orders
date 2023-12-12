from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    dish = Dish('quiche', 21.99)

    assert dish.name == 'quiche'
    assert repr(dish) == "Dish('quiche', R$21.99)"

    queijo = Ingredient('queijo')
    farinha = Ingredient('farinha')
    massa = Ingredient('massa')
    dish.add_ingredient_dependency(queijo, 5)
    dish.add_ingredient_dependency(farinha, 4)
    dish.add_ingredient_dependency(massa, 8)

    assert dish.recipe == {
        Ingredient('queijo'): 5,
        Ingredient('farinha'): 4,
        Ingredient('massa'): 8
    }
    assert dish.get_ingredients() == {queijo, farinha, massa}

    dish2 = Dish('quiche', 21.99)
    dish3 = Dish('bolo', 11.99)

    assert dish == dish2
    assert dish != dish3
    assert hash(dish) == hash(dish2)
    assert hash(dish) != hash(dish3)

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish('quitute', 'vinte merrél')

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish('quitute', -15.00)

    assert dish.get_restrictions() == {Restriction.GLUTEN}
