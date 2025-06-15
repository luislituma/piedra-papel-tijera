"""Este es el trabajo Autonomo para Logica de Programacion
Autor: Luis Lituma
"""
print("BIENVENIDO AL JUEGO PIEDRA PAPEL O TIJERA")
print("Inicio del juego")
print("Elige entre las opciones: piedra, papel o tijera")

intentos = 3  

contador = 0

while contador < intentos:
    jugador = input("Tu elección: ")

    # El jugador
    print("Elegiste:", jugador)

    # La computadora
    if contador == 0:
        computadora = "piedra"
    elif contador == 1:
        computadora = "papel"
    else:
        computadora = "tijera"

    print("La computadora eligió:", computadora)


    if jugador == computadora:
        print("Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("Ganaste!")
    else:
        print("Perdiste!")

    contador = contador + 1

print("El juego termina")