from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


bun_price: float = 988.0
bun_name = 'Флюоресцентная булка R2-D3'
sauce_type = INGREDIENT_TYPE_SAUCE
sauce_name = 'Соус традиционный галактический'
sauce_price: float = 15.0
filling_type = INGREDIENT_TYPE_FILLING
filling_name = 'Плоды Фалленианского дерева'
filling_price: float = 824.0
burger_price = 1003.0

receipt = ("(==== Флюоресцентная булка R2-D3 ====)\n"
                   "= sauce Соус традиционный галактический =\n"
                   "(==== Флюоресцентная булка R2-D3 ====)\n"
                   "\n"
                   "Price: 1003.0")


buns_db = [[0, "black bun", 100], [1, "white bun", 200], [2, "red bun", 300]]
ingredients_db = [[0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100], [1, INGREDIENT_TYPE_SAUCE, "sour cream", 200],
                  [2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300], [3, INGREDIENT_TYPE_FILLING, "cutlet", 100],
                  [4, INGREDIENT_TYPE_FILLING, "dinosaur", 200], [5, INGREDIENT_TYPE_FILLING, "sausage", 300]]
