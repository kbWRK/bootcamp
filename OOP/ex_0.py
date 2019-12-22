class Product:
    def __init__(self, id , name, price):
        self.id = id
        self.name = name
        self.price = price
    def print_info(self):
        print(f"produkt{self.name!r}, id: {self.id!r}, cena {self.price!r}")

def test_product_init():
    product = Product(1, 'woda', 10.99)
    assert product.id == 1
    assert product.name == "woda"
    assert product.price == 10.99
def test_product_info(capsys):
    product = Product(1, "woda", 10.99)
    product.print_info()
    captured = capsys.readouterr()
if __name__ == '__main__':
    product = Product(1,"woda",10.99)
    Product.print_info(None)