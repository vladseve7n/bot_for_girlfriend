# https://complimentr.com/api

import telebot
import time
import random

bot = telebot.TeleBot('1891785143:AAHstdc2t03P0G0TYi9QoycK4zilaZ6WAuo')

compliments = []
with open('Clear_compliment.txt', 'r') as f:
    for i in f:
        compliments.append(i)


def compliment_maker(compliments):
    return 'Комплимент для тебя:\n' + random.choice(compliments)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('Комплимент')
    markup.add(itembtn1)
    hello_message = "Это все для тебя, солнышко ❤"
    bot.send_message(message.from_user.id, hello_message, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_compliment(message):
    if message.text == 'Комплимент':
        timer = time.time()
        bot.send_message(message.chat.id, compliment_maker(compliments))
        while True:
            if time.time() - timer > 60:
                timer = time.time()
                bot.send_message(message.chat.id,
                                 compliment_maker(compliments))


bot.polling()
