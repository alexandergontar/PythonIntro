import os
N = int(input(" Введите трехзначное число: "))
summ = 0
while(N>0):
    summ += N%10
    N = N//10
print(f' Cумма цифр в числе = {summ}')