from store.products import Product
from dataclasses import dataclass
# from products import product1


@dataclass
class OrderElement:
    product: Product
    quantity: int

    @property
    def calc_element_price(self):
        element_price = self.quantity * self.product.unit_price
        return element_price

    def __str__(self):
        return f'{self.product} | Ilość: {self.quantity} | Wartość: {self.calc_element_price}'


# x = OrderElement(product=product1, quantity=2)
