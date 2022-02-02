import math


def wartosc_lokaty_w_czasie(kwota, oprocentowanie, okres_inwestycji):
    wartosc = kwota * pow((1+oprocentowanie/100), okres_inwestycji)
    return wartosc

