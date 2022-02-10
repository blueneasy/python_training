from store.Policies import Policies
from store.Product import Product
import random
from store.OrderElement import OrderElement
from store.Order import Order, orders

MIN_QUANTITY = 1
MAX_QUANTITY = 10

MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30


def generuj_zamowienie(number_of_products=None, policy=Policies.default_policy):
    lista_elementow = []
    if number_of_products is None:
        number_of_products = random.randint(1, Order.MAX_ORDER_ELEMENTS)

    for i in range(number_of_products):
        product_name = 'Produkt-' + str(i + 1)
        category = 'Fruit'
        unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
        random_product = Product(product_name, category, unit_price)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        element = OrderElement(random_product, quantity)
        lista_elementow.append(element)
    nowe_zamowienie = Order('Katarzyna Zwijaj-Rogala', lista_elementow, policy)
    orders.append(nowe_zamowienie)