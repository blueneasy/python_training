
class Potato:
    def __init__(self, sort, size, kg_price):
        self.sort = sort
        self.size = size
        self.kg_price = kg_price
        self.unit_price = self.kg_price * self.size


potato1 = Potato('ziemniak', 0.4, 0.06)
potato2 = Potato('topinambur', 0.3, 0.1)