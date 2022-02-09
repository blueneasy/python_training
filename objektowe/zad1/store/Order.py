import random
from store.Product import Product
from store.OrderElement import OrderElement
from store.Policies import Policies


class Order:

    MAX_ORDER_ELEMENTS = 8

    def __init__(self, client_name, order_elements=None, policy=Policies.default_policy):
        self.policy = policy
        self.client_name = client_name

        if order_elements is None:
            order_elements = []
        elif len(order_elements) > Order.MAX_ORDER_ELEMENTS:
            order_elements = order_elements[:Order.MAX_ORDER_ELEMENTS]
            print(f'Przekroczono liczbę możliwych linii - {Order.MAX_ORDER_ELEMENTS}!')
        self._order_elements = order_elements
        self.order_price = self._order_price()

    def _order_price(self):
        order_price = 0
        for element in self._order_elements:
            order_price += element.element_price
        final_price = self.policy(order_price)
        return final_price

    def dodaj_element(self, product, quantity):
        if len(self._order_elements) < Order.MAX_ORDER_ELEMENTS:
            new_element = OrderElement(product, quantity)
            self._order_elements.append(new_element)
            self.order_price = self._order_price()
            print('Dodano element!')
        else:
            print(f'Nie dodano elementu - przekracza maksymalną ilość elementów - {Order.MAX_ORDER_ELEMENTS}!')

    @classmethod
    def generuj_zamowienie(cls, number_of_products, policy=Policies.default_policy):
        lista_elementow = []
        for i in range(random.randint(number_of_products, number_of_products)):
            random_product = Product('Produkt-' + str(i + 1), 'Fruit', 100)
            element = OrderElement(random_product, random.randint(1, 16))
            lista_elementow.append(element)
        nowe_zamowienie = Order('Katarzyna Zwijaj-Rogala', lista_elementow, policy)
        orders.append(nowe_zamowienie)

    def __str__(self):
        header = (
            f'-----Zamowienie-----\n'
            f'Klient: {self.client_name}\n'
            f'Zamówione produkty:\n'
        )

        details = ""
        for element in self._order_elements:
            details += f'\t{element} \n'

        footer = (
                '\t' * 15 + '=' * 25 + '\n'
                + '\t' * 15 + f'Łączna wartość: {self.order_price} PLN.'
        )

        return header + details + footer

    def __len__(self):
        return len(self._order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.client_name == other.client_name and \
            len(self) == len(other) and \
            porownaj_listy(self._order_elements, other.order_elements)


def porownaj_listy(lista_a, lista_b):
    for i in lista_a:
        if i not in lista_b:
            return False
    return True


order1 = Order('Janusz Jarzyna', [OrderElement(Product('Testowy2', 'randomowa', 124), 5),
                                  OrderElement(Product('Testowy', 'randomowa', 124), 7)])
order2 = Order('Janusz Jarzyna', [OrderElement(Product('Testowy', 'randomowa', 124), 5),
                                  OrderElement(Product('Testowy2', 'randomowa', 124), 5)])


# element1 = OrderElement(Product('Testowy', 'randomowa', 124), 4)
# element2 = OrderElement(Product('Testowy', 'randomowa', 124), 5)

orders = [
    order1,
    order2
]
