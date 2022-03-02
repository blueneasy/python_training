from products import Product


def test_product_comparison():
    parameters = [
        (1, 'Jabłko', 'Food', 4, 1, 'Jabłko', 'Food', 4, True),
        (1, 'Jabłko', 'Food', 4, 1, 'Gruszka', 'Food', 4, False),
        (1, 'Jabłko', 'Food', 4, 1, 'Jabłko', 'Misc', 4, False),
        (1, 'Jabłko', 'Food', 4, 1, 'Jabłko', 'Food', 8, False),
    ]

    for params in parameters:
        id, name, category, price, other_id, other_name, other_category, other_price, expected_result = params
        result = Product(id, name, category, price) == Product(other_id, other_name, other_category, other_price)
        if result == expected_result:
            print('OK')
        else:
            print(f'Błąd! Dla danych {params} wynik porównywania jest {params} a powinien być {expected_result}')


def run_test():
    test_product_comparison()


run_test()