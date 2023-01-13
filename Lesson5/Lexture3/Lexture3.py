import os
import re
#def f(x):
#    return x**2
#g = f
#print(type(g))
#print(g(2))
#print(f(2))

print('========lambdas========')
def calc1(x):
    return x + 10
def calc2(x):
    return x*10
def math(op, x):
   print(op(x))
math(calc1, 10)
math(calc2, 10)

def sum(x, y):
    return x + y
def mult(x, y):
    return x*y
def calc(op, a, b):
    print(op(a, b))
    return op(a, b)
calc(sum, 2, 3)
print(calc(mult, 2, 3))
f = sum
calc(f, 4, 5)
f = lambda q, w : q + w
calc(f, 6, 7)
power = lambda a, b: a**b
calc(power, 2, 3)
calc(lambda a, b: a*b, 5, 5)
print('======= comprehensive lists ============')
lst = []
for i in range(1, 101):
    if i % 2 == 0:
        lst.append(i)
print(lst)
def F(x):
    return x**3
def kv(x):
    return x*x
#lst = [(i, i) for i in range(1, 21) if i % 2 == 0]
lst = [(i,F(i)) for i in range(1, 21) if i % 2 == 0]
print(lst)
#задача
file = open('data.txt', 'r')
data = file.read() + ' '
file.close()
print(data)
numbers = []
while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos + 1:]
print(numbers)
#lst = [1,2,3,5,8,15,23,38]
# решение 1  
lst = [(i, kv(i)) for i in numbers if i % 2 == 0]
print(lst)
# решение 2
def select(f, col):
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
res = select(int, data)
print(res)
res = where(lambda x: not x%2, res)
print(res)
res = select(lambda x: (x, x**2), res)
print(res)
print("========== map =============")
li = [x for x in range(1, 20)]
print(li)
li = list(map(lambda x: x+10, li))
print(li)
data = list(map(int, input('Введите целые числа через пробел: ').split()))
print(data)
print('========= filter ===============')
data = [x for x in range(10)]
print(data)
res = list(filter(lambda x: x % 2 == 0, data))
print(res)
print('========= zip ===============')
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [1, 3, 7, 14, 19]
print(users)
print(ids)
data = list(zip(users, ids))
print(data)
salary = [111, 222, 333]
print(salary)
data = list(zip(users, ids, salary)) # по соединит по минимальному
print(data)
print('========= enumerate ==========')
print(users)
data = list(enumerate(users))
print(data)
input()
