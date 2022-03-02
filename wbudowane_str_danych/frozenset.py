import random


# def my_function(numbers):
#     x = random.randint(0, 10)
#     print(f'added: {x}')
#     numbers.add(x)
#     return numbers
#
# numbers = set()
# goal = set(x for x in range(10))
# counter = 0
# print(goal)
# while not goal.issubset(numbers):
#     print('set: ', numbers)
#     my_function(numbers)
#     counter += 1
#
# print(numbers)
# print('end', counter)

def my_function(numbers):
    x = random.randint(0, 10)
    xset = frozenset({x})
    print(f'added: {x}')
    numbers.union(xset)
    return numbers

numbers = set()
goal = set(x for x in range(10))
counter = 0
print(goal)
while not goal.issubset(numbers):
    print('set: ', numbers)
    numbers = my_function(numbers)
    counter += 1

print(numbers)
print('end', counter)
