from dataclasses import dataclass

import Stock


@dataclass
class Fruit:
    name: str
    stock: Stock
    price: float
