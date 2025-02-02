import pytest
from praktikum.database import Database
import data


class TestDatabase:

    @pytest.mark.parametrize('db_index, db_bun_name, db_bun_price', data.buns_db)
    def test_get_available_buns_got_successfully(self, db_index, db_bun_name, db_bun_price):
        database = Database()
        available_buns = database.available_buns()
        assert available_buns[db_index].get_name() == db_bun_name \
               and available_buns[db_index].get_price() == db_bun_price
        assert len(available_buns) == 3

    @pytest.mark.parametrize('db_index, db_type_of_ingredient, db_ingredient_name, db_ingredient_price',
                             data.ingredients_db)
    def test_get_available_ingredients_got_successfully(self, db_index, db_type_of_ingredient, db_ingredient_name,
                                       db_ingredient_price):
        database = Database()
        available_ingredients = database.available_ingredients()
        assert available_ingredients[db_index].get_type() == db_type_of_ingredient \
               and available_ingredients[db_index].get_name() == db_ingredient_name \
               and available_ingredients[db_index].get_price() == db_ingredient_price
        assert len(available_ingredients) == 6
