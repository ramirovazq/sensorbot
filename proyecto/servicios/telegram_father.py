from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils import print_, print__, human_answer
import subprocess
import time
import os

TOKEN_FATHER = os.getenv("TOKEN_FATHER")

TOKEN = TOKEN_FATHER

print("telegram_father is set to: {}, token {}" .format(__name__, TOKEN))

def hi(update, context):
    print_("bot father: hi")
    context.bot.send_message(chat_id = update.effective_chat.id, text="Hi i'm bot father. /help")

def unknown(update, context):
    print_("bot father: unknown text")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Mi no comprende. /help")

def prende_foto(update, context):
    print_("bot father: comando prende foto")
    try:
        subprocess.run(['systemctl', '--user', 'start', 'telegram_foto.service'])
    except Exception as e:
        print("Error in subprocess ...")
        raise

def prende_sensor(update, context):
    print_("bot father: comando prende sensor")
    subprocess.run(["systemctl", "--user", "start", "telegram_sensor.service"])

def apaga_sensor(update, context):
    print_("bot father: comando apaga sensor")
    subprocess.run(["systemctl", "--user", "stop", "telegram_sensor.service"])

def apaga_foto(update, context):
    print_("bot father: comando apaga foto")
    subprocess.run(["systemctl", "--user", "stop", "telegram_foto.service"])

def estado_sensor(update, context):
    print_("bot father: comando estado sensor")
    answer = subprocess.run(["systemctl", "--user", "status", "telegram_sensor.service"])
    answer_text = human_answer(answer.returncode)
    context.bot.send_message(chat_id=update.effective_chat.id, text=answer_text)

def estado_foto(update, context):
    print_("bot father: comando estado foto")
    answer = subprocess.run(["systemctl", "--user", "status", "telegram_foto.service"])
    answer_text = human_answer(answer.returncode)
    context.bot.send_message(chat_id=update.effective_chat.id, text=answer_text)

def recarga_servicios(update, context):
    print_("bot father: reload")
    answer = subprocess.run(["systemctl", "--user", "daemon-reload"])

def ayuda(update, context):
    print_("bot father: Ayuda")

    ayuda_text = "opciones: "
    commands_list = [
        "/hi", 
        "/sensor_on",
        "/sensor_off",
        "/sensor_status",
        "/foto_on",
        "/foto_off",
        "/foto_status",
        "/reload",
        "/help "
    ]
    ayuda_text = ayuda_text + " ".join(commands_list)

    update.message.reply_text('Ayuda')
    context.bot.send_message(chat_id=update.effective_chat.id, text=ayuda_text)

def main_father():

    print_("Inicia bot father")
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dict_commands = {'hi': hi, 
                    'sensor_on': prende_sensor, 
                    'sensor_off': apaga_sensor, 
                    'sensor_status': estado_sensor, 
                    'foto_on': prende_foto, 
                    'foto_off': apaga_foto, 
                    'foto_status': estado_foto, 
                    'reload': recarga_servicios, 
                    'help': ayuda}

    for command in dict_commands:
        dispatcher.add_handler(CommandHandler(command, dict_commands[command]))

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main_father()
