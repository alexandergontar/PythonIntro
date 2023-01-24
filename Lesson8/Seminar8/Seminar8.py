def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b

def calc_no_priorities(m : []):
     result = int(m[0])
     for i in range(1, len(m) - 1, 2):
         result = calc(result, int(m[i + 1]), m[i])         
     return result
 
def calc_priorities(m : []):
     for i in range(1, len(m) - 1, 2):
       if m[i] == '*' or m[i] == '/':
        result = calc(int(m[i - 1]), int(m[i + 1]), m[i])
        m[i-1]=' '
        m[i]=str(result)
        m[i+1]=' '         
     m = list(filter(lambda a: a != ' ', m))     
     return m

def calc_line_no_brackets(expression : str()):
    array = expression.split()
    print(array)
    array_copy = array.copy()
    mm = calc_priorities(array)
    print(mm)
    for field in array_copy:
      print(field, end = ' ')
    result = calc_no_priorities(mm)
    print('=', result) 
    return result

n = '22 * 300 - 14 + 10 * 10'
result = calc_line_no_brackets(n)
print(result)




