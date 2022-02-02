from pack.exp import srednia
import math
import calculations.calc

x = srednia(20, 2)
print(x)


def dlugosc_przeciwprostokatnej(a, b):
    return math.sqrt((pow(a, 2)) + (pow(b, 2)))


print(dlugosc_przeciwprostokatnej(10, 12))


def float_input(text):
    answer = float(input(text))
    return answer


poczatkowy_kapital = float_input('wpisz wartosc poczatkowego kapitalu')
oprocentowanie = float_input('jakie oprocentowanie (%)')
okres_trwania_inwestycji = float_input('lata trwania inwestycji')

print(calculations.calc.wartosc_lokaty_w_czasie(poczatkowy_kapital, oprocentowanie, okres_trwania_inwestycji))