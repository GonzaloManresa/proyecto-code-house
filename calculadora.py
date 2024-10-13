"""
En un proyecto nuevo, crea un programa que muestre un menú y como opciones que muestre las operaciones de una calculadora. Según la opción que seleccione el usuario debe realizar la operación correspondiente, solicitandole previamente los operandos necesarios y mostrando el resultado con la operación, por ejemplo, para una suma debería mostrar algo como: '2 + 2 = 4'
"""
def menu():
    print("Calculadora")
    print("--------------------")
    print("Suma:              (1)")
    print("Resta:             (2)")
    print("Multiplicación:    (3)")
    print("División:          (4)")
    print("Mostrar Historial: (5)")
    print("Salir:             (0)")

# Lista para almacenar el historial de operaciones
historial = []

# Función para mostrar el historial
def mostrar_historial():
    if len(historial) == 0:
        print("No hay operaciones en el historial.")
    else:
        print("Historial de operaciones:")
        for operacion in historial:
            print(operacion)

# Bucle principal
while True:
    # Mostrar el menú y solicitar la opción del usuario
    menu()
    operacion_seleccionada = int(input("Seleccione una operación (0-5): "))

    if operacion_seleccionada == 0:
        print("Saliendo...")
        break  # Terminar el programa
    elif operacion_seleccionada == 5:
        mostrar_historial()
    else:
        # Pedir los números solo si no selecciona salir o mostrar historial
        numero_1 = float(input("Número 1: "))
        numero_2 = float(input("Número 2: "))

        # Realizar la operación según la selección
        if operacion_seleccionada == 1:
            resultado = numero_1 + numero_2
            operacion = f'{numero_1} + {numero_2} = {resultado}'
        elif operacion_seleccionada == 2:
            resultado = numero_1 - numero_2
            operacion = f'{numero_1} - {numero_2} = {resultado}'
        elif operacion_seleccionada == 3:
            resultado = numero_1 * numero_2
            operacion = f'{numero_1} * {numero_2} = {resultado}'
        elif operacion_seleccionada == 4:
            if numero_2 != 0:
                resultado = numero_1 / numero_2
                operacion = f'{numero_1} / {numero_2} = {resultado}'
            else:
                operacion = "Error: No se puede dividir entre cero."
        else:
            print("Operación no válida.")
            continue  # Reiniciar el bucle si la opción es inválida

        # Imprimir el resultado o error
        print(f'Resultado: {operacion}')
        
        # Agregar la operación al historial
        historial.append(operacion)
