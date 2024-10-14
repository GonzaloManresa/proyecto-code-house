from termcolor import colored, cprint

def menu():
    print(colored("Calculadora","blue",attrs=["reverse", "blink","bold"]))
    print("----------------------")
    print(colored("Suma:              (1)","light_blue"))
    print(colored("Resta:             (2)","light_blue"))
    print(colored("Multiplicación:    (3)","light_blue"))
    print(colored("División:          (4)","light_blue"))
    print(colored("Mostrar Historial: (5)","light_blue"))
    print(colored("Salir:             (0)","light_blue"))


# Lista para almacenar el historial de operaciones
historial = []

# Función para mostrar el historial
def mostrar_historial():
    if len(historial) == 0:
        print("No hay operaciones en el historial.")
    else:
        print(colored("Historial de operaciones:","light_red",attrs=["bold"]))
        for operacion in historial:
            print(operacion)