import os
import random
list_m = []
list_n = []
output_set = set()
m = 0
n = 0
while True:
  try: 
      m = int(input('Введите длину первого ряда m: '))
      n = int(input('Введите длину второго ряда n: '))
      break
  except:
      print('неверный ввод')
for i in range(1, m):
   list_m.append(random.randint(1, 10))
for i in range(1, n):
   list_n.append(random.randint(1, 10))
print(list_m)
print(list_n)
for j in list_m:
    for k in list_n:
        if j == k:
            print(k)
            output_set.add(j)
print(output_set)
input()
