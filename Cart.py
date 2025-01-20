from dataclasses import dataclass

import Customer


@dataclass
class Cart:
    purchases: list
    total: float
    customer: Customer

