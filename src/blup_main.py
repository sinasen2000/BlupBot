from telegram.ext import Updater, CommandHandler, InlineQueryHandler
import telegram
import requests
import json
import re

def get_url_dog():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_url_cat():
    contents = requests.get('http://aws.random.cat/meow').text
    d = json.loads(contents)
    return d['file']

def blupblup(bot, update):
    url_dog = get_url_dog()
    url_cat = get_url_cat()
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Here's your daily dog:")
    bot.send_photo(chat_id=chat_id, photo=url_dog)
    bot.send_message(chat_id=chat_id, text="Here's your daily cat:")
    bot.send_photo(chat_id=chat_id, photo=url_cat)

def main():
    updater = Updater('947153096:AAGteU11rJx48A8aFrUiZeShKg2AblC7msI')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('blup', blupblup))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()