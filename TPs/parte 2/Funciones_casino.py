# MODULO funciones_casino: funciones del Tragamonedas y del BlackJack simplificado.
# Ambos juegos comparten el puntaje del jugador y la apuesta actual (se reciben por parametro).
import random


# ============================ VALIDACIONES Y ENTRADA DE DATOS ============================

def verificar_es_digito(caracter: str) -> bool:
    """
    Determina si un caracter esta comprendido entre 0...9.
    Parametros:
- caracter (str): el caracter a evaluar.
    Return:
- bool: True si es numerico, False en caso contrario.
    """
    if caracter >= "0" and caracter <= "9":
        es_digito = True
    else:
        es_digito = False
    return es_digito


def verificar_es_cadena_entera(texto: str) -> bool:
    """
    Verifica que un texto represente un numero entero (signo "-" opcional),
    para poder convertirlo a int sin errores.
    Parametros:
- texto (str): el texto a evaluar.
    Return:
- bool: True si se puede convertir a int, False en caso contrario.
    """
    inicio = 0
    if len(texto) > 0 and texto[0] == "-":
        inicio = 1
        
    if len(texto) > inicio:
        es_entera = True
    else:
        es_entera = False
        
    for i in range(inicio, len(texto)):
        if verificar_es_digito(texto[i]) == False:
            es_entera = False
            break
    return es_entera


def solicitar_entero_validado(mensaje: str, minimo: int, maximo: int) -> int:
    """
    Solicita un entero al usuario y lo revalida hasta que sea correcto (formato y rango).
    Parametros:
- mensaje (str): mensaje que se le muestra al usuario.
- minimo (int): valor minimo permitido (inclusive).
- maximo (int): valor maximo permitido (inclusive).
    Return:
- int: el numero validado.
    """
    es_valido = False
    numero = 0
    while es_valido == False:
        texto = input(mensaje)
        if verificar_es_cadena_entera(texto):
            numero = int(texto)
            if numero >= minimo and numero <= maximo:
                es_valido = True
            else:
                es_valido = False
        if es_valido == False:
            print(f"ERROR, ingrese un numero entero entre {minimo} y {maximo}.")
    return numero


# ============================ APUESTA (COMPARTIDA) ============================

def ajustar_apuesta(apuesta_actual: int, puntaje: int) -> int:
    """
    Ajusta la apuesta al puntaje disponible si la supera.
    Parametros:
- apuesta_actual (int): la apuesta seleccionada.
- puntaje (int): el puntaje disponible del jugador.
    Return:
- int: la apuesta a utilizar (igual a la actual, o al puntaje si la apuesta lo superaba).
    """
    if apuesta_actual > puntaje:
        apuesta = puntaje
        print(f"La apuesta se ajusto al puntaje disponible: {apuesta}")
    else:
        apuesta = apuesta_actual
    return apuesta


def cambiar_apuesta(apuesta_actual: int, puntaje: int) -> int:
    """
    Solicita una nueva apuesta (entre 1 y el puntaje disponible).
    Parametros:
- apuesta_actual (int): la apuesta seleccionada hasta el momento.
- puntaje (int): el puntaje disponible del jugador.
    Return:
- int: la nueva apuesta validada.
    """
    nueva_apuesta = solicitar_entero_validado(f"Ingrese el nuevo valor de apuesta (1-{puntaje}): ", 1, puntaje)
    print(f"Apuesta actualizada a: {nueva_apuesta}")
    return nueva_apuesta


# ============================ TRAGAMONEDAS ============================

def generar_fila_tragamonedas() -> list:
    """
    Genera una fila de 3 caracteres aleatorios entre A, B, C, D, E, 0 y 7.
    Parametros:
        Ninguno
    Return:
- list: lista con los 3 caracteres obtenidos.
    """
    caracteres = ["A", "B", "C", "D", "E", "0", "7"]
    fila = []
    for _ in range(3):
        indice = random.randint(0, len(caracteres) - 1)
        fila += [caracteres[indice]]
    return fila


