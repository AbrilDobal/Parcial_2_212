# MODULO funciones_casino: Tragamonedas, BlackJack simplificado y Sopa de Letras.
# Desarrollado estrictamente con los apuntes y métodos básicos de la cursada.
import random


# ============================ VALIDACIONES Y ENTRADA DE DATOS ============================

def verificar_es_digito(caracter: str) -> bool:
    if caracter >= "0" and caracter <= "9":
        es_digito = True
    else:
        es_digito = False
    return es_digito


def verificar_es_cadena_entera(texto: str) -> bool:
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


# ============================ APUESTA Y RANKING (CON ARCHIVOS DE TEXTO/CSV) ============================

def ajustar_apuesta(apuesta_actual: int, puntaje: int) -> int:
    if apuesta_actual > puntaje:
        apuesta = puntaje
        print(f"La apuesta se ajusto al puntaje disponible: {apuesta}")
    else:
        apuesta = apuesta_actual
    return apuesta


def cambiar_apuesta(apuesta_actual: int, puntaje: int) -> int:
    nueva_apuesta = solicitar_entero_validado(f"Ingrese el nuevo valor de apuesta (1-{puntaje}): ", 1, puntaje)
    print(f"Apuesta actualizada a: {nueva_apuesta}")
    return nueva_apuesta


def actualizar_ranking(nombre_jugador: str, puntaje_actual: int) -> None:
    """
    Lee el archivo 'ranking.csv' (formato Nombre,Puntaje), actualiza o agrega
    al jugador manteniendo su puntaje máximo, ordena descendentemente y guarda el Top 10.
    Todo utilizando lectura/escritura básica de archivos de texto vista en los apuntes.
    """
    lista_ranking = []
    
    # 1. Lectura del archivo CSV existente (si existe)
    try:
        with open("ranking.csv", "r") as archivo:
            datos = archivo.read()
            datos_limpios = datos.strip()
            if len(datos_limpios) > 0:
                lineas = datos_limpios.split("\n")
                for i in range(len(lineas)):
                    partes = lineas[i].split(",")
                    if len(partes) == 2:
                        jugador = {
                            "nombre": partes[0],
                            "puntaje": int(partes[1])
                        }
                        lista_ranking += [jugador]
    except:
        # Si el archivo no existe, se inicia una lista vacía
        lista_ranking = []

    # 2. Buscar si el jugador ya existe para actualizar su puntaje máximo
    encontrado = False
    for i in range(len(lista_ranking)):
        if lista_ranking[i]["nombre"] == nombre_jugador:
            encontrado = True
            if puntaje_actual > lista_ranking[i]["puntaje"]:
                lista_ranking[i]["puntaje"] = puntaje_actual
            break

    # Si no existe, lo agregamos
    if encontrado == False:
        nuevo_jugador = {
            "nombre": nombre_jugador,
            "puntaje": puntaje_actual
        }
        lista_ranking += [nuevo_jugador]

    # 3. Ordenamiento Burbuja Descendente por puntaje (visto en los apuntes)
    for i in range(len(lista_ranking) - 1):
        for j in range(i + 1, len(lista_ranking)):
            if lista_ranking[i]["puntaje"] < lista_ranking[j]["puntaje"]:
                aux = lista_ranking[i]
                lista_ranking[i] = lista_ranking[j]
                lista_ranking[j] = aux

    # 4. Guardar nuevamente en el archivo CSV (Top 10)
    with open("ranking.csv", "w") as archivo:
        limite = 10
        if len(lista_ranking) < 10:
            limite = len(lista_ranking)
            
        for i in range(limite):
            nombre = lista_ranking[i]["nombre"]
            puntaje = lista_ranking[i]["puntaje"]
            archivo.write(f"{nombre},{puntaje}\n")


def mostrar_ranking() -> None:
    """
    Muestra por pantalla el ranking histórico leyendo el archivo 'ranking.csv'.
    """
    print("\n================ RANKING HISTORICO (TOP 10) ================")
    try:
        with open("ranking.csv", "r") as archivo:
            datos = archivo.read()
            datos_limpios = datos.strip()
            if len(datos_limpios) == 0:
                print("Aun no hay registros en el ranking.")
            else:
                print(f"{'Posicion':<10} | {'Jugador':<15} | {'Puntaje Maximo':<10}")
                print("-" * 45)
                lineas = datos_limpios.split("\n")
                for i in range(len(lineas)):
                    partes = lineas[i].split(",")
                    if len(partes) == 2:
                        posicion = i + 1
                        nombre = partes[0]
                        puntaje = partes[1]
                        print(f"{posicion:<10} | {nombre:<15} | {puntaje:<10}")
    except:
        print("Aun no hay registros en el ranking.")
    print("=" * 52)


