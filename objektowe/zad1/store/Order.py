import random
from .Product import Product, product1, product2, product3
from .Product import wypisz_produkt


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


def wypisz_zamowienie(order):
    print(f'-----Zamowienie-----')
    print(f'Klient: {order.client_name}')
    print(f'O łącznej wartości {order.total_price} PLN')
    print('Zamówione produkty:')
    products_formatted = []
    for i in order.product_list:
        products_formatted.append(wypisz_produkt(i))
    print('=' * 20)




def generuj_zamowienie():
    random_lista = []
    for i in range(random.randint(1, 20)):
        random_product = Product('Produkt-'+str(i), 'random', 100)
        random_lista.append(random_product)
    nowe_zamowienie = Order('Kowalski', random_lista)
    orders.append(nowe_zamowienie)

order1 = Order('Janusz Jarzyna', [product1, product2, product3])
order2 = Order('Mirosław Łotysz', [product3])
order3 = Order('Hubert Chrząkała', [product3, product2])

orders = [
    order1,
    order2,
    order3,
]
