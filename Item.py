from dataclasses import dataclass


@dataclass
class Item:
    name: str
    quantity: int
    total_cost: float

    def __repr__(self):
        return f"{self.name}, {self.quantity}, {self.total_cost}"
