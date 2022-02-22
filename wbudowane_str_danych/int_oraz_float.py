"""

Wylosuj 6 liczb typu float z przedziału od -20 do 20 oraz 3 liczby całkowite z przedziału od 1 do 10.

Następnie na pierwszych trzech liczbach typu float zastosuj zaokrąglanie (kolejno round, ceil oraz floor).

Kolejne trzy liczby typu float podnieś do potęgi o wartości odpowiednio pierwszej, drugiej i trzeciej wylosowanej
liczby całkowitej.

"""

import random
import math


rand_float1 = random.uniform(-20, 20)
rand_float2 = random.uniform(-20, 20)
rand_float3 = random.uniform(-20, 20)
rand_float4 = random.uniform(-20, 20)
rand_float5 = random.uniform(-20, 20)
rand_float6 = random.uniform(-20, 20)

rand_int1 = random.randint(1, 10)
rand_int2 = random.randint(1, 10)
rand_int3 = random.randint(1, 10)

rounded1 = round(rand_float1)
rounded2 = math.floor(rand_float2)
rounded3 = math.ceil(rand_float3)

print(rand_float4 ** rand_int1)
print(pow(rand_float5, rand_int2))
print(math.pow(rand_float6, rand_int3))
