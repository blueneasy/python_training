from .produkty import lista_produktow, aktualizuj_magazyn

zamowienia = [
    {
        'produkt': 'chleb',
        'ilosc': 20,
        'wartosc_zamowienia': 149.4
    }
]

def dodaj_zamowienie(produkt, ilosc):
    cena = lista_produktow[produkt]['cena']
    dostepna_ilosc = lista_produktow[produkt]['ilosc']

    if dostepna_ilosc < ilosc:
        print(f'Na stanie mamy niewystarczajaca ilosc sztuk produktu {produkt}')
        print('Nie zrealizowano zamowienia')
        return None

    wartosc_zamowienia = cena*ilosc
    nowe_zamowienie = {
        'produkt': produkt,
        'ilosc': ilosc,
        'wartosc_zamowienia': wartosc_zamowienia
    }
    aktualizuj_magazyn(produkt, ilosc)
    zamowienia.append(nowe_zamowienie)
    return wartosc_zamowienia
