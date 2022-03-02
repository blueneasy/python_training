from collections import namedtuple
from dataclasses import dataclass


@dataclass
class Apple:
    sort: str
    size: str
    price: float

    def calculate_price(self, quantity):
        return quantity * self.price


apple1 = Apple('szampion', 'b', 1.54)
apple2 = Apple('lobo', 's', 1.2)
apple3 = Apple('jonagold', 'm', 1.6)


Apple_tuple = namedtuple('Apple_tuple', ['sort', 'size', 'kg_price'])

apple_t = Apple_tuple('jonagold', 'm', 3)
