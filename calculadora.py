"""
En un proyecto nuevo, crea un programa que muestre un menú y como opciones que muestre las operaciones de una calculadora. Según la opción que seleccione el usuario debe realizar la operación correspondiente, solicitandole previamente los operandos necesarios y mostrando el resultado con la operación, por ejemplo, para una suma debería mostrar algo como: '2 + 2 = 4'
"""

def menu():
    print("Calculadora")
    print("--------------------")
    print("Suma:           (1)")
    print("Resta:          (2)")
    print("Multiplicacion: (3)")
    print("Division:       (4)")
    print("Salir:          (0)")

# Mostrar el menú 
menu()

# Solicitar la opción del usuario
operacion_seleccionada = int(input("Seleccione una operación (0-4): "))

# Si la opción es salir, terminar el programa
if operacion_seleccionada == 0:
    print("Saliendo de la calculadora")
else:
    # Pedir los números solo si no selecciona salir
    numero_1 = float(input("Número 1: "))
    numero_2 = float(input("Número 2: "))

    # Realizar la operación según la selección
    if operacion_seleccionada == 1:
        print(f'Resultado: {numero_1} + {numero_2} = {numero_1 + numero_2}')
    elif operacion_seleccionada == 2:
        print(f'Resultado: {numero_1} - {numero_2} = {numero_1 - numero_2}')
    elif operacion_seleccionada == 3:
        print(f'Resultado: {numero_1} * {numero_2} = {numero_1 * numero_2}')
    elif operacion_seleccionada == 4:
        # Manejar la división por cero
        if numero_2 != 0:
            print(f'Resultado: {numero_1} / {numero_2} = {numero_1 / numero_2}')
        else:
            print("Error: No se puede dividir entre cero.")
    else:
        print("Operación no válida.")
