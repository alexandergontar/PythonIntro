import os

def A_power_B(A, B):
    if (B == 1):
        return A
    if (B != 1):
        return A * A_power_B(A, B - 1)
while True:
    try:
      A = int(input("Введите число: "))
      B = int(input("Введите степень: "))
      break
    except:
        print('Неверный ввод')
print("Результат возведения в степень равен:", A_power_B(A, B))


input()