from sklep.zamowienia import dodaj_zamowienie, zamowienia
from sklep.produkty import lista_produktow, aktualizuj_magazyn

def wprowadz_zamowienie():
    produkt = input('Co chciałbyś zamówić?')
    ilosc = int(input('Ile jednostek zamówić?'))
    return produkt, ilosc


def run():
    produkt, ilosc = wprowadz_zamowienie()
    wartosc_zamowienia = dodaj_zamowienie(produkt, ilosc)
    if wartosc_zamowienia is not None:
        print(f'lista zamowien: {zamowienia}')
        print(f'stan magazynu: {lista_produktow}')
        print(f'Dziekujemy za zakup. Wartosc zamowienia to: {wartosc_zamowienia}')


if __name__ == "__main__":
    run()


