# Zadanie nr 1
# W ciągu 3 godzin biegu biegacz pokonał 38 kilometrów. Wyznacz średnią prędkość korzystając ze zmiennych.
# km = 38
# h = 3
# srednia = km/h
# print(f'Biegacz biegł z prędkością {srednia:.2f} km/h')
#
# lata = input('Ile masz lat koleżko/koleżanko?')
# mies = int(lata) * 12
# print(f'Masz więc ponad {mies} miesięcy.')

# Zad funkcja input 1
# kilometry = input('Ile kilometrów przeszedłeś w tym tygodniu?')
# obwod = 40075
# tygodnie = obwod/int(kilometry)
# print(f'Obejdziesz Ziemię w {tygodnie:.0f} tygodni!')
#
# Typ int oraz float, zadanie 1
# Napisz program, który zapyta użytkownika jaka jest cena jabłek w Biedronce, Lidlu i Żabce.
# Następnie wypisz informację: Ile kosztują najtańsze jabłka?

# biedr = input('Jaka jest cena jabłek w Biedronce?')
# lidl = input('cena w Lidlu: ')
# zaba = input('cena w Żabce: ')
#
# min_cena = min(float(biedr), float(lidl), float(zaba))
# print(f'Najniższa cena to {min_cena}')

# name = input('W jakim miescie mieszkasz?: ')
# print(name.capitalize())

# ford = "ab100100"
# audi = "EEE 123123"
# citroen = "Zk-300300"
# honda = "AB210210"
# names = [ford, audi, citroen, honda]
# for s in names:
#     first = s.upper().replace("-",'')
#     print(first.replace(' ',''))

# favourite_sports = ['tenis', 'pilka', 'siatka']
# print(favourite_sports)
# favourite_sports[0] = 'dupa'
# print(favourite_sports)
#
# lista = []
# potrawa = input('podaj ulubione potrawy')
# lista.append(potrawa)
# potrawa = input('podaj ulubione potrawy')
# lista.append(potrawa)
# potrawa = input('podaj ulubione potrawy')
# lista.append(potrawa)
# print(lista)

# nr = input('podaj nr tel: ')
# print(nr[:5] + (len(nr)-5) * '-')


#
# Stwórz i wypisz słownik, w którym kluczami będą różne przedmioty szkolne,
# a wartościami oceny uzyskane z tych przedmiotów.
#
# wyniki = {
#     'georgafia': 2,
#     'polski': 3,
#     'angielski': 5,
#     'niemiecki': 3
# }
# print(wyniki['georgafia'])

# Stwórz zmienną my_family zawierającą drzewo genealogiczne Twojej rodziny.
# Zacznij od siebie, opisując imię, nazwisko oraz datę urodzenia każdej osoby oraz jej rodziców.
# Podpowiedź: rodzice będą listami zawierającymi w sobie kolejne słowniki.

# my_family = [
#     {
#         'imię': 'michal',
#         'nazwisko': 'piesiewicz',
#         'wiek': 27
#     },
#     {
#         'imię': 'zbigniew',
#         'nazwisko': 'piesiewicz',
#         'wiek': 56
#     },
#     {
#         'imię': 'małgorzata',
#         'nazwisko': 'piesiewicz',
#         'wiek': 50
#     }
# ]
#

# Zapytaj użytkownika ile miesięcznie wydaje pieniędzy na:
# jedzenie
# rozrywkę
# opłaty
# inne
# Oblicz udział procentowy każdej kategorii w łącznych wydatkach.
# Następnie poproś użytkownika o wybór kategorii i wypisz jaki jest jej udział procentowy.

