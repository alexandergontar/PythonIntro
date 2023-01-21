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
        ("1", "Вывод всех списков", fn.get_lists),        
        ("2", "Добавление автобуса", fn.add_bus),        
        ("3", "Добавление водителя", fn.add_driver),        
        ("4", "Добавление маршрута", fn.add_route),
        ("5", "Удаление", fn.delete),        
        ("0", "Выход", lambda: exit())]

  for i in menuitems:
     print(i[0],i[1])

  text = input("Введите номер: ")
  if text == '1':
    display_resources(fn.get_lists())
  elif text == '2':
    fn.add_bus()
  elif text == '3':
    fn.add_driver()
  elif text == '4':
    fn.add_route()
  elif text == '5':
    fn.delete_from_list()
  elif text == '0':
    return True  
  if input("Продолжить/Выход - y / n: ").upper() == 'N':
     return True
  else:
     return False