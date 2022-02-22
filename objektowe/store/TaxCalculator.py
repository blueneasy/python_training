
class TaxCalculator:
    TAX_RATES = {
        'Fruit': 0.05,
        'Veggie': 0.05,
        'Food': 0.08
    }
    BASE_TAX_RATE = 0.2

    @staticmethod
    def tax_element(order_element):
        product_category = order_element.product.category
        if product_category in TaxCalculator.TAX_RATES:
            tax_rate = TaxCalculator.TAX_RATES[product_category]
        else:
            tax_rate = TaxCalculator.BASE_TAX_RATE
        return tax_rate * order_element.element_price

    @staticmethod
    def tax_order(order):
        for element in order._order_elements:
            if element.product.category in TaxCalculator.TAX_RATES:
                print(element.element_price * TaxCalculator.TAX_RATES[element.product.category])
            else:
                print(element.element_price * TaxCalculator.BASE_TAX_RATE)
