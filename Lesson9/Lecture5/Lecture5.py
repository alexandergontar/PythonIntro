import telebot
import wikipedia
import re
import os
from isOdd import isOdd
from progress.bar import Bar
import progress
import time
import emoji
import matplotlib.pyplot as plt
import numpy as np



TOKEN = '5923725347:AAHJXDY76Dghdu5bU_doA9C0awRhy0D4zDk'
bot = telebot.TeleBot(TOKEN)
wikipedia.set_lang("ru") # Устанавливаем русский язык в Wikipedia
                   
#print(isOdd(3))
#print(isOdd(0))

#bar = Bar('Processing',max = 20)
#for i in range(20):
#    time.sleep(1)
    #print('#', end = "")
#    bar.next()
#bar.finish()
#print(emoji.emojize('Python is :thumbs_up:'))
np.random.seed(19680801)

plt.rcdefaults()
fig, ax = plt.subplots()
input()
