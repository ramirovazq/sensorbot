
def print_(palabra="Inicio"):
    print("=".rjust(50, "="))
    print(f"{palabra}".rjust(50, "."))
    print("=".rjust(50, "="))

def print__(palabra="Inicio"):
    print(f"{palabra}".rjust(50, "."))

def human_answer(valor):
    answer = "?"
    valor = str(valor)
    if valor == "0":
        answer = "encendido"
    elif valor == "3":
        answer = "apagado"
    return answer
