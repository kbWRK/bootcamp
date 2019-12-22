class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        print(f"Produkt {self.name!r}, id: {self.id}, cena: {self.price} PLN")


def test_product_init():
    product = Product(1, 'Woda', 10.99)
    assert product.id == 1
    assert product.name == 'Woda'
    assert product.price == 10.99


def test_print_info(capsys):
    product = Product(1, 'Woda', 10.99)
    product.print_info()
    captured = capsys.readouterr()
    assert captured.out == "Produkt 'Woda', id: 1, cena: 10.99 PLN\n"


if __name__ == "__main__":
    product = Product(1, 'Woda', 10.99)
    product.print_info()


class Basket:
    def __init__(self):
        self._products = {}

    def add_product(self, produkt, quantity):
        if produkt in self._products:
            self._products[produkt] += quantity
        else:
            self._products[produkt] = quantity

    def count_total_price(self):
        total_price = 0
        for product, quantity in self._products.items():
            total_price += product.price * quantity
        return total_price


# roduct = Product(1, "woda", 10.99)
# basket.add_product(product, 5)
# basket.count_total_price()

def test_basket_empty_price():
    b = Basket()
    p = Product(1, "woda", 10.99)
    b.add_product(p, 3)
    assert b.count_total_price() == 10.99 * 3


def test_basket_mltiple_product_price():
    b = Basket()
    woda = Product(1, "woda", 10)
    chleb = Product(2, "chleb", 20)
    b.add_product(woda, 2)
    b.add_product(chleb, 2)
    b.add_product(woda, 2)
    assert b.count_total_price() == 10 * 4 + 2 * 20
