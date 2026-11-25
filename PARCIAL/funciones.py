import random

# ====================== Normalizacion =====================
def transformar_a_mayusculas(cadena: str) -> str:
    """
    Convierte las letras minúsculas (a-z) de una cadena a mayúsculas usando
    el código ASCII, sin métodos de strings. Los demás caracteres quedan igual.

    Parametros:
    -cadena (str): la cadena a convertir.

    Retorno: Return (str):
    -Una nueva cadena con las letras en mayúsculas.
    """
    resultado = ""
    for i in range(len(cadena)):
        caracter = cadena[i]
        if caracter >= "a" and caracter <= "z":
            resultado += chr(ord(caracter) - 32)
        else:
            resultado += caracter
    return resultado

# =================== Punto 1 =============================

def generar_patente() -> str:
    """
    Genera una patente aleatoria con formato AB123CD: dos letras mayúsculas
    (ASCII 65-90), tres números (ASCII 48-57) y dos letras mayúsculas.

    Parametros:
    -No recibe parametros.

    Retorno: Return (str):
    -La patente generada.
    """
    patente = ""
    for i in range(7):
        if i < 2 or i > 4: #(0 y 1) o (5 y 6)
            patente += chr(random.randint(65, 90))
        else:
            patente += chr(random.randint(48, 57))
    return patente


def buscar_patente(lista_patentes: list, patente: str) -> bool:
    """
    Busca una patente dentro de la lista, recorriéndola con índices.

    Parametros:
    -lista_patentes (list): lista de patentes donde se busca.
    -patente (str): la patente a buscar.

    Retorno: Return (bool):
    -True si la patente está en la lista.
    -False si no está.
    """
    encontrada = False
    for i in range(len(lista_patentes)):
        if lista_patentes[i] == patente:
            encontrada = True
    return encontrada


def cargar_patentes(cantidad_patentes: int, lista_general_patentes: list) -> None:
    """
    Genera la cantidad pedida de patentes únicas y las agrega al final de la
    lista general, conservando las que ya existían. Cada patente generada se
    verifica con buscar_patente: si está repetida se descarta y se genera otra.

    Parametros:
    -cantidad_patentes (int): cantidad de patentes a agregar.
    -lista_general_patentes (list): lista donde se agregan las patentes.

    Retorno: None
    """
    contador = 0
    while contador < cantidad_patentes:
        patente = generar_patente()
        if not buscar_patente(lista_general_patentes, patente):
            lista_general_patentes += [patente]
            contador += 1


# ========================== Punto 2 =========================

def validar_patente(patente: str) -> bool:
    """
    Verifica que la patente tenga formato LLNNNLL: 7 caracteres, con dos
    letras mayúsculas, tres caracteres numéricos y dos letras mayúsculas.

    Parametros:
    -patente (str): la patente a validar.

    Retorno: Return (bool):
    -True si el formato es correcto.
    -False si el formato es incorrecto.
    """
    es_valida = True

    if len(patente) != 7:
        es_valida = False
    else:
        for i in range(7):
            caracter = patente[i]
            if i < 2 or i > 4:
                if caracter < "A" or caracter > "Z":
                    es_valida = False
            else:
                if caracter < "0" or caracter > "9":
                    es_valida = False

    return es_valida

# ======================== Punto 3A ===========================
def rebanar_cadena_casero(cadena: str, desde: int, hasta: int, salto: int = 1) -> str:
    """
    Extrae una porción de una cadena sin usar slicing: recorre los índices
    desde "desde" (incluido) hasta "hasta" (excluido), de "salto" en "salto",
    y va concatenando los caracteres.

    Parametros:
    -cadena (str): la cadena de la que se extrae la porción.
    -desde (int): índice donde empieza la porción (incluido).
    -hasta (int): índice donde termina la porción (excluido).
    -salto (int): de cuánto en cuánto avanza. 1 por defecto.

    Retorno: Return (str):
    -La porción de la cadena. Por ejemplo, "125" para ("AB125DC", 2, 5).
    """
    extracto = ""

    for i in range(desde, hasta, salto):
        extracto += cadena[i]

    return extracto

def obtener_numero_patente(patente: str) -> int:
    """
    Obtiene el numero de una patente, es decir, sus tres caracteres
    numericos (posiciones 2, 3 y 4) convertidos a entero.

    Args:
        patente (str): una patente con formato AB123CD.

    Returns:
        int: El numero de la patente. Por ejemplo, 125 para "AB125CD"
    """
    return int(rebanar_cadena_casero(patente, 2, 5))


