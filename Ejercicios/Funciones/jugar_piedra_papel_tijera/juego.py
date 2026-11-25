import random
from reglas import *
from input import *


def pedir_eleccion_jugador() -> int:
    """
    Pide la eleccion al jugador (1, 2 o 3) hasta obtener un dato valido.
    Parametros:
        Ninguno
    Return:
        - int: la eleccion validada (1 Piedra, 2 Papel, 3 Tijera).
    """
    eleccion = None
    while eleccion == None:
        eleccion = get_int("Elegí: 1) Piedra  2) Papel  3) Tijera: ", "ERROR, ingresá 1, 2 o 3.", 1, 3, 2)
        if eleccion == None:
            print("Demasiados intentos invalidos, probemos de nuevo.")
    return eleccion


def informar_resultado_ronda(ganador_ronda: str) -> None:
    """
    Imprime quien gano la ronda.
    Parametros:
        - ganador_ronda (str): "Jugador", "Máquina" o "Empate".
    Return:
        None
    """
    if ganador_ronda == "Jugador":
        print("Ganaste la ronda!")
    elif ganador_ronda == "Máquina":
        print("La máquina gana la ronda.")
    else:
        print("Empate, la ronda no suma puntos.")


def jugar_piedra_papel_tijera() -> str:
    """
    Gestiona toda la partida de Piedra, Papel o Tijera contra la maquina.
    Parametros:
        Ninguno
    Return:
        - str: "Jugador" o "Máquina", segun quien gano la partida.
    """
    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda_actual = 0
    partida_en_curso = True

    while partida_en_curso:
        ronda_actual += 1
        print(f"\n===== RONDA {ronda_actual} =====")

        eleccion_jugador = pedir_eleccion_jugador()
        eleccion_maquina = random.randint(1, 3)
        print(f"Elegiste: {mostrar_elemento(eleccion_jugador)}, la máquina eligió: {mostrar_elemento(eleccion_maquina)}")

        ganador_ronda = verificar_ganador_ronda(eleccion_jugador, eleccion_maquina)
        informar_resultado_ronda(ganador_ronda)
        if ganador_ronda == "Jugador":
            aciertos_jugador += 1
        elif ganador_ronda == "Máquina":
            aciertos_maquina += 1

        print(f"Marcador -> Jugador: {aciertos_jugador}, Máquina: {aciertos_maquina}")
        partida_en_curso = verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual)

    ganador_partida = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
    print(f"\n*** FIN DE LA PARTIDA. Ganador: {ganador_partida} ***")
    return ganador_partida