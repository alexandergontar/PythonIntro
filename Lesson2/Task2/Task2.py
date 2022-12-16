import os
print('s = x + y, p = x * y')
while True:
    try:
        s = int(input('Введите сумму s = '))
        p = int(input('Введите произведение р = '))
        break
    except:
        print('неверный ввод, повторите')
not_found = True
for i in range(2, 1000):
    for j in range(2, 1000):
         if i + j == s and i * j == p:         
            print(f'x = {i}, y = {j}')
            not_found = False
            break
if not_found:
    print('не подобрать таких x, y ...')
input()
