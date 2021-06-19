from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils import print_, print__, human_answer
import subprocess
import time
import os

TOKEN_FATHER = os.getenv("TOKEN_FATHER")

TOKEN = TOKEN_FATHER

print("File one __name__ is set to: {}, token {}" .format(__name__, TOKEN))

def hi(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text="Bienvenido soy el bot father")

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Mi no comprende")

def prende_foto(update, context):
    print_("comando prende foto")
    subprocess.run(["systemctl", "--user", "start", "python_telegram_foto.service"])

def prende_sensor(update, context):
    print_("comando prende sensor")
    subprocess.run(["systemctl", "--user", "start", "python_telegram_sensor.service"])

def apaga_sensor(update, context):
    print_("comando apaga sensor")
    subprocess.run(["systemctl", "--user", "stop", "python_telegram_sensor.service"])

def apaga_foto(update, context):
    print_("comando apaga foto")
    subprocess.run(["systemctl", "--user", "stop", "python_telegram_foto.service"])

def estado_sensor(update, context):
    print_("comando estado sensor")
    answer = subprocess.run(["systemctl", "--user", "status", "python_telegram_sensor.service"])
    answer_text = human_answer(answer.returncode)
    context.bot.send_message(chat_id=update.effective_chat.id, text=answer_text)

def estado_foto(update, context):
    print_("comando estado foto")
    answer = subprocess.run(["systemctl", "--user", "status", "python_telegram_foto.service"])
    answer_text = human_answer(answer.returncode)
    context.bot.send_message(chat_id=update.effective_chat.id, text=answer_text)

def recarga_servicios(update, context):
    print_("reload")
    answer = subprocess.run(["systemctl", "--user", "daemon-reload"])

def ayuda(update, context):
    print_("Ayuda")
    update.message.reply_text('Ayuda')
    context.bot.send_message(chat_id=update.effective_chat.id, text="opciones: /hi /sensor_on /sensor_off /sensor_status /foto_on /foto_off /foto_status /help")

def main():

    print_("Inicia bot father")
    #time.sleep(120)
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    unknown_handler = MessageHandler(Filters.command, unknown)
    dict_commands = {'hi': hi, 
                    'sensor_on': prende_sensor, 
                    'sensor_off': apaga_sensor, 
                    'sensor_status': estado_sensor, 
                    'foto_on': prende_foto, 
                    'foto_off': apaga_foto, 
                    'foto_status': estado_foto, 
                    'help': ayuda}
    for command in dict_commands:
        dispatcher.add_handler(CommandHandler(command, dict_commands[command]))
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
