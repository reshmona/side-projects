from .order import Order
from typing import List, Dict


class OrderManager:
    @staticmethod
    def _aggregate_orders(orders: List[Dict]) -> Dict:
        """
        Helper to aggregate quantities by id.
        """
        order_map = {}
        for order in orders:
            oid = order["id"]
            qty = order["quantity"]
            if oid in order_map:
                order_map[oid] += qty
            else:
                order_map[oid] = qty
        return order_map

    @staticmethod
    def consolidate_orders(orders: List[Dict]) -> List[Order]:
        """
        Consolidate orders by id, summing quantities, and return sorted list of Order objects.
        """
        order_map = OrderManager._aggregate_orders(orders)
        result = [Order(order_id, qty) for order_id, qty in order_map.items()]
        result.sort(key=lambda o: o.id)
        return result

    @staticmethod
    def top_k_orders(orders: List[Dict], k: int) -> List[Dict]:
        """
        Return the top k most ordered products by total quantity, descending. If tie, sort by id ascending.
        """
        order_map = OrderManager._aggregate_orders(orders)
        sorted_orders = sorted(order_map.items(), key=lambda x: (-x[1], x[0]))
        return [{"id": oid, "quantity": qty} for oid, qty in sorted_orders[:k]]
