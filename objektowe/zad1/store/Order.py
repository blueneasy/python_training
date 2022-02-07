import random
from store.Product import Product
from store.OrderElement import OrderElement


class Order:
    def __init__(self, client_name, order_elements=None):
        self.client_name = client_name
        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements
        self.order_price = self.order_price()

    def order_price(self):
        order_price = 0
        for element in self.order_elements:
            order_price += element.element_price
        return order_price

    def __str__(self):
        header = (
            f'-----Zamowienie-----\n'
            f'Klient: {self.client_name}\n'
            f'Zamówione produkty:\n'
        )

        details = ""
        for element in self.order_elements:
            details += f'\t{element} \n'

        footer = (
                '\t' * 15 + '=' * 25 + '\n'
                + '\t' * 15 + f'Łączna wartość: {self.order_price} PLN.'
        )

        return header + details + footer

    def __len__(self):
        return len(self.order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.client_name == other.client_name and \
            len(self) == len(other) and \
            porownaj_listy(self.order_elements, other.order_elements)


def generuj_zamowienie():
    lista_elementow = []
    for i in range(random.randint(1, 20)):
        random_product = Product('Produkt-' + str(i + 1), 'random', 100)
        element = OrderElement(random_product, random.randint(1, 16))
        lista_elementow.append(element)
    nowe_zamowienie = Order('Katarzyna Zwijaj-Rogala', lista_elementow)
    orders.append(nowe_zamowienie)


def porownaj_listy(lista_a, lista_b):
    for i in lista_a:
        if i not in lista_b:
            return False
    return True


order1 = Order('Janusz Jarzyna', [OrderElement(Product('Testowy2', 'randomowa', 124), 5),
                                  OrderElement(Product('Testowy', 'randomowa', 124), 7)])
order2 = Order('Janusz Jarzyna', [OrderElement(Product('Testowy', 'randomowa', 124), 5),
                                  OrderElement(Product('Testowy2', 'randomowa', 124), 5)])
#
# element1 = OrderElement(Product('Testowy', 'randomowa', 124), 4)
# element2 = OrderElement(Product('Testowy', 'randomowa', 124), 5)

orders = [
    order1,
    order2
]
