import unittest
from inventory_allocator import InventoryAllocator


class TestInventoryAllocator(unittest.TestCase):
    def test_happy_case(self):
        allocations = [{'owd': {'apple': 1}}]
        order = {"apple": 1}
        warehouses = [{"name": "owd", "inventory": {"apple": 1}}]

        output = InventoryAllocator().allocate(order, warehouses)
        self.assertEqual(allocations, output)

    def test_no_allocations(self):
        allocations = []
        order = {"apple": 1}
        warehouses = [{"name": "owd", "inventory": {"apple": 0}}]

        output = InventoryAllocator().allocate(order, warehouses)
        self.assertEqual(allocations, output)

    def test_split(self):
        allocations = [{"dm": {"apple": 5}}, {"owd": {"apple": 5}}]
        order = {"apple": 10}
        warehouses = [{"name": "dm", "inventory": {"apple": 5}}, {
            "name": "owd", "inventory": {"apple": 5}}]

        output = InventoryAllocator().allocate(order, warehouses)
        self.assertEqual(allocations, output)

    def test_assertion(self):
        order = {"apple": 1}
        warehouses = [{"hello": "owd", "inventory": {"apple": 0}}]

        self.assertRaises(
            ValueError, InventoryAllocator().allocate, order, warehouses)

    def test_empty_inputs(self):
        allocations = []
        order = {}
        warehouses = []

        output = InventoryAllocator().allocate(order, warehouses)
        self.assertEqual(allocations, output)

    def test_no_order(self):
        allocations = []
        order = {}
        warehouses = [{"name": "owd", "inventory": {"apple": 1}}]

        output = InventoryAllocator().allocate(order, warehouses)
        self.assertEqual(allocations, output)

    def test_no_warehouses(self):
        allocations = []
        order = {"apple": 1}
        warehouses = []

        output = InventoryAllocator().allocate(order, warehouses)
        self.assertEqual(allocations, output)

    def test_negative(self):
        allocations = []
        order = {"apple": -2}
        warehouses = [{"name": "owd", "inventory": {"apple": 1}}]

        output = InventoryAllocator().allocate(order, warehouses)
        self.assertEqual(allocations, output)

    def test_heavy(self):
        allocations = [{"hello": {"apple": 3, "watermelon": 20}}, {
            "qwerty": {"watermelon": 10}}, {"lol": {"watermelon": 10}}]
        order = {"apple": 3, "watermelon": 40, "pear": 300}
        warehouses = [
            {
                "name": "hello",
                "inventory": {
                    "peach": 1,
                    "pear": 5,
                    "apple": 3,
                    "watermelon": 20
                }
            },
            {
                "name": "qwerty",
                "inventory": {
                    "pear": 2,
                    "apple": 4,
                    "watermelon": 10
                }
            },
            {
                "name": "lol",
                "inventory": {
                    "pear": 5,
                    "watermelon": 600
                }
            }
        ]

        output = InventoryAllocator().allocate(order, warehouses)
        self.assertEqual(allocations, output)


if __name__ == "__main__":
    unittest.main()
