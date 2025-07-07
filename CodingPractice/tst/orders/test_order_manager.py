import unittest
from src.orders.order_manager import OrderManager, Order

class TestOrderManager(unittest.TestCase):
    def test_consolidate_basic(self):
        orders = [
            {"id": 1, "quantity": 3},
            {"id": 2, "quantity": 5},
            {"id": 1, "quantity": 2},
        ]
        result = OrderManager.consolidate_orders(orders)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].quantity, 5)
        self.assertEqual(result[1].id, 2)
        self.assertEqual(result[1].quantity, 5)

    def test_consolidate_empty(self):
        orders = []
        result = OrderManager.consolidate_orders(orders)
        self.assertEqual(result, [])

    def test_consolidate_single_order(self):
        orders = [{"id": 10, "quantity": 7}]
        result = OrderManager.consolidate_orders(orders)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 10)
        self.assertEqual(result[0].quantity, 7)

    def test_consolidate_multiple_ids(self):
        orders = [
            {"id": 3, "quantity": 1},
            {"id": 2, "quantity": 2},
            {"id": 3, "quantity": 4},
            {"id": 1, "quantity": 5},
        ]
        result = OrderManager.consolidate_orders(orders)
        self.assertEqual([o.id for o in result], [1,2,3])
        self.assertEqual([o.quantity for o in result], [5,2,5])

    def test_top_k_orders_basic(self):
        orders = [
            {"id": 1, "quantity": 3},
            {"id": 2, "quantity": 5},
            {"id": 1, "quantity": 2},
            {"id": 3, "quantity": 5},
        ]
        result = OrderManager.top_k_orders(orders, 2)
        self.assertEqual(result, [
            {"id": 1, "quantity": 5},
            {"id": 2, "quantity": 5}
        ])

    def test_top_k_orders_tie(self):
        orders = [
            {"id": 2, "quantity": 5},
            {"id": 1, "quantity": 5},
            {"id": 3, "quantity": 2},
        ]
        result = OrderManager.top_k_orders(orders, 2)
        self.assertEqual(result, [
            {"id": 1, "quantity": 5},
            {"id": 2, "quantity": 5}
        ])

    def test_top_k_orders_less_than_k(self):
        orders = [
            {"id": 1, "quantity": 2},
            {"id": 2, "quantity": 3},
        ]
        result = OrderManager.top_k_orders(orders, 5)
        self.assertEqual(result, [
            {"id": 2, "quantity": 3},
            {"id": 1, "quantity": 2}
        ])

if __name__ == "__main__":
    unittest.main()
