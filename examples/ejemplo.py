from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import re

token = ''

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
        context.bot.send_message(chat_id = update.effective_chat.id, text="Hi Welcome to Ramiro First Bot!")

def unknown(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, mi no comprende.")

def get_url():
        contents = requests.get('https://random.dog/woof.json').json()
        url = contents['url']
        return url

def get_image_url():
        allowed_extension = ['jpg','jpeg','png']
        file_extension = ''
        while file_extension not in allowed_extension:
            url = get_url()
            file_extension = re.search("([^.]*)$",url).group(1).lower()
        print("got url %s"%url)
        return url

def bop(update, context):
        print("reached bop")
        url = get_image_url()
        context.bot.send_photo(chat_id=update.effective_chat.id, photo = url)

unknown_handler = MessageHandler(Filters.command, unknown)
start_handler = CommandHandler('start', start)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(CommandHandler('bop',bop))
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
