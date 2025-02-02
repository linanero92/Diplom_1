from praktikum.bun import Bun
import data


class TestBun:

    def test_create_bun_created_successfully(self):
        bun = Bun(name=data.bun_name, price=data.bun_price)
        assert bun.name == data.bun_name
        assert bun.price == data.bun_price

    def test_bun_get_name_got_successfully(self):
        bun = Bun(name=data.bun_name, price=data.bun_price)
        assert bun.get_name() == data.bun_name

    def test_bun_get_price_got_successfully(self):
        bun = Bun(name=data.bun_name, price=data.bun_price)
        assert bun.get_price() == data.bun_price
