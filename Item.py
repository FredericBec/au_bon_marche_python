from dataclasses import dataclass


@dataclass
class Item:
    name: str
    quantity: int
    total_cost: float
