# Programa principal: Tragamonedas y BlackJack con puntaje y apuesta compartidos.
from Funciones_casino import *

puntaje = 100
apuesta_actual = 10
jugando = True

menu = """
=== MENU PRINCIPAL ===
1) Jugar Tragamonedas.
2) Jugar BlackJack.
3) Cambiar Apuesta.
4) Salir.

Seleccione una opcion: """

while jugando:
    print(f"\nPuntaje: {puntaje}, Apuesta actual: {apuesta_actual}")
    opcion = input(menu)

    match opcion:
        case "1":
            apuesta_actual = ajustar_apuesta(apuesta_actual, puntaje)
            puntaje = jugar_tragamonedas(puntaje, apuesta_actual)
        case "2":
            apuesta_actual = ajustar_apuesta(apuesta_actual, puntaje)
            puntaje = jugar_blackjack(puntaje, apuesta_actual)
        case "3":
            apuesta_actual = cambiar_apuesta(apuesta_actual, puntaje)
        case "4":
            print(f"Programa terminado. Puntaje final: {puntaje}")
            jugando = False
        case _:
            print("Opcion Incorrecta")

    if jugando and puntaje <= 0:
        puntaje = 0
        print(f"Te quedaste sin puntos! Fin del juego. Puntaje final: {puntaje}")
        jugando = False