# ============================ TRAGAMONEDAS ============================

def generar_fila_tragamonedas() -> list:
    caracteres = ["A", "B", "C", "D", "E", "0", "7"]
    fila = []
    for _ in range(3):
        indice = random.randint(0, len(caracteres) - 1)
        fila += [caracteres[indice]]
    return fila


def evaluar_fila_tragamonedas(fila: list) -> str:
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


# ============================ BLACKJACK ============================

def crear_carta_aleatoria() -> str:
    cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    indice = random.randint(0, len(cartas) - 1)
    return cartas[indice]


def calcular_valor_carta(carta: str) -> int:
    if carta == "A":
        valor = 11
    elif carta == "J" or carta == "Q" or carta == "K":
        valor = 10
    else:
        valor = int(carta)
    return valor


def calcular_valor_mano(mano: list) -> int:
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
    texto = ""
    for i in range(len(mano)):
        if i > 0:
            texto += " "
        texto += mano[i]
    return texto


def repartir_mano_inicial() -> list:
    return [crear_carta_aleatoria(), crear_carta_aleatoria()]


def jugar_turno_jugador(mano_jugador: list) -> list:
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


# ============================ SOPA DE LETRAS ============================

# ============================ SOPA DE LETRAS ============================

def obtener_coleccion_palabras() -> list:
    """
    Retorna una colección de 15 palabras disponibles para la Sopa de Letras[cite: 1, 4].
    Return:
- list: lista de palabras (str).
    """
    return [
        "PYTHON", "MATRIZ", "PROGRAMACION", "JUEGO", "ALGORITMO",
        "SISTEMA", "VARIABLES", "PUNTAJE", "APUESTA", "FUNCION",
        "CODIGO", "LISTA", "DICCIONARIO", "COMPUTADORA", "CASINO"
    ]


def inicializar_matriz_sopa() -> list:
    """
    Inicializa una matriz de 15x15 con espacios vacíos[cite: 1, 4].
    Return:
- list: matriz vacía de 15x15.
    """
    matriz = []
    for _ in range(15):
        fila = []
        for _ in range(15):
            fila += [" "]
        matriz += [fila]
    return matriz


