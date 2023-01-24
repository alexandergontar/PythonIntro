def calc(a, b, op): # элементарные операции
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '/':
        return a / b
    elif op == '*':
        return a * b

def calc_no_priorities(m : []): # вычисление строки без приоритетов
     result = float(m[0])
     for i in range(1, len(m) - 1, 2):
         result = calc(result, float(m[i + 1]), m[i])         
     return result
 

def calc_priority(m : []): # вычисление и удаление одной приоритетной операции
     for i in range(1, len(m) - 1, 2):
       if m[i] == '*' or m[i] == '/':
        result = calc(float(m[i - 1]), float(m[i + 1]), m[i])
        m[i-1]=' '
        m[i]=str(result)
        m[i+1]=' '         
        m = list(filter(lambda a: a != ' ', m))     
        return m
def calc_replace_priorities(m : []): # замены всех приоритетный операций их резултатами
    while '*' in m or '/' in m:
       m = calc_priority(m)
    return m

def convert(n : str()): # формирует нужный массив из строки
    lst = []
    temp =''
    for item in n:      
      if item.isdigit():
         temp += item
      elif item =='*' or item == '/' or item == '+' or item == '-':
        if len(temp) > 0:
           lst.append(temp)
           temp = ''
           lst.append(item)
    if len(temp) > 0:
      lst.append(temp)
      temp = ''
    return lst

def calc_line_no_brackets(expression : str()): # вычисление простой строки, без скобок
    lst = []
    lst = convert(expression)  
    array_copy = lst.copy()     
    mm = calc_replace_priorities(lst)    
    for field in array_copy:
      print(field, end = ' ')
    result = calc_no_priorities(mm)
    print('=', result) 
    return result

# примеры ввода
#n = '22 * 300 - 14 + 10 * 10' # аккуратный пользователь
#n = '  22* ,300-14 ;+  10* 10 _' # дрож в руках
#n = '10 + 40 / 5 - 5' # все хорошо
n = ' 10 ;*  5/2 ,+ 10/ 2 - 15_' # что-то не то ...

result = calc_line_no_brackets(n)
print('Результат: ',int(result))




