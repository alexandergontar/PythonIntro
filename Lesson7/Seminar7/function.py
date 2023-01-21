def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result

def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_list +'\n')

def save_as_csv(file_name, lines):
    with open(file_name, 'w', encoding='utf8') as data:
        for line in lines:
            col=0
            for col in range(len(line)-1):
                data.write(line[col]+',')
            data.write(line[len(line)-1]+'\n')

def get_buses():
    return read_data_from_file('bus.txt')
def get_drivers():
    return read_data_from_file('driver.csv')
def get_routes():
    return read_data_from_file('route.txt')

def get_lists():
    pathes = ['bus.txt', 'driver.csv', 'route.txt']
    try:
        n = int(input('Выберите список - (1 - автобусы, 2 - водители, 3 - маршруты): ')) - 1
        path = pathes[n]
    except:
        print('ошибка ввода')
        return []
    return  read_data_from_file(path)

def find_by_id(lines : list(), id):      
       count = 0
       for line in lines:
           if line[0] == id:
               count+=1
               return line
       if count == 0:           
           return None 
       else:
           return line

def delete(lines : list(), path, id):
    item = find_by_id(lines, id)
    if item != None:
        lines.remove(item)
        save_as_csv(path, lines)
    else:
        print('id не найден')
# проверка на присутствие в маршрутах
def is_used(id, pos):
    routes = get_routes()
    for route in routes:
        if route[pos] == id:
           print('невозможно удалить, сначала удалите соответствующий маршрут')
           return True
    return False
# удаление из списков, выбор списка
def delete_from_list():
    pathes = ['bus.txt', 'driver.csv', 'route.txt']
    try:
        n = int(input('Выберите список - (1 - автобусы, 2 - водители, 3 - маршруты): ')) - 1
        path = pathes[n]
    except:
        print('ошибка ввода')
        return
    lines = read_data_from_file(path)
    id = input('Id = ')
    if n < 2:
      if is_used(id, n + 2):
          return
    delete(lines, path, id)

# добавления с проверками на дупликаты id
# для маршрутов также проверка на существование вносимых водителй и автобусов
def add_bus():          
    lines = get_buses()
    line = list()
    bus_id = input("Bus Id: ")
    if find_by_id(lines, bus_id) != None:
        print('этот Id уже используется')
        return
    line.append(bus_id)
    line.append(input("X-Plate: "))
    lines.append(line)    
    save_as_csv('bus.txt', lines)

def add_driver():
    lines = get_drivers()
    line = list()
    driver_id = input("Driver Id: ")
    if find_by_id(lines, driver_id) != None:
        print('этот Id уже используется')
        return
    line.append(driver_id)
    line.append(input("Name: "))
    lines.append(line)    
    save_as_csv('driver.csv', lines)

def add_route():
    lines = get_routes()
    line = list()
    route_id = input("Route Id: ")
    if find_by_id(lines, route_id) != None:
        print('этот Route Id уже используется')
        return
    line.append(route_id)
    line.append(input("Number: "))
    bus_id = input("Bus_Id: ")
    buses = get_buses();
    if find_by_id(buses, bus_id) == None:
        print('этот Bus Id не существует')
        return
    line.append(bus_id)
    driver_id = input("Driver_Id: ")
    drivers = get_drivers();
    if find_by_id(drivers, driver_id) == None:
        print('этот Driver Id не существует')
        return
    line.append(driver_id)
    lines.append(line)    
    save_as_csv('route.txt', lines)

