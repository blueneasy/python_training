
class OrderElement:
    def __init__(self, product, quantity):
        self.quantity = quantity
        self.product = product
        self.element_price = self.calc_element_price()

    def calc_element_price(self):
        element_price = self.quantity * self.product.unit_price
        return element_price

    def __str__(self):
        return f'{self.product} | Ilość: {self.quantity} | Wartość: {self.element_price}'

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.product == other.product and \
            self.quantity == other.quantity
