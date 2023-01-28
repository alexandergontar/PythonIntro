#import telebot
import wikipedia
import re
import os
import spy
import bot_commands
#import time
import telebot
#import telegram
#import bot_commands as bc
#from telegram import Update
#from telegram.ext import Updater,  CommandHandler, CallbackContext
#from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
#from bot_commands import *
#from telegram import Update
#from telegram.ext import Updater, CommandHandler, CallbackContext
#from bot_commands import *
TOKEN = '5923725347:AAHJXDY76Dghdu5bU_doA9C0awRhy0D4zDk'
#updater = Updater(TOKEN)
#app = ApplicationBuilder().token('5923725347:AAHJXDY76Dghdu5bU_doA9C0awRhy0D4zDk').build()
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=[ 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Добро пожаловать, напишите через пробел 2 цифры: ')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Введите через пробел 2 цифры: ')
@bot.message_handler(content_types=["text"])
def run_commands(message): # Название функции не играет никакой роли    
    bot.add_message_handler(bot_commands.sum_a_b(message))

bot.infinity_polling()

input()
