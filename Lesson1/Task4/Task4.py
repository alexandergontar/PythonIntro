import os

print('Делим шоколадку на дольки по прямой')

m = int(input('Введите размер по вертикали - m: '))
n = int(input('Введите размер по горизонтали - n: '))
s = m * n
print(f'Вcего долек s = {s}')
k = int(input(f'Введите число k >= 1, но < {s}: '))    
if k < s and (k % m == 0 or k % n == 0):
    print('делится')
else:
    print('не делится')
if k >= s:
    print('k должно быть меньше s !')