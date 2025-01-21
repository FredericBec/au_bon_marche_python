from dataclasses import dataclass

import Customer


@dataclass
class Cart:
    purchases: list
    total: float
    customer: Customer

    def __repr__(self):
        return f"{self.customer}, {self.purchases}, {self.total}"
