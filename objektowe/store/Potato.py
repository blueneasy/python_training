from dataclasses import dataclass


@dataclass
class Potato:
     sort: str
     size: str
     kg_price: float


potato1 = Potato('ziemniak', 'b', 0.06)
potato2 = Potato('topinambur', 's', 0.1)
