# zad1
import random

lista_1 = [i for i in range(30) if i % 3 == 0]
lista_2= [i for i in range(30) if i % 5 == 0]

print(lista_1)
print(lista_2)

lista_3 = lista_1 + lista_2
print(lista_3)

user_input = input('wypisz listę ulubionych sportów')
lista = user_input.split(',')
print(lista[1::2])

lista = [random.randint(1,100) for x in range(10000)]
print(lista)