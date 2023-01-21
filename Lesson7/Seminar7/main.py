from menu import Menu
import function as fn
import UI

while True:
    try:      
      if UI.menu():
          break
    except:
      print('неверный ввод')
      break

