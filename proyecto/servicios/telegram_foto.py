from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from camera import take_photo 
from utils import print_, print__
import RPi.GPIO as GPIO
import os

TOKEN_SON = os.getenv("TOKEN_SON")
TOKEN = TOKEN_SON

print("telegram_foto is set to: {}, token {}" .format(__name__, TOKEN))

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

def hi(update, context):
    print_("bot foto: Hi")
    context.bot.send_message(chat_id = update.effective_chat.id, text="Hi! im bot foto. /help")

def unknown(update, context):
    print_("bot foto: unknown text")
    context.bot.send_message(chat_id=update.effective_chat.id, text="No te entiendo. /help")

def toma_y_envia_foto(update, context):
    print_("bot foto: comando de toma y envia foto")
    take_photo()
    with open("/home/pi/sensorcam/storage/fotos/image.jpg", "rb") as lafoto:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo = lafoto)
        print__("bot foto: Photo sent")

def ayuda(update, context):
    print_("bot foto: Ayuda")

    ayuda_text = "opciones: "
    commands_list = [
        "/hi", 
        "/help",
        "/foto",
    ]
    ayuda_text = ayuda_text + " ".join(commands_list)

    update.message.reply_text("Ayuda")
    context.bot.send_message(chat_id=update.effective_chat.id, text=ayuda_text)

def main_foto():

    print_("Inicia bot foto")
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dict_commands = {'hi': hi, 
                     'help': ayuda, 
                     'foto': toma_y_envia_foto}

    for command in dict_commands:
        dispatcher.add_handler(CommandHandler(command, dict_commands[command]))

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main_foto()
