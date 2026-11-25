from Especificas import *

def contar_positivos_negativos(lista: list) -> list:
    """
    Cuenta cuantos elementos de la lista son positivos y cuantos son negativos.
    Parametros:
        - lista (list): lista de numeros enteros.
    Return:
        - list: [cantidad_positivos, cantidad_negativos]
    """
    cantidad_positivos = 0
    cantidad_negativos = 0
    for i in range(len(lista)):
        if es_positivo(lista[i]):
            cantidad_positivos += 1
        elif es_negativo(lista[i]):
            cantidad_negativos += 1
    resultado = [cantidad_positivos, cantidad_negativos]
    return resultado


def sumar_pares(lista: list) -> int:
    """
    Suma los elementos pares de una lista de numeros.
    Parametros:
        - lista (list): lista de numeros enteros.
    Return:
        - int: la suma de los numeros pares.
    """
    suma = 0
    for i in range(len(lista)):
        if es_par(lista[i]):
            suma += lista[i]
    return suma


def mayor_impar(lista: list) -> int:
    """
    Busca el mayor numero impar de una lista.
    Parametros:
        - lista (list): lista de numeros enteros.
    Return:
        - int: el mayor numero impar encontrado (None si no hay ninguno).
    """
    mayor = None
    for i in range(len(lista)):
        if es_impar(lista[i]):
            if mayor == None or lista[i] > mayor:
                mayor = lista[i]
    return mayor


def listar_elementos(lista: list) -> None:
    """
    Muestra por pantalla todos los elementos de una lista, en el orden ingresado.
    Parametros:
        - lista (list): lista de numeros enteros.
    Return:
        None
    """
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()


def listar_pares(lista: list) -> None:
    """
    Muestra por pantalla unicamente los numeros pares de una lista.
    Parametros:
        - lista (list): lista de numeros enteros.
    Return:
        None
    """
    for i in range(len(lista)):
        if es_par(lista[i]):
            print(lista[i], end=" ")
    print()


def listar_posiciones_impares(lista: list) -> None:
    """
    Muestra por pantalla los numeros que se encuentran en posiciones (indices) impares de una lista.
    Parametros:
        - lista (list): lista de numeros enteros.
    Return:
        None
    """
    for i in range(len(lista)):
        if i % 2 != 0:
            print(lista[i], end=" ")
    print()
