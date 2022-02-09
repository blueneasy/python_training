
class Policies:

    @staticmethod
    def default_policy(order_price):
        return order_price

    @staticmethod
    def loyal_customer_policy(order_price):
        return order_price * 0.95

    @staticmethod
    def christmas_policy(order_price):
        if order_price > 100:
            return order_price - 20
