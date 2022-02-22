import random


# zad1, zad4
def clear_input():
    user_input = input("What's your name?")
    user_input.strip()
    name = user_input.split(' ')[0]
    surname = user_input.split(' ')[1]
    print(f"Nazywasz się {name} {surname} - jak miło Cię poznać".format(name=name, surname=surname))


# zad2
def random_id():
    rand_id = random.randint(0, 99999)
    return str(rand_id).zfill(5)


# zad3
def zad3():
    user_input = input('podaj kolory')
    poz_niebieski = user_input.find('niebieski')
    if poz_niebieski == -1:
        print('nie ma niebieskiego')
    else:
        print('jest niebieski')


clear_input()
# print(random_id())
# zad3()


