import datetime
import logging

import telebot

TOKEN = "1176688239:AAECLP6Vkgj9ZeoXK9XwL0XLqlN996zkXQk"

# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", level=logging.INFO, filemode="w")
logging.info(f"Start logging. Session start time - {datetime.datetime.now()}")

bot = telebot.TeleBot(TOKEN)
logging.info("Bot initialize")
logging.info("Bot activate")


@bot.message_handler(commands=['start'])
def start_action(message):
    print(message)
    try:
        logging.info(f"{message.from_user.last_name} {message.from_user.first_name} {message.from_user.id} registered")
    except:
        logging.warning(f"Not a user send message")
    bot.send_message(message.chat.id, "You were registered.\nLet's start!")


bot.polling()
