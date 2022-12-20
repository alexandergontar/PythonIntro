import os
import random
N=0
X=0
while True:
  try: 
      N = int(input('Введите размер массива N = '))
      X = int(input(f'Введите число X от 1 до {N//2}, X = '))
      break
  except:
      print('неверный ввод')

l = []
for i in range(1, N + 1):
    l.append(random.randint(1, N//2 + 1))
print(l)
count = 0
for item in l:
    if item == X:
        count += 1
print(f' Число {X} встретилось {count} раз')