from store.Order import orders, Order
from store.Product import Product
from store.TaxCalculator import TaxCalculator
from store.OrderElement import OrderElement
from store.Policies import Policies


def element_price(order_element):
    return order_element.calc_element_price()


def run_homework():
    Order.generuj_zamowienie(5, Policies.loyal_customer_policy)
    print(orders[2])

    elements = orders[2]._order_elements
    elements.sort(key=lambda element: element.calc_element_price(), reverse=True)
    for element in elements:
        print(element)

    # orders[2].dodaj_element(Product('Testowy', 'randomowa', 124), 4)
    # print(orders[2])
    # TaxCalculator.tax_order(orders[2])

    # marchew = OrderElement(Product('Marchew', 'Veggie', 1), 75)
    # wolowina = OrderElement(Product('Wołowina', 'Food', 100), 1)
    # rower = OrderElement(Product('Rower', 'Sprzęt', 1), 1000)
    #
    # tax_marchew = TaxCalculator.tax_element(marchew)
    # tax_wolowina = TaxCalculator.tax_element(wolowina)
    # tax_rower = TaxCalculator.tax_element(rower)
    #
    # print(f'Cena marchwi: {marchew.element_price}zł + tax {tax_marchew}zł')
    # print(f'Cena wołowiny: {wolowina.element_price}zł + tax {tax_wolowina}zł')
    # print(f'Cena roweru: {rower.element_price}zł + tax {tax_rower}zł')


if __name__ == '__main__':
    run_homework()
