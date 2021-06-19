import RPi.GPIO as GPIO
from time import sleep
from camera import take_photo

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)


def inicia_sensor(debug=False):
    if debug:
        print("MODO DEBUG !")
    while True:
        if GPIO.input(23):
            if debug:
                print("DETECTADO ....................")
                sleep(1)
            else:
                print("DETECTADO ...................")
                take_photo()
                sleep(15)

if __name__ == "__main__":
    print("================ INICIA SENSOR ====================")
    inicia_sensor(True)

