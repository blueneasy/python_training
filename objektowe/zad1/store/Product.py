
class Product:
    def __init__(self, name, category, unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price

    def __str__(self):
        return f'Nazwa: {self.name} | Kategoria: {self.category} | Cena/szt: {self.unit_price}'

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.name == other.name and \
            self.category == other.category and \
            self.unit_price == other.unit_price


product1 = Product('pianino', 'instrumenty', 1200)
product1b = Product('pianino', 'instrumenty', 1200)
product2 = Product('szafa', 'meble', 1000)
product3 = Product('ziemniak', 'ziemniaki', 0.2)
products = [product3, product2, product1]

