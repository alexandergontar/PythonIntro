import function as fn


def display_resources(resources : list()):    
    for i in range(len(resources)):         
         print(i + 1, end = ' ')
         resource = resources[i]
         for item in resource:
             print(item, end =' ')
         print()

def menu():    
  menuitems = [
        ("1", "Вывод автобусов", fn.print_bus),
        ("2", "Добавление автобуса", fn.add_bus),
        ("3", "Вывод водителей", fn.print_driver),
        ("4", "Добавление водителей", fn.add_driver),
        ("5", "Вывод маршрута", fn.print_route),
        ("6", "Добавление маршрута", fn.add_route),
        ("7", "Выход", lambda: exit())]

  for i in menuitems:
     print(i[0],i[1])

  text = input("Введите номер: ")
  if text == '1':    
    display_resources(fn.print_bus())
  elif text == '2':
    fn.add_bus()
  elif text == '3':
    display_resources(fn.print_driver())
  elif text == '4':
    fn.add_driver()
  elif text == '5':    
    display_resources(fn.print_route())
  elif text == '6':
    fn.add_route()
  elif text == '7':
    return True  
  if input("Продолжить/Выход - yes/no: ").upper() == 'NO':
     return True
  else:
     return False