# def obtener_patente_por_antiguedad(lista_patentes: list):
#     """_summary_

#     Args:
#         lista_patentes (list): _description_
#     """
#     patente_mas_nueva = lista_patentes[0]
#     patente_mas_vieja = lista_patentes[0]

#     for patente in lista_patentes:# 1 2 3 4 5 6 7 
#         numero = obtener_numero_patente(patente)# posicion 2 a la 5 de la patente -> entero
#         if numero < obtener_numero_patente(patente_mas_vieja):#[2:5] slicing #2 3 4
#             patente_mas_vieja = patente
#         if numero > obtener_numero_patente(patente_mas_nueva):
#             patente_mas_nueva = patente

    #datos = [patente_mas_nueva, patente_mas_vieja]
#     return datos


def obtener_patente_mas_vieja(lista_patentes: list) -> str:
    """
    Busca la patente más vieja, es decir, la de menor número. Si hay varias
    con el mismo número, devuelve la primera de la lista.

    Parametros:
    -lista_patentes (list): lista de patentes almacenadas. No puede estar vacía.

    Retorno: Return (str):
    -La patente más vieja.
    """
    patente_mas_vieja = lista_patentes[0]
    min_numero = obtener_numero_patente(patente_mas_vieja)

    for i in range(1, len(lista_patentes)):
        numero_actual = obtener_numero_patente(lista_patentes[i])

        if numero_actual < min_numero:
            min_numero = numero_actual
            patente_mas_vieja = lista_patentes[i]

    return patente_mas_vieja


def obtener_patente_mas_nueva(lista_patentes: list) -> str:
    """
    Busca la patente más nueva, es decir, la de mayor número. Si hay varias
    con el mismo número, devuelve la primera de la lista.

    Parametros:
    -lista_patentes (list): lista de patentes almacenadas. No puede estar vacía.

    Retorno: Return (str):
    -La patente más nueva.
    """
    patente_mas_nueva = lista_patentes[0]
    max_numero = obtener_numero_patente(patente_mas_nueva)

    for i in range(1, len(lista_patentes)):
        numero_actual = obtener_numero_patente(lista_patentes[i])

        if numero_actual > max_numero:
            max_numero = numero_actual
            patente_mas_nueva = lista_patentes[i]

    return patente_mas_nueva

# ======================= Punto 3B ===========================

def informar_porcentajes_letra_inicial(lista_patentes: list) -> None:
    """
    Calcula e informa por consola el porcentaje de patentes que comienzan con
    cada letra del abecedario (A-Z), generando las letras con chr() desde su
    código ASCII (65 a 90).

    Parametros:
    -lista_patentes (list): lista de patentes almacenadas. No puede estar vacía.

    Retorno: None
    """
    total = len(lista_patentes)
    for codigo in range(65, 91):
        letra = chr(codigo)
        contador = 0
        for i in range(total):
            if lista_patentes[i][0] == letra:
                contador += 1
        porcentaje = contador * 100 / total
        print(f"{letra}: {porcentaje:.2f}%")


# ===================== PUNTO 4 =====================

def intercambiar_elementos(lista: list, i: int, j: int) -> None:
    """
    Intercambia (swap) dos elementos de una lista mediante una variable auxiliar.

    Parametros:
    -lista (list): la lista donde se hace el intercambio.
    -i (int): índice del primer elemento.
    -j (int): índice del segundo elemento.

    Retorno: None
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def ordenar_patentes_burbuja(lista_patentes: list, criterio: str) -> None:
    """
    Ordena la lista de patentes en el mismo lugar con el método de burbujeo,
    comparando las patentes completas.

    Parametros:
    -lista_patentes (list): la lista de patentes a ordenar.
    -criterio (str): "ASC" para ordenar de menor a mayor o "DESC" para ordenar de mayor a menor.

    Retorno: None
    """
    total = len(lista_patentes)
    for i in range(total - 1):
        for j in range(i + 1, total):
            if criterio == "ASC" and lista_patentes[i] > lista_patentes[j]:
                intercambiar_elementos(lista_patentes, i, j)
            elif criterio == "DESC" and lista_patentes[i] < lista_patentes[j]:
                intercambiar_elementos(lista_patentes, i, j)


def mostrar_patentes(lista_patentes: list) -> None:
    """
    Muestra cada patente de la lista, una por línea, por consola.

    Parametros:
    -lista_patentes (list): lista de patentes a mostrar.

    Retorno: None
    """
    for i in range(len(lista_patentes)):
        print(lista_patentes[i])