def jugar_sopa_de_letras(puntaje: int, apuesta_actual: int) -> int:
    """
    Desarrolla el juego de Sopa de Letras según los requisitos de la consigna[cite: 1, 4].
    Parametros:
- puntaje (int): puntaje actual.
- apuesta_actual (int): apuesta seleccionada.
    Return:
- int: puntaje actualizado.
    """
    print("\n--- JUEGO: SOPA DE LETRAS ---")
    
    # 1. Seleccionar aleatoriamente 8 palabras de una colección de 15 palabras disponibles[cite: 1, 4]
    coleccion = obtener_coleccion_palabras()
    palabras_ocultas = []
    
    while len(palabras_ocultas) < 8:
        idx = random.randint(0, len(coleccion) - 1)
        palabra_elegida = coleccion[idx]
        
        repetida = False
        for p in range(len(palabras_ocultas)):
            if palabras_ocultas[p] == palabra_elegida:
                repetida = True
                break
                
        if repetida == False:
            palabras_ocultas += [palabra_elegida]

    # 2. Generar matriz de 15x15 caracteres (letras mayúsculas)[cite: 1, 4]
    matriz = inicializar_matriz_sopa()

    # 3. Ubicar las palabras seleccionadas en la matriz (Horizontal izq->der y Vertical arriba->abajo)[cite: 1, 4]
    for p in range(len(palabras_ocultas)):
        palabra = palabras_ocultas[p]
        colocada = False
        intentos = 0
        while colocada == False and intentos < 200:
            orientacion = random.randint(0, 1) # 0: Horizontal, 1: Vertical
            if orientacion == 0: # Horizontal
                fila_idx = random.randint(0, 14)
                col_idx = random.randint(0, 15 - len(palabra))
                espacio_libre = True
                for c in range(len(palabra)):
                    if matriz[fila_idx][col_idx + c] != " ":
                        espacio_libre = False
                if espacio_libre == True:
                    for c in range(len(palabra)):
                        matriz[fila_idx][col_idx + c] = palabra[c]
                    colocada = True
            else: # Vertical
                fila_idx = random.randint(0, 15 - len(palabra))
                col_idx = random.randint(0, 14)
                espacio_libre = True
                for f in range(len(palabra)):
                    if matriz[fila_idx + f][col_idx] != " ":
                        espacio_libre = False
                if espacio_libre == True:
                    for f in range(len(palabra)):
                        matriz[fila_idx + f][col_idx] = palabra[f]
                    colocada = True
            intentos += 1

    # 4. Completar las celdas vacías restantes con letras mayúsculas aleatorias[cite: 2, 5]
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(15):
        for j in range(15):
            if matriz[i][j] == " ":
                matriz[i][j] = letras[random.randint(0, len(letras) - 1)]

    # 5. Mostrar la matriz por pantalla para que el jugador comience a buscar[cite: 2, 5]
    print("\n      ", end="")
    for j in range(15):
        print(f"{j:2} ", end="")
    print()
    print("     " + "-" * 45)

    for i in range(15):
        fila_str = f"{i:2} | "
        for j in range(15):
            fila_str += f" {matriz[i][j]} "
        print(fila_str)

    # 6. Desarrollo del juego: 10 intentos para encontrar las 8 palabras[cite: 2, 5]
    intentos_restantes = 10
    palabras_encontradas = []

    while intentos_restantes > 0 and len(palabras_encontradas) < 8:
        print(f"\nPalabras encontradas: {len(palabras_encontradas)}/8 | Intentos restantes: {intentos_restantes}")
        intento = input("Ingrese la palabra que desea marcar en la matriz (o escriba SALIR para abandonar): ").strip().upper()

        if intento == "SALIR":
            print("Has decidido abandonar la partida.")
            break

        # Verificar si la secuencia ingresada corresponde a alguna palabra oculta y evitar contarla más de una vez[cite: 2, 5]
        es_valida = False
        ya_encontrada = False

        for p in range(len(palabras_ocultas)):
            if palabras_ocultas[p] == intento:
                es_valida = True
                break

        for p in range(len(palabras_encontradas)):
            if palabras_encontradas[p] == intento:
                ya_encontrada = True
                break

        if es_valida == True and ya_encontrada == False:
            print(f"¡Correcto! La palabra '{intento}' existe en la matriz y se contabiliza como encontrada.")
            palabras_encontradas += [intento]
            intentos_restantes -= 1
        elif es_valida == True and ya_encontrada == True:
            print("Esa palabra ya fue contabilizada anteriormente. No se puede repetir.")
            intentos_restantes -= 1
        else:
            print("Selección incorrecta. La palabra ingresada no se encuentra en la matriz.")
            intentos_restantes -= 1

    # 7. Sistema de apuestas y recompensas según la cantidad de palabras encontradas[cite: 2, 3, 5]
    cant = len(palabras_encontradas)
    print(f"\n--- FIN DE LA PARTIDA ---")
    print(f"Palabras encontradas en total: {cant}")

    if cant <= 1:
        print("Resultado: Pierde la apuesta[cite: 2, 5].")
        puntaje -= apuesta_actual
    elif cant <= 3:
        print("Resultado: Recupera la apuesta[cite: 2, 5].")
    elif cant <= 5:
        ganancia = int(apuesta_actual * 0.5)
        puntaje += ganancia
        print(f"Resultado: Gana 50% adicional (+{ganancia} puntos netos)[cite: 2, 5].")
    elif cant <= 7:
        ganancia = apuesta_actual
        puntaje += ganancia
        print(f"Resultado: Gana 100% adicional (+{ganancia} puntos netos)[cite: 2, 5].")
    elif cant <= 9:
        ganancia = int(apuesta_actual * 1.5)
        puntaje += ganancia
        print(f"Resultado: Gana 150% adicional (+{ganancia} puntos netos)[cite: 2, 5].")
    else:
        ganancia = apuesta_actual * 2
        puntaje += ganancia
        print(f"Resultado: Gana 200% adicional (+{ganancia} puntos netos)[cite: 2, 5].")

    print(f"Puntaje actual: {puntaje}")
    return puntaje