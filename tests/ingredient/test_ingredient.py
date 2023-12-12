from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    ingredient = Ingredient('carne')

    assert ingredient.name == 'carne'
    assert ingredient.restrictions == {
        Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED
    }
    assert repr(ingredient) == "Ingredient('carne')"

    ingredient_B = Ingredient('salmão')
    ingredient_C = Ingredient('carne')

    assert ingredient != ingredient_B
    assert ingredient == ingredient_C

    assert hash(ingredient) == hash(ingredient_C)
    assert hash(ingredient) != hash(ingredient_B)
