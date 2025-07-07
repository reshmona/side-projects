class Order:
    def __init__(self, order_id, quantity):
        self.id = order_id
        self.quantity = quantity

    def __repr__(self):
        return f"Order(id={self.id}, quantity={self.quantity})"