# print('Ile miesięcznie wydajesz na...')
# jedzenie = float(input('jedzenie: '))
# rozrywka = float(input('rozrywka'
#                        ' '))
# oplaty = float(input('oplaty'))
# inne = float(input('inne'))
# suma = sum([jedzenie, rozrywka, oplaty, inne])
# wydatki = {
#     'jedzenie': jedzenie/suma*100,
#     'rozrywka': rozrywka/suma*100,
#     'oplaty': oplaty/suma*100,
#     'inne': inne/suma*100
# }
# kategoria = input('wybierz kategorię')
# print(f'Na {kategoria} wydajesz {wydatki[kategoria]:.2f}%')

# oceny = input('wypisz po przecinku swoje oceny z: matematyki, polskiego, geografii, angielskiego').split(',')
# oceny_lista = list(map(int, oceny))
# if 1 in oceny_lista:
#     print('nie zdałeś, popraw lache')
# else:
#     srednia = sum(oceny_lista)/len(oceny_lista)
#     if srednia >= 3.5:
#         print('zdałeś.')
#     else:
#         print('nie zdałeś')
#         print(f'srednia {srednia}')
#
#
# imie = input('podaj imię: ')
# if imie[-1] == 'a':
#     print(f'witaj kobieto {imie[:-1]}o.')
# else:
#     print(f'witaj gościu')

# decyzja = input('chcesz obliczyć kredyt czy wartość w czasie na lokacie? (1 lub 2)')
# if decyzja == '1':
#     kwota_kredytu = float(input('kwota kredytu'))
#     oproc_kredytu = float(input('oprocentowanie kredytu'))
#     wklad = float(input('wartość wkładu własnego'))
#     lata = int(input('czas kredytowania w latach'))
#     przychod_mies = float(input('przychod miesieczny'))
#     wydatki = float(input('miesieczne wydatki'))
#
#     rata = (kwota_kredytu * oproc_kredytu/100) / 12 + kwota_kredytu  / (lata * 12)
#     dostepne_srodki = przychod_mies - wydatki
#     wartosc_nieruchomosci = kwota_kredytu+wklad
#
#     print(f'rata: {rata}')
#     print(f'dostepne srodki: {dostepne_srodki}')
#     print(f'wartosc nieruchomosci: {wartosc_nieruchomosci}')
#
#     procent_wkladu = wklad/wartosc_nieruchomosci
#     pozostale_srodki = dostepne_srodki - rata
#
#     if procent_wkladu > 0.2 and pozostale_srodki >= 1000:
#         print('możesz wziąć kredyt.')
#     elif 0.1 <= procent_wkladu <= 0.2 and pozostale_srodki >= 2000:
#         print('spelniasz drugi warunek, możesz wziąć kredyt.')
#     elif procent_wkladu < 0.1:
#         print('warunek 3, nie możesz wziąć kredytu.')
#     else:
#         print('4.: nie możesz wziąć kredytu.')
# elif decyzja == '2':
#     pocz = input('Ile chcesz włożyć na lokatę: ')
#     proc = input('Jakie jest oprocentowanie roczne (%): ')
#     lata = input('Na ile lat chcesz włożyć piniądz: ')
#
#     wartosc = float(pocz) * (1 + float(proc)/100) ** float(lata)
#     print(f'Będziesz miał/a tyle: {wartosc:.2f} zł.')
# else:
#     print('wybierz opcję 1 lub 2.')

# wiek = int(input('podaj swoj wiek'))
#
# if wiek < 20 or wiek > 30:
#     print('jesteś za stary lub za młody na test coopera.')
# else:
#     plec = input('podaj plec')
#     wynik = float(input('podaj wynik'))
#     if plec == 'M':
#         if wynik < 1600:
#             print('bardzo źle.')
#         elif wynik < 2199:
#             print('źle')
#         elif wynik < 2399:
#             print('średnio')
#         elif wynik < 2800:
#             print('dobrze.')
#         else:
#             print('bardzo dobrze!')
#     elif plec == 'K':
#         if wynik < 1500:
#             print('bardzo źle.')
#         elif wynik < 1799:
#             print('źle')
#         elif wynik < 2199:
#             print('średnio')
#         elif wynik < 2700:
#             print('dobrze.')
#         else:
#             print('bardzo dobrze!')
#     else:
#         print('podaj wlasciwą plec (M/K)')
#
# zakupy = input('podaj listę zakupów, rozdziel przecinkami.:').split(',')
# if 'chleb' in zakupy or 'bułki' in zakupy:
#     print('pieczywo jest na liście')
# else:
#     print('zapomniałeś o pieczywie!')
# numer = input('podaj nr telefonu')
# numer = map(int, list(numer))
# if 0 in numer:
#     print('mamy zero w numerze')
# else:
#     print('w numerze nie ma zera.')

