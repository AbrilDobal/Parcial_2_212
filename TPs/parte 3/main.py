# Programa principal: Tragamonedas, BlackJack y Sopa de Letras con puntaje, apuesta compartidos y ranking por archivo CSV.
from funciones_casino import *

print("=== BIENVENIDO AL CASINO DE PROGRAMACION I ===")
nombre_jugador = input("Ingrese su nombre de jugador: ").strip()
if nombre_jugador == "":
    nombre_jugador = "Anonimo"

puntaje = 1000
apuesta_actual = 100
jugando = True

menu = """
=== MENU PRINCIPAL ===
1) Jugar Tragamonedas.
2) Jugar BlackJack.
3) Jugar Sopa de Letras.
4) Cambiar Apuesta.
5) Mostrar Ranking.
6) Salir.

Seleccione una opcion: """

while jugando:
    print(f"\nJugador: {nombre_jugador} | Puntaje: {puntaje} | Apuesta actual: {apuesta_actual}")
    opcion = input(menu)

    match opcion:
        case "1":
            apuesta_actual = ajustar_apuesta(apuesta_actual, puntaje)
            puntaje = jugar_tragamonedas(puntaje, apuesta_actual)
            actualizar_ranking(nombre_jugador, puntaje)
        case "2":
            apuesta_actual = ajustar_apuesta(apuesta_actual, puntaje)
            puntaje = jugar_blackjack(puntaje, apuesta_actual)
            actualizar_ranking(nombre_jugador, puntaje)
        case "3":
            apuesta_actual = ajustar_apuesta(apuesta_actual, puntaje)
            puntaje = jugar_sopa_de_letras(puntaje, apuesta_actual)
            actualizar_ranking(nombre_jugador, puntaje)
        case "4":
            apuesta_actual = cambiar_apuesta(apuesta_actual, puntaje)
        case "5":
            mostrar_ranking()
        case "6":
            actualizar_ranking(nombre_jugador, puntaje)
            print(f"Programa terminado. Puntaje final de {nombre_jugador}: {puntaje}")
            jugando = False
        case _:
            print("Opcion Incorrecta")

    if jugando and puntaje <= 0:
        puntaje = 0
        actualizar_ranking(nombre_jugador, puntaje)
        print(f"Te quedaste sin puntos! Fin del juego. Puntaje final: {puntaje}")
        jugando = False