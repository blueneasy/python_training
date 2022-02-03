
class Product:
    def __init__(self, name, category, unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price


def wypisz_produkty():
    for i in products:
        print(i.name, [i.unit_price, i.category])


product1 = Product('pianino', 'instrumenty', 1200)
product2 = Product('szafa', 'meble', 1000)
product3 = Product('ziemniak', 'ziemniaki', 0.2)
products = [product3, product2, product1]