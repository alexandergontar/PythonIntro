import bot_commands
import telebot
import conf

bot = telebot.TeleBot(conf.TOKEN)

@bot.message_handler(commands=[ 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Добро пожаловать, введите арифметическое выражение, например 1 + 2 * (7 - 1) + (4 - 2) / 2 : ')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Введите арифметическое выражение: ')

@bot.message_handler(content_types=["text"])
def run_commands(message):    
    bot.add_message_handler(bot_commands.calc_exp(message))

bot.infinity_polling()


