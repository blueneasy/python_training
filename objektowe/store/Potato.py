from dataclasses import dataclass


@dataclass
class Potato:
    sort: str
    size: str
    price: float

    def calculate_price(self, quantity):
        return quantity * self.price

potato1 = Potato('ziemniak', 'b', 0.06)
potato2 = Potato('topinambur', 's', 0.1)
