
class Apple:
    def __init__(self, sort, size, kg_price):
        self.sort = sort
        self.size = size
        self.kg_price = kg_price
        self.unit_price = self.kg_price * self.size


apple1 = Apple('szampion', 1, 1.54)
apple2 = Apple('lobo', 0.7, 1.2 )
apple3 = Apple('jonagold', 0.9, 1.6)