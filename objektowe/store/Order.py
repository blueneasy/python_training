from objektowe.store.products import Product
from objektowe.store.OrderElement import OrderElement
from objektowe.store.Policies import DiscountPolicy
from objektowe.store.Policies import abs_100, prc_10


class Order:
    MAX_ORDER_ELEMENTS = 8

    def __init__(self, client_name, order_elements=None, policy=DiscountPolicy):
        self.policy = policy
        self.client_name = client_name

        if order_elements is None:
            order_elements = []
        self._order_elements = order_elements

    @property
    def order_elements(self):
        return self._order_elements

    @order_elements.setter
    def order_elements(self, order_elements):
        if len(order_elements) > Order.MAX_ORDER_ELEMENTS:
            self._order_elements = order_elements[:Order.MAX_ORDER_ELEMENTS]
            print(f'Przekroczono maksymalną ilość elementów - {Order.MAX_ORDER_ELEMENTS}!')
        else:
            self._order_elements = order_elements

    @property
    def order_price(self):
        order_price = 0
        for element in self._order_elements:
            order_price += element.calc_element_price
        final_price = self.policy.apply_discount(order_price)
        return final_price

    def dodaj_element(self, product, quantity):
        if len(self._order_elements) < Order.MAX_ORDER_ELEMENTS:
            new_element = OrderElement(product, quantity)
            self._order_elements.append(new_element)
            print('Dodano element!')
        else:
            print(f'Nie dodano elementu - przekracza maksymalną ilość elementów - {Order.MAX_ORDER_ELEMENTS}!')

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


class ExpressOrder(Order):
    EXPRESS_DELIVERY_FEE = 20

    def __init__(self, client_name, order_elements, policy, delivery_date):
        super().__init__(client_name, order_elements, policy)
        self.delivery_date = delivery_date

    @property
    def order_price(self):
        return super().order_price + ExpressOrder.EXPRESS_DELIVERY_FEE

    def __str__(self):
        header = (
            f'-----Zamowienie Expresowe-----\n'
            f'Klient: {self.client_name}\n'
            f'Zamówione produkty:\n'
        )

        details = ""
        for element in self._order_elements:
            details += f'\t{element} \n'

        footer = (
                '\t' * 15 + '=' * 25 + '\n'
                + '\t' * 15 + f'Wartość zamówienia po rabatach: {super().order_price}zł \n'
                + '\t' * 15 + f'Koszt przesyłki: {ExpressOrder.EXPRESS_DELIVERY_FEE}zł \n'
                + '\t' * 15 + f'Łączna wartość zamówienia: {self.order_price}zł'

        )

        return header + details + footer


def porownaj_listy(lista_a, lista_b):
    for i in lista_a:
        if i not in lista_b:
            return False
    return True


order1 = Order('Janusz Jarzyna', [OrderElement(Product(2147, 'Testowy2', 'randomowa', 124), 5),
                                  OrderElement(Product(666, 'Testowy', 'randomowa', 124), 7)])
order2 = Order('Janusz Jarzyna', [])
#
# order_express = ExpressOrder('Szybki Michał', [OrderElement(Product('Bardzo potrzebny kabel', 'kable', 12), 1),
#                                                OrderElement(Product('MMMSY', 'łakocie dla Magdy', 4.65), 2)],
#                              policy=DiscountPolicy, delivery_date='21-05-2022')
#
# order_express2 = ExpressOrder('Szybki Michał', [OrderElement(Product('Bardzo potrzebny kabel', 'kable', 12), 1),
#                                                 OrderElement(Product('MMMSY', 'łakocie dla Magdy', 4.65), 2)],
#                               policy=abs_100, delivery_date='21-05-2022')
#
# order_express3 = ExpressOrder('Szybki Michał', [OrderElement(Product('Bardzo potrzebny kabel', 'kable', 12), 1),
#                                                 OrderElement(Product('MMMSY', 'łakocie dla Magdy', 4.65), 2)],
#                               policy=prc_10, delivery_date='21-05-2022')

# element1 = OrderElement(Product('Testowy', 'randomowa', 124), 4)
# element2 = OrderElement(Product('Testowy', 'randomowa', 124), 5)
#
orders = [
    order1,
    order2
]