def evaluar_fila_tragamonedas(fila: list) -> str:
    """
    Clasifica el resultado de una fila de 3 caracteres.
    Parametros:
- fila (list): lista con los 3 caracteres de la tirada.
    Return:
- str: "tres_ceros", "tres_sietes", "tres_iguales", "dos_iguales" o "distintos".
    """
    if fila[0] == fila[1] and fila[1] == fila[2]:
        if fila[0] == "0":
            resultado = "tres_ceros"
        elif fila[0] == "7":
            resultado = "tres_sietes"
        else:
            resultado = "tres_iguales"
    elif fila[0] == fila[1] or fila[1] == fila[2] or fila[0] == fila[2]:
        resultado = "dos_iguales"
    else:
        resultado = "distintos"
    return resultado


def jugar_tragamonedas(puntaje: int, apuesta_actual: int) -> int:
    """
    Juega una tirada de tragamonedas e informa el resultado.
    Parametros:
- puntaje (int): el puntaje disponible del jugador.
- apuesta_actual (int): la apuesta seleccionada (no mayor al puntaje).
    Return:
- int: el puntaje actualizado luego de la tirada.
    """
    fila = generar_fila_tragamonedas()
    print(f"Resultado: {fila[0]} {fila[1]} {fila[2]}")

    resultado = evaluar_fila_tragamonedas(fila)
    if resultado == "tres_ceros":
        puntaje = 0
        print("Perdiste todos los puntos!")
    elif resultado == "tres_sietes":
        puntaje += apuesta_actual * 10
        print(f"Tres 7! Ganaste {apuesta_actual * 10} puntos.")
    elif resultado == "tres_iguales":
        puntaje += apuesta_actual * 5
        print(f"Tres iguales! Ganaste {apuesta_actual * 5} puntos.")
    elif resultado == "dos_iguales":
        puntaje += apuesta_actual * 2
        print(f"Dos iguales! Ganaste {apuesta_actual * 2} puntos.")
    else:
        puntaje -= apuesta_actual
        print(f"Todos distintos. Perdiste {apuesta_actual} puntos.")

    print(f"Puntaje actual: {puntaje}")
    return puntaje


# ============================ BLACKJACK: CARTAS Y MANOS ============================

def crear_carta_aleatoria() -> str:
    """
    Saca una carta al azar de un mazo estandar (sin distinguir palos).
    Parametros:
        Ninguno
    Return:
- str: "A", "2" al "10", "J", "Q" o "K".
    """
    cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    indice = random.randint(0, len(cartas) - 1)
    carta = cartas[indice]
    return carta


def calcular_valor_carta(carta: str) -> int:
    """
    Calcula el valor de una carta (el As se cuenta como 11).
    Parametros:
- carta (str): "A", "2" al "10", "J", "Q" o "K".
    Return:
- int: 11 para el As, 10 para J, Q y K, y el numero de la carta en los demas casos.
    """
    if carta == "A":
        valor = 11
    elif carta == "J" or carta == "Q" or carta == "K":
        valor = 10
    else:
        valor = int(carta)
    return valor


def calcular_valor_mano(mano: list) -> int:
    """
    Calcula el valor total de una mano. Cada As vale 11, y pasa a valer 1 si hace falta para no superar 21.
    Parametros:
- mano (list): lista de cartas (str).
    Return:
- int: el mejor valor posible de la mano.
    """
    total = 0
    cantidad_ases = 0
    for carta in mano:
        total += calcular_valor_carta(carta)
        if carta == "A":
            cantidad_ases += 1
    while total > 21 and cantidad_ases > 0:
        total -= 10
        cantidad_ases -= 1
    return total


def mostrar_mano(mano: list) -> str:
    """
    Arma un texto con las cartas de una mano separadas por espacios.
    Parametros:
- mano (list): lista de cartas (str).
    Return:
- str: las cartas en una sola cadena. Ej: ["A", "7"] -> "A 7".
    """
    texto = ""
    for i in range(len(mano)):
        if i > 0:
            texto += " "
        texto += mano[i]
    return texto


def repartir_mano_inicial() -> list:
    """
    Reparte dos cartas.
    Parametros:
        Ninguno
    Return:
- list: lista con las dos cartas repartidas.
    """
    mano = [crear_carta_aleatoria(), crear_carta_aleatoria()]
    return mano


