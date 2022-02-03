import random
from .Product import Product, product1, product2, product3


class Order:
    def __init__(self, client_name, product_list=None):
        self.client_name = client_name
        if product_list is None:
            product_list = []
        self.product_list = product_list

        total_price = 0
        for product in product_list:
            total_price += product.unit_price
        self.total_price = total_price


def wypisz_zamowienie():
    for i in orders:
        print(i.client_name, [i.product_list])


def generuj_zamowienie():
    random_lista = []
    for i in range(0, random.randint(1, 20)):
        random_product = Product('Produkt-'+str(i), 'random', 100)
        random_lista.append(random_product)
    nowe_zamowienie = Order('Kowalski', random_lista)
    print(nowe_zamowienie)
    print(nowe_zamowienie.client_name, random_lista[0].name)


order1 = Order('Janusz Jarzyna', [product1, product2, product3])
order2 = Order('Mirosław Łotysz', [product3])
order3 = Order('Hubert Chrząkała', [product3, product2])

orders = [
    order1,
    order2,
    order3,
]
