from funciones import menu,mostrar_historial,historial


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
        print(f'Resultado: {resultado}')
        
        # Agregar la operación al historial
        historial.append(operacion)
