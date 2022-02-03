lista_produktow = {
                        'jablka': {
                                'ilosc': 143,
                                'cena': 0.26
                        },
                        'maka': {
                                'ilosc': 82,
                                'cena': 1.2
                        },
                        'chleb': {
                                'ilosc': 20,
                                'cena': 7.47
                        }
                    }


def cena_dla_produktu(produkt):
    return lista_produktow[produkt]['cena']


def aktualizuj_magazyn(produkt, zamowiona_ilosc):
    lista_produktow[produkt]['ilosc'] -= zamowiona_ilosc

print("cos")