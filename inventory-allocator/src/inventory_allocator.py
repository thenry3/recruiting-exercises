from typing import List, Dict, Any
from warehouse import Warehouse


class InventoryAllocator():
    def validate_warehouse(self, warehouse: Dict[str, Any]) -> bool:
        '''
        Validates warehouse object format. Helper function for allocate()

        Args:
            warehouse: warehouse to be validated

        Returns:
            bool: True if warehouse is validated, False otherwise
        '''
        if "name" not in warehouse or "inventory" not in warehouse:
            return False
        return True

    def allocate(self, order: Dict[str, int], warehouses: List[Dict[str, Any]]) -> List[Dict[str, Dict[str, int]]]:
        '''
        Allocates inventory from warehouse to order based on best price

        Args: 
            order: orders to be processed
            warehouses: list of available warehouses and their inventory

        Returns:
            List[Dict[str, Dict[str, int]]]: list of orders fulfilled for each warehouse
        '''
        allocations = []
        if not order:
            return allocations

        for warehouse in warehouses:
            # validate warehouse
            if not self.validate_warehouse(warehouse):
                raise ValueError("Warehouse invalid")

            # intialize warehouse and allocation
            warehouse = Warehouse(warehouse["name"], warehouse["inventory"])
            allocation = {}

            # check if warehouse can fulfill any order item
            for item, quantity in order.items():
                stock = warehouse.inventory.get(item, 0)

                # if no stock or no need for more fulfillment for current item
                # move on to another item
                if not (quantity > 0 and stock > 0):
                    continue

                # calculate as much quantity to fulfill for the current warehouse and item
                order[item] = max(order[item] - stock, 0)
                allocation[item] = quantity - order[item]

            # add allocation if warehouse has any allocations
            if allocation:
                allocations.append({warehouse.name: allocation})

        # check for items that could not be fully fulfilled
        for item, quantity in order.items():
            if quantity == 0:
                continue

            # delete item from allocations
            for warehouse in allocations:
                name = list(warehouse.keys())[0]
                allocation = warehouse[name]
                if item in allocation:
                    del allocation[item]

        # remove empty allocations and return
        allocations = list(filter(lambda warehouse: len(
            warehouse[list(warehouse.keys())[0]]) > 0, allocations))
        return allocations
