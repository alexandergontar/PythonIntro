n = '22 * 300 - 14 + 10 * 10'

m = n.split()
m2 = []
m2 = m.copy()
print(m)      


def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b


# a = int(m[0])
# c = m[1]
# b = int(m[2])

result = int(m[0])
for i in range(1, len(m) - 1, 2):
         result = calc(result, int(m[i + 1]), m[i])
         print(result)

#for i in range(1, len(m) - 1, 2):
#   if m[i] == '*' or m[i] == '/':
#        result = calc(int(m[i - 1]), int(m[i + 1]), m[i])
#       m2.append(result)
#    else:
#        m2.append(m[i])
#        m2.append(int(m[i + 1]))
for i in range(1, len(m2) - 1, 2):
   if m2[i] == '*' or m2[i] == '/':
        result = calc(int(m2[i - 1]), int(m2[i + 1]), m2[i])
        m2[i-1]=' '
        m2[i]=str(result)
        m2[i+1]=' '
#new_str = ''
#for item in m2:
#   new_str += item

#print(m[i], m[i + 1])
print(m2)
#print(new_str)
m2 = list(filter(lambda a: a != ' ', m2))
print(m2)
result = int(m2[0])
for i in range(1, len(m2) - 1, 2):
         result = calc(result, int(m2[i + 1]), m2[i])
         print(result)
#print(result)



