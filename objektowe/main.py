from store.Order import orders
# from store.Order import order_express, order_express2, order_express3
from store.Policies import DiscountPolicy
from store.data_generator import Generator


def element_price(order_element):
    return order_element.calc_element_price()


def run_homework():
    Generator.generuj_zamowienie(50, policy=DiscountPolicy)
    # print(orders[0])

    # elements = orders[2]._order_elements
    # elements.sort(key=lambda element: element.calc_element_price(), reverse=True)
    # for element in elements:
    #     print(element)

    nowe_linie = Generator.generuj_linie_zamowienia(40)
    # print(nowe_linie)
    orders[1].order_elements = nowe_linie
    print(orders[1])

    # dict comprehension
    identifier_to_product = {
        linia.product.identifier: linia.product for linia in nowe_linie
    }
    # print(identifier_to_product)

    new = {
        id+1: rest for id, rest in identifier_to_product.items()
    }

    # print(new)
    available_products = set()
    ordered_products = set([element.product.name for element in orders[1].order_elements])
    new_delivery = set()
    left_to_order = ordered_products.difference(new_delivery)
    print(f'pozostało do zamówienia: {left_to_order}')
    while len(left_to_order) > 0:
        new_delivery = set(Generator.products_delivery(5))
        available_products.update(new_delivery)
        left_to_order = ordered_products.difference(available_products)
        print(f'dostawa: {new_delivery}')
        print(f'pozostało do zamówienia: {left_to_order}')
    print('done! all products available now.')



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

    # print(order_express)
    # print(order_express2)
    # print(order_express3)


if __name__ == '__main__':
    run_homework()
