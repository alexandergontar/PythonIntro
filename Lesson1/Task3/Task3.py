import os
import sys
ticket = list(map(int, input('Введите 6-значное число: ')))
while len(ticket) != 6:
    print('число должно быть 6-значным!')
    ticket = list(map(int, input('Введите 6-значное число: ')))
print('Цифры билета')
for d in ticket:
    print(d, end = ' ')
print()
if ticket[0] + ticket[1] + ticket[2] == ticket[3] + ticket[4] + ticket[5]:
     print('Билет счастливый')
else:
      print('Билет обычный')