import telebot
TOKEN = '5923725347:AAHJXDY76Dghdu5bU_doA9C0awRhy0D4zDk'
bot = telebot.TeleBot(TOKEN)
def repeat_all_messages(message): # Название функции не играет никакой роли
    print(message.id, message.text)
    bot.send_message(message.chat.id, message.text)

def sum_a_b(message):
    print(message.id, message.text)
    msg = message.text
    args = msg.split()
    try:          
         a = int(args[0])
         b = int(args[1])
         sum = a + b
         bot.send_message(message.chat.id, f'{a} + {b} = {sum}')         
    except:
         print('неверный ввод')
         bot.send_message(message.chat.id, 'неверный ввод')
    return