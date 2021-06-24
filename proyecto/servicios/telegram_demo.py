if __name__ == '__main__':
    import time
    import os
    import subprocess

    TOKEN_DEMO = os.getenv("TOKEN_DEMO")

    process = subprocess.Popen(['awk'], stdout=subprocess.PIPE)
    print(process)
    sub = subprocess.run(["systemctl", "--user", "start", "telegram_foto.service"])
    print(sub)

    while True:
        print(f'Este es el DEMO de telegram script en python ejecutandose cada 5 segundos {TOKEN_DEMO}')
        print("-----")
        time.sleep(5)
