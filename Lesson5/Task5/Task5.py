import os

def A_plus_B(A, B):
    if A == 0:
        return B
    if A != 0:
        return A_plus_B(A-1, B+1)
while True:
    try:
      A = int(input("Введите число A: "))
      B = int(input("Введите число В: "))
      break
    except:
      print('Неверный ввод')
print('\nA + B = ',A_plus_B(A, B))