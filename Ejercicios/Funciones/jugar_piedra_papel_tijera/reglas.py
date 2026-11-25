def verificar_ganador_ronda(jugador: int, maquina: int) -> str:
    """
    Determina quien gano la ronda segun las elecciones.
    Parametros:
        - jugador (int): eleccion del jugador (1 Piedra, 2 Papel, 3 Tijera).
        - maquina (int): eleccion de la maquina (1 Piedra, 2 Papel, 3 Tijera).
    Return:
        - str: "Jugador", "Máquina" o "Empate".
    """
    if jugador == maquina:
        ganador = "Empate"
    elif (jugador == 1 and maquina == 3) or (jugador == 3 and maquina == 2) or (jugador == 2 and maquina == 1):
        # Piedra aplasta Tijera, Tijera corta Papel, Papel envuelve Piedra
        ganador = "Jugador"
    else:
        ganador = "Máquina"
    return ganador


def verificar_estado_partida(aciertos_jugador: int, aciertos_maquina: int, ronda_actual: int) -> bool:
    """
    Determina si la partida sigue en curso o ya finalizo.
    Se llama al terminar cada ronda. La partida finaliza cuando alguien llega a 2 aciertos,
    o cuando ya se jugaron las 3 rondas y hay un ganador (si hay empate, se sigue jugando).
    Parametros:
        - aciertos_jugador (int): rondas ganadas por el jugador.
        - aciertos_maquina (int): rondas ganadas por la maquina.
        - ronda_actual (int): numero de la ronda que se acaba de jugar.
    Return:
        - bool: True si la partida sigue en curso, False si finalizo.
    """
    sigue_en_curso = True
    if aciertos_jugador >= 2 or aciertos_maquina >= 2:
        sigue_en_curso = False
    elif ronda_actual >= 3 and aciertos_jugador != aciertos_maquina:
        sigue_en_curso = False
    return sigue_en_curso


def verificar_ganador_partida(aciertos_jugador: int, aciertos_maquina: int) -> str:
    """
    Determina quien gano la partida comparando los aciertos finales.
    Parametros:
        - aciertos_jugador (int): rondas ganadas por el jugador.
        - aciertos_maquina (int): rondas ganadas por la maquina.
    Return:
        - str: "Jugador" o "Máquina" ("Empate" solo si se la llama con aciertos iguales).
    """
    if aciertos_jugador > aciertos_maquina:
        ganador = "Jugador"
    elif aciertos_maquina > aciertos_jugador:
        ganador = "Máquina"
    else:
        ganador = "Empate"
    return ganador


def mostrar_elemento(eleccion: int) -> str:
    """
    Convierte la eleccion numerica en un texto legible.
    Parametros:
        - eleccion (int): 1 Piedra, 2 Papel, 3 Tijera.
    Return:
        - str: "Piedra", "Papel" o "Tijera" ("Invalido" si la eleccion no es 1, 2 o 3).
    """
    if eleccion == 1:
        elemento = "Piedra"
    elif eleccion == 2:
        elemento = "Papel"
    elif eleccion == 3:
        elemento = "Tijera"
    else:
        elemento = "Invalido"
    return elemento