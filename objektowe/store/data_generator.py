from objektowe.store.Policies import Policies
from objektowe.store.Product import Product
import random
from objektowe.store.OrderElement import OrderElement
from objektowe.store.Order import Order, orders
from objektowe.store.StudentListPack import StudentList


class Generator:

    MIN_QUANTITY = 1
    MAX_QUANTITY = 10

    MIN_UNIT_PRICE = 1
    MAX_UNIT_PRICE = 30

    @staticmethod
    def generuj_zamowienie(number_of_products=None, policy=Policies.default_policy):
        lista_elementow = StudentList()
        if number_of_products is None:
            number_of_products = random.randint(1, Order.MAX_ORDER_ELEMENTS)

        for i in range(number_of_products):
            product_name = 'Produkt-' + str(i + 1)
            category = 'Fruit'
            unit_price = random.randint(Generator.MIN_UNIT_PRICE, Generator.MAX_UNIT_PRICE)
            random_product = Product(product_name, category, unit_price)
            quantity = random.randint(Generator.MIN_QUANTITY, Generator.MAX_QUANTITY)
            element = OrderElement(random_product, quantity)
            lista_elementow.append(element)
        nowe_zamowienie = Order('Katarzyna Zwijaj-Rogala', lista_elementow, policy)
        orders.append(nowe_zamowienie)

    @staticmethod
    def generuj_linie_zamowienia(number_of_products):
        lista_elementow = []
        if number_of_products is None:
            number_of_products = random.randint(1, Order.MAX_ORDER_ELEMENTS)

        for i in range(number_of_products):
            product_name = 'Produkt-' + str(i + 1)
            category = 'Fruit'
            unit_price = random.randint(Generator.MIN_UNIT_PRICE, Generator.MAX_UNIT_PRICE)
            random_product = Product(product_name, category, unit_price)
            quantity = random.randint(Generator.MIN_QUANTITY, Generator.MAX_QUANTITY)
            element = OrderElement(random_product, quantity)
            lista_elementow.append(element)
        return lista_elementow
