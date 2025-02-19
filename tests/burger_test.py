from unittest.mock import patch
import data
from praktikum.burger import Burger


class TestBurger:

    @patch('praktikum.burger.Bun')
    def test_set_buns_set_successfully(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @patch('praktikum.burger.Ingredient')
    def test_add_ingredient_one_ingredient_added(self, mock_ingredient):
        burger = Burger()
        mock_ingredient.get_price.return_value = data.filling_price
        mock_ingredient.get_name.return_value = data.filling_name
        mock_ingredient.get_type.return_value = data.filling_type
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_price() == data.filling_price
        assert burger.ingredients[0].get_name() == data.filling_name
        assert burger.ingredients[0].get_type() == data.filling_type

    @patch('praktikum.burger.Ingredient')
    def test_remove_ingredient_one_ingredient_removed(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    @patch('praktikum.burger.Ingredient')
    @patch('praktikum.burger.Ingredient')
    def test_move_ingredient_ingredients_removed(self, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_ingredient_2
        assert burger.ingredients[1] == mock_ingredient_1

    @patch('praktikum.burger.Bun')
    @patch('praktikum.burger.Ingredient')
    def test_burger_get_price_got_successfully(self, mock_ingredient, mock_bun):
        mock_bun.return_value.get_price.return_value = data.bun_price / 2
        mock_ingredient.return_value.get_price.return_value = data.sauce_price
        burger = Burger()
        burger.set_buns(mock_bun.return_value)
        burger.add_ingredient(mock_ingredient.return_value)
        assert burger.get_price() == data.burger_price

    @patch('praktikum.burger.Bun')
    @patch('praktikum.burger.Ingredient')
    def test_get_receipt_got_successfully(self, mock_ingredient, mock_bun):
        mock_bun.return_value.get_name.return_value = data.bun_name
        mock_bun.return_value.get_price.return_value = data.bun_price / 2
        mock_ingredient.return_value.get_price.return_value = data.sauce_price
        mock_ingredient.return_value.get_name.return_value = data.sauce_name
        mock_ingredient.return_value.get_type.return_value = data.INGREDIENT_TYPE_SAUCE
        burger = Burger()
        burger.set_buns(mock_bun.return_value)
        burger.add_ingredient(mock_ingredient.return_value)
        assert burger.get_receipt() == data.RECEIPT
