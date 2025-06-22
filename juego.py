"""Este es el trabajo Autonomo para Logica de Programacion
Autor: Luis Lituma
"""
import random # Para usar en la eleccion aleatoria de la computadora


while True: # Para que mientras sea verdadero el juego continua ejecutandose
    
    # Mensaje de Bienvenida y muesta opciones al usuario 
    print("BIENVENIDO AL JUEGO PIEDRA, PAPEL O TIJERA")
    print("El juego inicia...")
    print("Elige entre estas opciones:")
    print("1 - Piedra")
    print("2 - Papel")
    print("3 - Tijera")
    print("0 - Salir")

    # Usamos el try para capturar entradas no válidas en teclado
    try:
        eleccion_Usuario = int(input("Tu eleccion: ")) # Variable que almacena la eleccion del usuario
        if eleccion_Usuario == 0:
            print("Saliendo del juego...")
            break
        if eleccion_Usuario not in[1, 2, 3]:
            print("Opcion no válida, intenta de nuevo")
            continue
    except ValueError:
        print("Entrada no válida, debes escribir solamente numeros")
        continue
    
    # Eleccion random de la computadora
    eleccion_Computadora = random.randint(1, 3) # Almacena la eleccionde la computadora. Ademas elige una opción random entre 1 y 3

    opciones = {1: "Piedra", 2:"Papel", 3:"Tijera"} # Uso de diccionario para almancenar las opciones

    print(f"Tu elegiste : {opciones[eleccion_Usuario]}") #Imprime la eleccion del usuario
    print(f"La computadora eligio: {opciones[eleccion_Computadora]}") # Imprime la eleccion de la computadora

    #Comparacion entre las elecciones de la computadora y el usuario. Imprime el resultado
    if eleccion_Computadora == eleccion_Usuario:
        print("Resultado: ¡Empate!")
    elif (eleccion_Usuario == 1 and eleccion_Computadora ==3) or (eleccion_Usuario == 2 and eleccion_Computadora == 1) and (eleccion_Usuario == 3 or eleccion_Computadora == 1):
        print("Resultado: ¡Ganaste!")
    else:
        print("Resultado: ¡Perdiste!")