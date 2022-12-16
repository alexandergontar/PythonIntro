import os

upper_bound = 0
while True:
   try:
       upper_bound = int(input('Введите верхнюю границу значений N = '))
       break
   except:
       print('неверный ввод')
n = 0
current_value = 0
while current_value <= upper_bound - current_value:
    current_value = 2 ** n
    print(current_value, end = ' ')
    n+=1
input()