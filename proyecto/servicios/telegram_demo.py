if __name__ == '__main__':
    import time
    import os
    import subprocess
    TOKEN_DEMO = os.getenv("TOKEN_DEMO")
    while True:
        print(f'Este es el DEMO de telegram script en python ejecutandose cada 5 segundos {TOKEN_DEMO}')
        print(TOKEN_DEMO)
        print("-----")
        algo = subprocess.run(["systemctl", "--user", "start", "telegram_sensor.service"])
        print(algo)
        time.sleep(50)
