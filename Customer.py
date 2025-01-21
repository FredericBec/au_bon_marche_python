from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    first_name: str

    def __repr__(self):
        return f"{self.name} - {self.first_name}"
