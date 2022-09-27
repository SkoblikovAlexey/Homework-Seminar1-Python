# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

import random
x = [False, True]
y = [False, True]
z = [False, True]

# a = random.randint(0,1)
# b = random.randint(0,1)
# c = random.randint(0,1)
trigger = True
for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            if not(x or y or z) != (not x and not y and not z):
                 print("Утверждение не истинно для всех значений предикат")
                 trigger = False
                 break            
if trigger: print("Утверждение истинно для всех значений предикат")
