import pytest
from praktikum.ingredient import Ingredient
import data


class TestIngredient:

    def test_create_ingredient_created_successfully(self):
        ingredient = Ingredient(ingredient_type=data.filling_type, name=data.filling_name, price=data.filling_price)
        assert ingredient.type == data.filling_type
        assert ingredient.name == data.filling_name
        assert ingredient.price == data.filling_price

    @pytest.mark.parametrize('ingredient_type, name, actual_price, expected_price', [
        [data.sauce_type, data.sauce_name, data.sauce_price, data.sauce_price],
        [data.filling_type, data.filling_name, data.filling_price, data.filling_price]])
    def test_ingredient_get_price_got_successfully(self, ingredient_type, name, actual_price, expected_price):
        ingredient = Ingredient(ingredient_type, name, actual_price)
        assert ingredient.get_price() == expected_price

    @pytest.mark.parametrize('ingredient_type, actual_name, expected_name, price', [
        [data.sauce_type, data.sauce_name, data.sauce_name, data.sauce_price],
        [data.filling_type, data.filling_name, data.filling_name, data.filling_price]])
    def test_ingredient_get_name_got_successfully(self, ingredient_type, actual_name, expected_name, price):
        ingredient = Ingredient(ingredient_type, actual_name, price)
        assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize('actual_ingredient_type, expected_ingredient_type, name, price', [
        [data.sauce_type, data.sauce_type, data.sauce_name, data.sauce_price],
        [data.filling_type, data.filling_type, data.filling_name, data.filling_price]])
    def test_ingredient_get_type_got_successfully(self, actual_ingredient_type, expected_ingredient_type, name, price):
        ingredient = Ingredient(actual_ingredient_type, name, price)
        assert ingredient.get_type() == expected_ingredient_type
