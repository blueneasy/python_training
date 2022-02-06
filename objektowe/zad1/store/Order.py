import random
from store.Product import Product, product1, product2, product3
# from .Product import wypisz_produkt


class Order:
    def __init__(self, client_name, order_elements=None):
        self.client_name = client_name
        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements

    def order_price(self):
        order_price = 0
        for element in self.order_elements:
            order_price += element.element_price()
        return order_price

    def wypisz_zamowienie(self):
        print(f'-----Zamowienie-----')
        print(f'Klient: {self.client_name}')
        print(f'Łączna wartość: {self.order_price()} PLN')
        print('Zamówione produkty:')

        for element in self.order_elements:
            element.wypisz_element()

        # products_formatted = []
        # for i in self.order_elements:
        #     products_formatted.append(Product.wypisz_produkt(i))
        print('=' * 20)


class OrderElement:
    def __init__(self, product, quantity):
        self.quantity = quantity
        self.product = product

    def element_price(self):
        element_price = self.quantity * self.product.unit_price
        return element_price

    def wypisz_element(self):
        print(f'Nazwa produktu: {self.product.name} | Ilość: {self.quantity} | Cena/szt: {self.product.unit_price} | Wartość: {self.element_price()}')


# def generuj_zamowienie():
#     random_lista_elementy = []
#     for i in range(random.randint(1, 20)):
#         random_product = Product('Produkt-'+str(i+1), 'random', 100)
#         random_lista_elementy.append([random_product, 1])
#     nowe_zamowienie = Order('Kowalski', random_lista_elementy)
#     orders.append(nowe_zamowienie)

def generuj_zamowienie():
    lista_elementow = []
    for i in range(random.randint(1, 20)):
        random_product = Product('Produkt-'+str(i+1), 'random', 100)
        element = OrderElement(random_product, random.randint(1, 16))
        lista_elementow.append(element)
    nowe_zamowienie = Order('Katarzyna Zwijaj-Rogala', lista_elementow)
    orders.append(nowe_zamowienie)


order1 = Order('Janusz Jarzyna', [product1, product2, product3])
order2 = Order('Mirosław Łotysz', [product3, 2])
order3 = Order('Hubert Chrząkała', [product3, product2])

orders = [
    order1,
    order2,
    order3,
]
