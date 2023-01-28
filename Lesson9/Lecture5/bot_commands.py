import telebot
import RPN
import conf

bot = telebot.TeleBot(conf.TOKEN)
def repeat_all_messages(message): 
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
def calc_exp(message):
    msg = message.text
    try:
         result = RPN.rpn_calc(msg)
         answer = str(result)
         bot.send_message(message.chat.id, f' {msg} = {answer}')
    except:
         print('неверный ввод')
         bot.send_message(message.chat.id, 'неверный ввод')
    