from menu import Menu
import function as fn
import UI

while True:
    try:
      #x = UI.menu()
      if UI.menu():
          break
    except:
      print('неверный ввод')
      break

