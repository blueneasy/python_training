from dataclasses import dataclass


@dataclass
class Product:
    identifier: int
    name: str
    category: str
    unit_price: float

    def __str__(self):
        return f'ID:{self.identifier} | Nazwa: {self.name} | Kategoria: {self.category} | Cena/szt: {self.unit_price}'


@dataclass
class ExpiringProduct(Product):
    validity_years: int
    production_year: int

    def does_expire(self, current_year):
        expiration_year = self.production_year + self.validity_years
        return current_year > expiration_year


product1 = Product(123, 'pianino', 'instrumenty', 1200)
# product1b = Product('pianino', 'instrumenty', 1200)
# product2 = Product('szafa', 'meble', 1000)
# product3 = Product('ziemniak', 'ziemniaki', 0.2)
# products = [product3, product2, product1]
# expired_product = ExpiringProduct('Zgniłe warzywo', 'Veggie', 3, 2000, 2)
# not_expired_product = ExpiringProduct('Świeżutkie jabłuszko', 'Fruit', 2, 2022, 2)
#
# print(expired_product.does_expire(2022))
# print(not_expired_product.does_expire(2022))


