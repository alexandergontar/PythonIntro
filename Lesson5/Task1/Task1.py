import os
import telebot
TOKEN = '5902108357:AAGCacwoAS7VEqINvpH2AF0F6fuqmlmXJZU'
bot = telebot.TeleBot(TOKEN)
def A_power_B(A, B):
    if (B == 1):
        return A
    if (B != 1):
        return A * A_power_B(A, B - 1)
while True:
    try:
      A = int(input("Введите число: "))
      B = int(input("Введите степень: "))
      break
    except:
        print('Неверный ввод')
print("Результат возведения в степень равен:", A_power_B(A, B))

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
input()