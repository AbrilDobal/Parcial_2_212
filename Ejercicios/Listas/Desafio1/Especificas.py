def es_positivo(numero: int) -> bool:
    """
    Determina si un numero es positivo.
    Parametros:
        - numero (int): el numero a evaluar.
    Return:
        - bool: True si es positivo, False caso contrario.
    """
    resultado = numero > 0
    return resultado


def es_negativo(numero: int) -> bool:
    """
    Determina si un numero es negativo.
    Parametros:
        - numero (int): el numero a evaluar.
    Return:
        - bool: True si es negativo, False caso contrario.
    """
    resultado = numero < 0
    return resultado


def es_par(numero: int) -> bool:
    """
    Determina si un numero es par.
    Parametros:
        - numero (int): el numero a evaluar.
    Return:
        - bool: True si es par, False caso contrario.
    """
    resultado = numero % 2 == 0
    return resultado

def es_impar(numero: int) -> bool:
    """
    Determina si un numero es impar.
    Parametros:
        - numero (int): el numero a evaluar.
    Return:
        - bool: True si es impar, False caso contrario.
    """
    resultado = numero % 2 != 0
    return resultado
