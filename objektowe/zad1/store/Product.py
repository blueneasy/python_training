
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


class ExpiringProduct(Product):
    def __init__(self, name, category, unit_price, production_year, validity_years):
        super().__init__(name, category, unit_price)
        self.validity_years = validity_years
        self.production_year = production_year

    def does_expire(self, current_year):
        expiration_year = self.production_year + self.validity_years
        return current_year > expiration_year


product1 = Product('pianino', 'instrumenty', 1200)
product1b = Product('pianino', 'instrumenty', 1200)
product2 = Product('szafa', 'meble', 1000)
product3 = Product('ziemniak', 'ziemniaki', 0.2)
products = [product3, product2, product1]
expired_product = ExpiringProduct('Zgniłe warzywo', 'Veggie', 3, 2000, 2)
not_expired_product = ExpiringProduct('Świeżutkie jabłuszko', 'Fruit', 2, 2022, 2)
#
# print(expired_product.does_expire(2022))
# print(not_expired_product.does_expire(2022))


