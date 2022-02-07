from store.Order import generuj_zamowienie, orders, Order
from store.Product import Product
from store.OrderElement import OrderElement

def run_homework():
    generuj_zamowienie()
    print(orders[2])
    orders[2].dodaj_element(Product('Testowy', 'randomowa', 124), 4)
    print(orders[2])

if __name__ == '__main__':
    run_homework()