# value = None
#
# if value is True:
#     print('value is True')
# elif value is False:
#     print('value is False')
# elif value is None:
#     print('value is None')
# else:
#     print('value is different')
#

# proba = 1
# liczba = int(input('podaj liczbę parzystą'))
# while liczba % 2 != 0 and proba < 10:
#     print('liczba nie jest liczbą parzystą')
#     liczba = int(input('podaj liczbę parzystą'))
#     proba += 1

# dania = input('wypisz swoje ulubione dania, rozdzielając je przecinkiem').split(',')
# index = 0
# while index < len(dania):
#     print(f'{dania[index]} zajmuje miejsce {index+1}')
# #     index += 1
# print('program do wyliczania sredniej. wpisz X by zakończyć.')
# lista_ocen = []
# ocena = 0
# while ocena != 'X':
#     ocena = input('wprowadź ocenę')
#     if ocena != 'X':
#         lista_ocen.append(int(ocena))
#         print(f'średnia: {sum(lista_ocen)/len(lista_ocen)}')
# srednia = 0
# for i in lista_ocen:
#     srednia += i
# srednia = srednia/len(lista_ocen)
# print(f'srednia obliczona petla for to {srednia}')


# telefon = input('podaj numer telefonu')
# telefon_format: str = ''
# index = 0
# while index < len(telefon):
#     if index != 0 and index % 2 == 0:
#         telefon_format += '-'
#     telefon_format += telefon[index]
#     index += 1
# print(telefon_format)

# telefon = input('podaj numer telefonu')
# telefon_format: str = ''
# for i, cyfra in enumerate(telefon):
#     if i % 2 == 0 and i != 0:
#         telefon_format += '-'
#     telefon_format += cyfra
# print(telefon_format)
#
# wydatki = []
# wydatki_dict = {}
# kategoria = ''
# kwota = ''
# print('0,0 zamyka program.')
# while '0' not in kategoria:
#     kategoria, kwota = input('wpisz kategorie wydatków oraz wydatek po przecinku').split(',')
#     if kategoria != '0' or kwota != 0:
#         wydatki_dict[kategoria] = float(kwota)
# suma = sum(wydatki_dict.values())
# # print('suma:', suma)
# # for index, (wydatek, kwota) in enumerate(wydatki_dict.items()):
# #     print(f'{index} kategoria: {wydatek}, suma: {kwota} udział: {kwota / suma * 100:.1f}%')
# print(f'najwiecej wydajesz miesiecznie na {max(wydatki_dict, key=wydatki_dict.get)}')
# print(wydatki_dict.get)

