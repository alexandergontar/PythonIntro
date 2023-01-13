import telebot
import wikipedia
import re
import os
TOKEN = '5923725347:AAHJXDY76Dghdu5bU_doA9C0awRhy0D4zDk'
bot = telebot.TeleBot(TOKEN)
wikipedia.set_lang("ru") # Устанавливаем русский язык в Wikipedia

def getwiki(s):
    try:
        data = wikipedia.page(s)
        wikitext_in = data.content[:2000] # 2000 символов c начала
        wikiarray = wikitext_in.split('.')
        wikiarray = wikiarray[:-1] # Все после последней точки удаляется
        wikitext_out = str() # Переменная для текста
        for each_strok in wikiarray:
            if not('==' in each_strok): # Все без заголовков
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((each_strok.strip()))>3):
                   wikitext_out=wikitext_out+each_strok+'.'
            else:
               break
        wikitext_out=re.sub('\([^()]*\)', '', wikitext_out) # Удаление разметки
        wikitext_out=re.sub('\([^()]*\)', '', wikitext_out)
        wikitext_out=re.sub('\{[^\{\}]*\}', '', wikitext_out)
        
        return wikitext_out # Возвращение текстовой строки
    except Exception as e:
        return (f'Данных об {s} НЕТ' ) # Исключение, возможное при запросе

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Вводим слово и узнаем его значение на Wikipedia (выводится не более 2000 символов')
@bot.message_handler(content_types=["text"]) # Сообщение что будем искать
def handle_text(message):
    global temp
    bot.send_message(message.chat.id, getwiki(message.text))
    temp = message.text
    print(f'Запрос на поиск значения слова {message.text}')
try:
    bot.polling(none_stop=True, interval=0)
except:
    print('polling failed, restart required')

input()
