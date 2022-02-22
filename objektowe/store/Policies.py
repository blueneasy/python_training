
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


class DiscountPolicy:

    @staticmethod
    def apply_discount(order_value):
        return order_value


class PercentageDiscount(DiscountPolicy):
    def __init__(self, percentage_discount):
        super().__init__()
        self.percentage_discount = percentage_discount

    def apply_discount(self, order_value):
        return order_value * (1-self.percentage_discount/100)


class AbsoluteDiscount(DiscountPolicy):
    def __init__(self, absolute_discount):
        super().__init__()
        self.absolute_discount = absolute_discount

    def apply_discount(self, order_value):
        discounted_value = order_value - self.absolute_discount
        if discounted_value < 0:
            return 0
        else:
            return discounted_value


prc_10 = PercentageDiscount(10)
abs_100 = AbsoluteDiscount(100)