# ============================ BLACKJACK: TURNOS Y RESULTADO ============================

def jugar_turno_jugador(mano_jugador: list) -> list:
    """
    Turno del jugador: puede pedir cartas hasta plantarse o llegar/superar 21.
    Parametros:
- mano_jugador (list): las cartas actuales del jugador.
    Return:
- list: la mano del jugador al finalizar su turno.
    """
    se_planta = False
    valor = calcular_valor_mano(mano_jugador)
    while se_planta == False and valor < 21:
        print(f"Tu mano: {mostrar_mano(mano_jugador)} (valor: {valor})")
        eleccion = solicitar_entero_validado("1) Pedir carta  2) Plantarse: ", 1, 2)
        if eleccion == 1:
            carta = crear_carta_aleatoria()
            mano_jugador += [carta]
            valor = calcular_valor_mano(mano_jugador)
            print(f"Recibiste: {carta}")
        else:
            se_planta = True
    print(f"Tu mano final: {mostrar_mano(mano_jugador)} (valor: {valor})")
    return mano_jugador


def jugar_turno_banca(mano_banca: list) -> list:
    """
    Turno de la banca: revela su carta oculta y pide cartas mientras su valor sea menor a 17.
    Parametros:
- mano_banca (list): las cartas actuales de la banca.
    Return:
- list: la mano de la banca al finalizar su turno.
    """
    valor = calcular_valor_mano(mano_banca)
    print(f"La banca revela su mano: {mostrar_mano(mano_banca)} (valor: {valor})")
    while valor < 17:
        carta = crear_carta_aleatoria()
        mano_banca += [carta]
        valor = calcular_valor_mano(mano_banca)
        print(f"La banca pide: {carta}")
    print(f"Mano final de la banca: {mostrar_mano(mano_banca)} (valor: {valor})")
    return mano_banca


def determinar_resultado_blackjack(valor_jugador: int, valor_banca: int) -> str:
    """
    Determina el resultado de la ronda de BlackJack.
    Parametros:
- valor_jugador (int): valor final de la mano del jugador.
- valor_banca (int): valor final de la mano de la banca.
    Return:
- str: "Jugador", "Banca" o "Push" (empate).
    """
    if valor_jugador > 21:
        ganador = "Banca"
    elif valor_banca > 21:
        ganador = "Jugador"
    elif valor_jugador > valor_banca:
        ganador = "Jugador"
    elif valor_jugador < valor_banca:
        ganador = "Banca"
    else:
        ganador = "Push"
    return ganador


def jugar_blackjack(puntaje: int, apuesta_actual: int) -> int:
    """
    Juega una ronda de BlackJack simplificado contra la banca.
    Parametros:
- puntaje (int): el puntaje disponible del jugador.
- apuesta_actual (int): la apuesta seleccionada (no mayor al puntaje).
    Return:
- int: el puntaje actualizado luego de la ronda.
    """
    print(f"Apuesta de la ronda: {apuesta_actual}")
    mano_jugador = repartir_mano_inicial()
    mano_banca = repartir_mano_inicial()
    print(f"Banca: {mano_banca[0]} [?]")

    mano_jugador = jugar_turno_jugador(mano_jugador)
    valor_jugador = calcular_valor_mano(mano_jugador)

    if valor_jugador > 21:
        print(f"Te pasaste de 21. La carta oculta de la banca era: {mano_banca[1]}")
    else:
        mano_banca = jugar_turno_banca(mano_banca)
    valor_banca = calcular_valor_mano(mano_banca)

    ganador = determinar_resultado_blackjack(valor_jugador, valor_banca)
    if ganador == "Jugador":
        puntaje += apuesta_actual * 2
        print(f"Ganaste la ronda! Recibis {apuesta_actual * 2} puntos.")
    elif ganador == "Banca":
        puntaje -= apuesta_actual
        print(f"Perdiste la ronda. Perdes {apuesta_actual} puntos.")
    else:
        print("Push: empate, se devuelve la apuesta.")

    print(f"Puntaje actual: {puntaje}")
    return puntaje