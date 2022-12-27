from random import randint
from os import system


berries = [] # Список кол-ва ягод по кустам
bushes = randint(4,9) # Генерируем кол-во кустов
print(f'На грядке  в фермерском хозяйстве растут  кусты с черникой, их : {bushes} шт.\n')

for i in range(1, bushes + 1):
    berris_i =randint(1,9) # Генерируем кол-во ягод на i-том кусте
    print(f'\t На {i} кусте черники выросло ягод :{berris_i} шт.')
    berries.append(berris_i)  

max_summa_berries = index = 0
i = 0
while(i < bushes ):
    if(berries[i -2] + berries[i -1] + berries[i] > max_summa_berries) : 
        max_summa_berries = berries[i -2] + berries[i -1] + berries[i] # Определяем макс. число собираемых ягод за раз
        index = i # Номер куста напротив которого собрано макс. кол-во ягод
    i +=1
    
print(f'\nМаксимальное количества ягод ( {max_summa_berries} шт. ) сборочный модуль собрал напротив куста номер {index}\n')
