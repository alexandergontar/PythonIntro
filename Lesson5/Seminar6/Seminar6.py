fileName = 'tel.txt' # файл с данными
# базовые функции
def writeFile(file_name, users):
    with open(file_name, 'w') as data:
        for user in users:
          data.write(user)


def readFile(file_name):
    result = []
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line)
    return result


def findUsers(userList, name):
    count = 0
    name = name.upper()
    i = int()  
    for i in range(len(userList)):      
         
         full_info = userList[i].split(',')
         if full_info[0].upper() == name or full_info[1].upper() == name or full_info[2].upper() == name:
             print(i+1, full_info[0],full_info[1],full_info[2],full_info[3], end = '' )
             count += 1
    if count == 0:
        print("такой пользователь не найден")

def find_by_phone(userList, phone):
    count = 0
    phone = phone.replace('+', '')
    i = int()  
    for i in range(len(userList)):         
         full_info = userList[i].split(',')         
         if full_info[3].replace('+', '') == phone+'\n':
             print(i+1, full_info[0],full_info[1],full_info[2],full_info[3], end = '' )
             count+=1
             break
    if count == 0:
        print('номер не найден')


users = readFile(fileName)
# операции меню пользователя
def add_user():    
        last_name = input("Фамилия: ")
        first_name = input("Имя: ")
        patronymic = input("Отчество: ")
        phone_number= input("Номер Телефона: ")
        user = last_name+','+first_name+','+patronymic+','+phone_number+'\n'        
        users.append(user)        
        writeFile(fileName, users)
        print("Добавлен пользователь: ", user)

def delete_user():
    i = int(input('Введите порядковый номер пользователя: '))
    print(users[i-1])
    usr =  users[i-1]
    users.remove(usr)    
    writeFile(fileName, users)

def edit_phone(userList, phone):
    count = 0
    phone = phone.replace('+', '')
    i = int()  
    for i in range(len(userList)):         
         full_info = userList[i].split(',')         
         if full_info[3].replace('+', '') == phone+'\n':
             print(i+1, full_info[0],full_info[1],full_info[2],full_info[3], end = '' )
             full_info[3] = input('Введите новый номер: ')
             user = full_info[0]+','+full_info[1]+','+full_info[2]+','+full_info[3]+'\n'
             users[i] = user
             writeFile(fileName, users)
             count +=1
             break
    if count == 0:
        print('номер не найден')
# создаем список операций (псевдо-switch)
ops = list()
def op1():
    print(' Полный список')
    result = readFile(fileName)
    for i in range(len(result)):
        print(i+1, '/', result[i].replace(',', ' '), end='')
def op2():
    print('Найти по имени, фамилии, или отчеству')
    findUsers(readFile(fileName), input('Введите имя, фамилию, или отчество: '))
def op3():
    print('Найти запись по телефону')
    find_by_phone(readFile(fileName), input('Введите номер телефона: '))
def op4():
    print('Добавить новый контакт')
    add_user()
def op5():
    print('Удалить контакт')
    delete_user()
def op6():
    print('Изменить номер телефона')
    edit_phone(readFile(fileName), input('Введите текущий номер телефона: '))
ops.append(op1)
ops.append(op2)
ops.append(op3)
ops.append(op4)
ops.append(op5)
ops.append(op6)
def do_op(op):
    op()
# UI
def display_operations():
    print('\nРабота с телефонным справочником')
    print('1 - Показать все записи')
    print('2 - Найти запись по вхождению частей имени')
    print('3 - Найти запись по телефону')
    print('4 - Добваить новый контакт')
    print('5 - Удалить контакт')
    print('6 - Изменить номер телефона')
    print('7 - Завершение работы')

display_operations()
while True:
    try:       
      n = int(input('введите номер операции (или 0 для справки): '))
      if n == 7:
          break
      if n == 0:
          display_operations()
          continue
      do_op(ops[n-1])
    except:
      print('неверный ввод')


