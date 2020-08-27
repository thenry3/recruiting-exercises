from typing import Dict


class Warehouse:
    def __init__(self, name: str, inventory: Dict[str, int]):
        self.name = name
        self.inventory = inventory
