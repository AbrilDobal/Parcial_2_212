from validate import *


def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
    """
    Pide un numero entero por consola y lo valida.
    Parametros:
        - mensaje (str): mensaje que se imprime antes de pedir el dato.
        - mensaje_error (str): mensaje que se imprime si el dato es invalido.
        - minimo (int): valor minimo admitido (inclusive).
        - maximo (int): valor maximo admitido (inclusive).
        - reintentos (int): cantidad de veces que se vuelve a pedir el dato en caso de error.
    Return:
        - int | None: el numero validado, o None si se agotaron los reintentos.
    """
    numero = None
    intentos_restantes = reintentos
    es_valido = False
    while es_valido == False and intentos_restantes >= 0:
        texto = input(mensaje)
        es_valido = validate_number(texto, minimo, maximo, True)
        if es_valido:
            numero = int(texto)
        else:
            print(mensaje_error)
            intentos_restantes -= 1
    return numero


def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float|None:
    """
    Pide un numero flotante por consola y lo valida.
    Parametros:
        - mensaje (str): mensaje que se imprime antes de pedir el dato.
        - mensaje_error (str): mensaje que se imprime si el dato es invalido.
        - minimo (float): valor minimo admitido (inclusive).
        - maximo (float): valor maximo admitido (inclusive).
        - reintentos (int): cantidad de veces que se vuelve a pedir el dato en caso de error.
    Return:
        - float | None: el numero validado, o None si se agotaron los reintentos.
    """
    numero = None
    intentos_restantes = reintentos
    es_valido = False
    while es_valido == False and intentos_restantes >= 0:
        texto = input(mensaje)
        es_valido = validate_number(texto, minimo, maximo, False)
        if es_valido:
            numero = float(texto)
        else:
            print(mensaje_error)
            intentos_restantes -= 1
    return numero


def get_string(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> str|None:
    """
    Pide una cadena por consola y valida su longitud (prototipo extendido).
    Parametros:
        - mensaje (str): mensaje que se imprime antes de pedir el dato.
        - mensaje_error (str): mensaje que se imprime si la cadena es invalida.
        - longitud (int): cantidad maxima de caracteres admitida (inclusive).
        - reintentos (int): cantidad de veces que se vuelve a pedir el dato en caso de error.
    Return:
        - str | None: la cadena validada, o None si se agotaron los reintentos.
    """
    cadena = None
    intentos_restantes = reintentos
    es_valido = False
    while es_valido == False and intentos_restantes >= 0:
        texto = input(mensaje)
        es_valido = validate_length(texto, longitud)
        if es_valido:
            cadena = texto
        else:
            print(mensaje_error)
            intentos_restantes -= 1
    return cadena