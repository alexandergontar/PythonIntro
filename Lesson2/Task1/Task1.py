import random

coins = []
N = 0
while True:
   try:
       N = int(input('Введите нечетное количество вбрасываемых монеток N = '))
       break
   except:
       print('неверный ввод')
if N % 2 == 0:
    N+=1
    print(f'коррекция до ближайшего нечетного, N = {N}')
for i in range(0,N):
    coins.append(random.randint(0,1))
print(coins)
heads = 0
tails = 0
for coin in coins:
    if coin == 1:
      heads += 1
      print('орел', end = ' ')
    else:
      tails += 1
      print('решка', end = ' ')
print(f'\nОрлов = {heads}, Решек = {tails}')
if heads < tails:
    print(f'Перевернуть {heads} монеты со стороной\' орел\'')
else:
    print(f'Перевернуть {tails} монеты со стороной\' решка\'')
input()