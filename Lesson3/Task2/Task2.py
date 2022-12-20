import os
import random
def safe_input(message):    
    X = 0
    while True:
        try:
          X = int(input(message))
          return X
                    
        except:
          print('неверный ввод')


N = safe_input('Введите размер массива N = ')
X = safe_input(f'Введите число  X = ')
l = []
for i in range(1, N + 1):
    l.append(random.randint(1, N//2 + 1))
print(l)
deltas = []
for i in range(0, len(l)):
    delta = X - l[i]
    if delta < 0:
        delta = -delta
    #if delta != 0:
    deltas.append(delta)

i_min = 0
i_mins = []
i_mins.append(i_min)
closest = deltas[0]
for i in range(1, len(deltas)):
    if deltas[i] < closest:
        i_mins.clear()
        closest = deltas[i]
        i_min = i
        i_mins.append(i_min)
    elif deltas[i] == closest:
        i_mins.append(i)

print(f'Наиближайшие из масчива числа к {X}:')
min = 100000
for i in i_mins:
    print(f"l[{i}] = {l[i]}")
    if l[i] < min:          
       min = l[i]
print(f"Наименьшее из них: {min}")