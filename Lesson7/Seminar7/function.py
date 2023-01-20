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
          #data.write(user[0]+','+user[1]+'\n')

def add_line(lines, line):
    #lines = print_bus()
    line = list()
    line.append(bus_id)
    line.append(x_plate)
    lines.append(line)
    print(lines)
    return lines


def print_bus():
    return read_data_from_file('bus.txt')
def print_driver():
    return read_data_from_file('driver.txt')
def print_route():
    return read_data_from_file('route.txt')

def find_by_id(lines : list(), id):      
       count = 0
       for line in lines:
           if line[0] == id:
               count+=1               
       if count == 0:           
           return None 
       else:
           return line

def add_bus():
    lines = print_bus()
    line = list()
    bus_id = input("Bus Id: ")
    if find_by_id(lines, bus_id) != None:
        print('this id already exist')
        return
    line.append(bus_id)
    line.append(input("X-Plate: "))
    lines.append(line)
    
    save_as_csv('bus.txt', lines)  


def add_driver():
    lines = print_driver()
    line = list()
    driver_id = input("Driver Id: ")
    if find_by_id(lines, driver_id) != None:
        print('this id already exist')
        return
    line.append(driver_id)
    line.append(input("Name: "))
    lines.append(line)    
    save_as_csv('driver.txt', lines)

def add_route():
    lines = print_route()
    line = list()
    route_id = input("Route Id: ")
    if find_by_id(lines, route_id) != None:
        print('this id already exist')
        return
    line.append(route_id)
    line.append(input("Number: "))
    line.append(input("Bus_Id: "))
    line.append(input("Driver_Id: "))
    lines.append(line)    
    save_as_csv('route.txt', lines)

