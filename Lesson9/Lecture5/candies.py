import telebot, conf
from random import randint
from random import choice

bot = telebot.TeleBot(conf.TOKEN)

# для многопользовательности используем словари, ключ идентифицирует пользователей
# переменные ниже для индивидуальных message.chat.id
candies = dict()
enable_game = dict()
who_first = dict()

# фильтр   - продожить / закончить игру
def continue_end_game(message):
    global enable_game
    
    try:
        if (enable_game[message.chat.id] and 1 <= int(message.text) <= max_move): return True
        else: return False
    except KeyError:
        enable_game[message.chat.id] = False
        if (enable_game[message.chat.id] and 1 <= int(message.text) <= max_move ): return True
        else: return False
# начало игры
@bot.message_handler(commands=['sg']) # /sg - start game
def send_welcome(message):
    print('\t Играем в конфеты')
    global who_first, candies, enable_game, max_move, max_candies
    max_move = 28 # макс число конфет, которые можно брать за раз
    max_candies = 117 # всего конфет
    bot.reply_to(message, f'Начинаем игру в конфеты, на столе {max_candies} берем не больше { max_move} шт. за ход')
    candies[message.chat.id] = max_candies
    who_first[message.chat.id] = choice(['Bot', 'Вы'])
    bot.send_message(message.chat.id, f'Начинает игру в конфеты {who_first[message.chat.id]}')
    enable_game[message.chat.id] = True
    if who_first[message.chat.id] == 'Bot':
        # стратегия Бота: 
        how_many_candies = randint(1, candies[message.chat.id] % (max_move + 1))
        candies[message.chat.id] -= how_many_candies
        bot.send_message(message.chat.id, f'Бот взял со стола конфет {how_many_candies}')
        bot.send_message(message.chat.id,f'Осталось конфет на столе {candies[message.chat.id]}')
        who_first[message.chat.id] = 'Вы'
# продолжение игры (тело игрового процесса)
@bot.message_handler(func=continue_end_game)
def game_process(message):
    print(message.chat.id)
    global candies, who_first, enable_game
    if who_first[message.chat.id] == 'Вы':
        if candies[message.chat.id] > max_move:
            candies[message.chat.id] -= int(message.text)
            bot.send_message(message.chat.id,f'Осталось на столе конфет {candies[message.chat.id]} Ваш ход')
            if candies[message.chat.id] > max_move:
                temp = candies[message.chat.id] % (max_move + 1)
                if temp == 0 : how_many_candies = randint(1, max_move)
                else : how_many_candies = randint(1, temp)
                candies[message.chat.id] -= how_many_candies
                bot.send_message(message.chat.id, f'Бот взял со стола конфет {how_many_candies}')
                bot.send_message(message.chat.id, f'Осталось на столе конфет  {candies[message.chat.id]} Ваш ход')
                if candies[message.chat.id] <= max_move:
                    bot.send_message(message.chat.id, 'Вы победили')
                    enable_game[message.chat.id] = False
            else:
                bot.send_message(message.chat.id, 'Bot победил')
                enable_game[message.chat.id] = False
        else:
            bot.send_message(message.chat.id, 'Bot победил')
            enable_game[message.chat.id] = False

bot.infinity_polling()
