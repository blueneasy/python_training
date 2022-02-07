
class Potato:
    def __init__(self, sort, size, kg_price):
        self.sort = sort
        self.size = size
        self.kg_price = kg_price
        self.unit_price = self.kg_price * self.size

    def __repr__(self):
        return f'sort={self.sort}, size={self.size}, kg_price={self.kg_price}, unit_price={self.unit_price}'


    def total_price(self, size):
        total_price = self.kg_price * size
        return total_price


potato1 = Potato('ziemniak', 0.4, 0.06)
potato2 = Potato('topinambur', 0.3, 0.1)
