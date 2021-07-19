from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from camera import take_photo 
from time import sleep
from utils import print_, print__
import RPi.GPIO as GPIO
import os

TOKEN_SON = os.getenv("TOKEN_SON")
TOKEN = TOKEN_SON

print("telegram_sensor is set to: {}, token {}" .format(__name__, TOKEN))

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

def hi(update, context):
    print_("bot sensor: Hi")
    context.bot.send_message(chat_id = update.effective_chat.id, text="Hi! soy el sensor. /help")

def unknown(update, context):
    print_("bot sensor: unknown text")
    context.bot.send_message(chat_id=update.effective_chat.id, text="No te entiendo")

def ayuda(update, context):
    print_("bot sensor: Ayuda")

    ayuda_text = "opciones: "
    commands_list = [
        "/hi", 
        "/start_sensor",
        "/help",
    ]
    ayuda_text = ayuda_text + " ".join(commands_list)

    update.message.reply_text("Ayuda")
    context.bot.send_message(chat_id=update.effective_chat.id, text=ayuda_text)

def comienza_sensor(update, context):
    print_("bot sensor: inicia sensor (while)")

    while True:
        if GPIO.input(23):
            print__("bot sensor: Movement detected")
            take_photo()
            with open("/home/pi/sensorcam/storage/fotos/image.jpg", "rb") as lafoto:
                context.bot.send_photo(chat_id=update.effective_chat.id, photo = lafoto, timeout=180)
                print__("bot sensor: Photo sent")
    print_("bot sensor: inicia sensor, finalizado (while)")

def main_sensor():

    print_("Inicia bot sensor")
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dict_commands = {'hi': hi, 
                     'help': ayuda, 
                     'start_sensor': comienza_sensor}

    for command in dict_commands:
        dispatcher.add_handler(CommandHandler(command, dict_commands[command]))

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main_sensor()
