import os
import telebot
import requests
import json
#import wikipedia
TOKEN = '5902108357:AAGCacwoAS7VEqINvpH2AF0F6fuqmlmXJZU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
input()