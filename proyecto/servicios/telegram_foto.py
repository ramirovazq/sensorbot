from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from camera import take_photo 
from utils import print_, print__
import RPi.GPIO as GPIO
import os

TOKEN_SON = os.getenv("TOKEN_SON")
TOKEN = TOKEN_SON

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

def hi(update, context):
    print_("Hi")
    context.bot.send_message(chat_id = update.effective_chat.id, text="Hi! soy el bot de foto")

def unknown(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="No te entiendo")

def toma_y_envia_foto(update, context):
    print_("comando de toma y envia foto")
    take_photo()
    with open("/home/pi/sensorcam/fotos/image.jpg", "rb") as lafoto:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo = lafoto)
        print__("Photo sent")

def ayuda(update, context):
    print__("Ayuda")
    update.message.reply_text("Ayuda")
    context.bot.send_message(chat_id=update.effective_chat.id, text="opciones: /hi /foto /help /unknown")

def main():

    print_("Inicia bot toma foto")
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    unknown_handler = MessageHandler(Filters.command, unknown)

    dict_commands = {'hi': hi, 'help': ayuda, 'foto': toma_y_envia_foto}
    for command in dict_commands:
        dispatcher.add_handler(CommandHandler(command, dict_commands[command]))
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
