#from telegram import Update
#from telegram.ext import Updater, CommandHandler, CallbackContext
import telebot
TOKEN = '5923725347:AAHJXDY76Dghdu5bU_doA9C0awRhy0D4zDk'
#updater = Updater(TOKEN)
#app = ApplicationBuilder().token('5923725347:AAHJXDY76Dghdu5bU_doA9C0awRhy0D4zDk').build()
bot = telebot.TeleBot(TOKEN)



def myFunc(message):
    print(message.id, message.text)
    msg = message.text
    args = msg.split()
    try:          
         a = int(args[0])
         b = int(args[1])
         sum = a + b
         bot.send_message(message.chat.id, f'{a} + {b} = {sum}')
         #bot.add_message_handler(spy.myFunc())
    except:
         print('неверный ввод')
         bot.send_message(message.chat.id, 'неверный ввод')
    return