import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.read(source_path)

    def read(self, source_path: str) -> None:
        with open(source_path, newline='', encoding='utf-8') as csvfile:
            dish_set = {}

            reader = csv.DictReader(csvfile)
            for r in reader:
                name = r['dish']
                price = float(r['price'])
                ingredient_name = r['ingredient']
                quantity = int(r['recipe_amount'])
                dish = Dish(name, price)

                if name not in dish_set:
                    self.dishes.add(dish)
                    dish_set[name] = dish
                else:
                    dish = dish_set[name]

                ingredient = Ingredient(ingredient_name)
                if ingredient not in dish.recipe:
                    dish.add_ingredient_dependency(ingredient, quantity)
