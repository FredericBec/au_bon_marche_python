from dataclasses import dataclass

import Stock


@dataclass
class Vegetable:
    name: str
    stock: Stock
    price: float