# telefon = input('podaj nr telefonu')
# for i in telefon:
#     print(f'{i} występuje {telefon.count(i)}')
#
# kwota = float(input('podaj kwotę kredytu'))
# procent = float(input('podaj oprocentowanie'))
# lata = int(input('podaj lata kredytu'))
# koszty = float(input('podaj koszty poczatkowe'))
#
# credit_time_in_months = lata*12
# monthly_paid_capital = kwota/credit_time_in_months
# total_paid = koszty
# for month in range(1, credit_time_in_months+1):
#     capital_to_be_paid = kwota - (month-1) * monthly_paid_capital
#     installment = (capital_to_be_paid*procent/100)/12 + monthly_paid_capital
#     total_paid += installment
#     print(f'Rata w miesiacu {month} wyniesie {installment}')
# print(f'zaciągając kredyt na tych warunkach spłacisz z odsetkami {total_paid}')
#
# oceny = input('wypisz po przecinku swoje oceny z: matematyki, polskiego, geografii, angielskiego').split(',')
# oceny_lista = list(map(int, oceny))
# x = 1
# for i in oceny_lista:
#     if i == 1:
#         print('klasę trzeba powtórzyć')
#         x = 0
#         break
# if x == 1:
#     print('gratulacje!')

#
# wydatki_dict = {}
# kategoria = ''
# kwota = ''
# print('0,0 zamyka program.')
# while True:
#     kategoria, kwota = input('wpisz kategorie wydatków oraz wydatek po przecinku').split(',')
#     if kategoria == '0' or kwota == 0:
#         break
#     wydatki_dict[kategoria] = float(kwota)
# suma = sum(wydatki_dict.values())
# print('suma:', suma)
# for index, (wydatek, kwota) in enumerate(wydatki_dict.items()):
#     print(f'{index} kategoria: {wydatek}, suma: {kwota} udział: {kwota / suma * 100:.1f}%')
# print(f'najwiecej wydajesz miesiecznie na {max(wydatki_dict, key=wydatki_dict.get)}')

# lista = [1,2,3,4,5,6,7,8,9,10,11]
# for i in lista:
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

def pole_pow_prostokata(a, b):
    return a*b


# print(pole_pow_prostokata(8, 3))

def srednia_predkosc(km, h):
    return km/h


# km = 10
# czas_samochod = 0.2
# czas_bieg = 1.2
# czas_rower = 0.5
# print(f'średnia prędkość jazdy samochodem to {srednia_predkosc(km=km, h=czas_samochod):.1f} km/h')
# print(f'średnia prędkość biegu to {srednia_predkosc(km, czas_bieg):.1f}km/h')
# print(f'średnia prędkość jazdy rowerem to {srednia_predkosc(km, czas_rower):.1f}km/h')
#

def double_input():
    kategoria, kwota = input('wpisz kategorie wydatków oraz wydatek po przecinku').split(',')
    return kategoria, kwota


def wypisz_wydatki(wydatki_dict):
    suma = sum(wydatki_dict.values())
    for wydatek, kwota in wydatki_dict.items():
        print(f'kategoria: {wydatek}, suma: {kwota} udział: {kwota / suma * 100:.1f}%')


def klucz_o_najwiekszej_wartosci(dict):
    return max(wydatki_dict, key=wydatki_dict.get)


# wydatki_dict = {}
#
# print('0,0 zamyka program.')
# while True:
#     kategoria, kwota = double_input()
#     if kategoria == '0' or kwota == 0:
#         break
#     wydatki_dict[kategoria] = float(kwota)
#
# wypisz_wydatki(wydatki_dict)
# print(f'najwiecej wydajesz miesiecznie na {klucz_o_najwiekszej_wartosci(wydatki_dict)}')
#

def range10(num, num_range=10):
    output = []
    output.append(num*(1-num_range)/100)
    output.append(num*(1+num_range)/100)
    return output
#
#
# inpt = 20
#
# ranger = range10(inpt)
#
# print(range10(inpt, 20))
# print(f'dla wartości {inpt}, range to {range10(inpt)} ')


def dodaj_osobe(imiona, zapisane_osoby=None):
    if zapisane_osoby is None:
        zapisane_osoby = []
    for i in imiona.split(','):
        zapisane_osoby.append(i)
    return zapisane_osoby

imiona = 'marek,jacek'
juz_obecne = ['lukasz', 'michal']
wynik = dodaj_osobe(imiona, zapisane_osoby=juz_obecne)
print(wynik)