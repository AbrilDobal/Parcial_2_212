# Matrices: listas de listas / listas anidadas.
import random as r

lista = ["a", "b", "c"]

# matriz = [["a", "b", "c"], ["d", "e", "z"]]

# Matriz 2x3
# 2 filas (horizontalmente) y 3 columnas (verticalmente)
#           0    1    2
matriz = [["a", "b", "c"], # 0
          ["d", "e", "z"]] # 1

# Es posible hacer matrices de mas de dos dimensiones.

# print(type(matriz)) # list
# print(matriz) # [["a", "b", "c"], ["d", "e", "z"]] la matriz completa, en la misma linea
# print(matriz[0]) # ["a", "b", "c"] -> Primer fila de la matriz
# print(matriz[1]) # ["d", "e", "z"] -> Segunda fila de la matriz

#          [fila][columna]
# print(matriz[1][1]) # "e"
# print(matriz[1][0]) # "d"

# fila_uno = matriz[0]
# print(fila_uno[1]) # "b"

# Modificar un indice de la matriz:
# matriz[1][2] = "f"
# print(matriz) # PRINT PROHIBIDO  [["a", "b", "c"], ["d", "e", "f"]]


# Iteramos una lista:
# for i in range(len(lista)):
#     print(lista[i], end=" ")

# Iteramos una matriz:
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end=" ")
#     print()

# len(matriz) -> Nos da la CANTIDAD de FILAS de la matriz.
# len(matriz[i]) -> Nos da la CANTIDAD de COLUMNAS de CADA fila.

# For each (solo lectura)
# for fila in matriz:
#     for valor in fila:
#         print(valor, end=" ")
#     print()


def mostrar_matriz(matriz:list[list])->None:
    """Documentacion"""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

# INICIALIZAR UNA MATRIZ

# def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial:any=None)->list[list]:
#     """Documentacion"""
#     matriz = []
#     for _ in range(cant_filas): # 3 iteraciones (1 para cada fila)
#         matriz += [[valor_inicial] * cant_columnas] # [[None, None], [None, None], [None, None]]
#         # fila = [valor_inicial] * cant_columnas # [None, None]
#         # matriz += [fila]
#     # matriz = [fila] * cant_filas # NO SIRVE; YA QUE COPIA Y PEGA LA FILA
#     return matriz

def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial:any=None)->list[list]:
    """Documentacion"""
    matriz = []
    for _ in range(cant_filas): 
        fila = []
        for _ in range(cant_columnas):
            fila += [valor_inicial]
        matriz += [fila]
    return matriz

def cargar_matriz_secuencialmente(matriz:list[list])->None:
    """Documentacion"""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valor_aleatorio = r.randint(1, 9)
            matriz[i][j] = valor_aleatorio
            # matriz[i][j] = input("Ingrese un nombre: ")

def cargar_matriz_aleatoriamente(matriz:list[list])->None:
    """Documentacion"""
    respuesta = "S"
    while respuesta != "N":
        dato_ingresado = input("Ingrese un nombre: ")
        indice_fila = int(input("Ingrese el indice de FILA: "))
        indice_columna = int(input("Ingrese el indice de COLUMNA: "))
        matriz[indice_fila][indice_columna] = dato_ingresado
        respuesta = input("Desea seguir ingresando datos? S/N: ")


# Matriz de 3x2
# [[None, None],
#  [None, None],
#  [None, None]]

# matriz = inicializar_matriz(3, 2)
# mostrar_matriz(matriz)
# print("===============================")
# matriz[0][0] = False
# cargar_matriz_secuencialmente(matriz)
# cargar_matriz_aleatoriamente(matriz)
# mostrar_matriz(matriz)

def sumar_matrices(matriz_a:list[list], matriz_b:list[list])->list[list] | None:
    """Documentacion"""
    retorno = None
    #  Matriz NO vacia    y   Ambas Matr, == cant de Filas.  y   Matriz Tenga columnass y  Ambas Matr, coinciden en cant de columnas
    if len(matriz_a) != 0 and len(matriz_a) == len(matriz_b) and len(matriz_a[0]) != 0 and len(matriz_a[0]) == len(matriz_b[0]):
        matriz_c = inicializar_matriz(len(matriz_a), len(matriz_a[0]))
        for i in range(len(matriz_a)):
            for j in range(len(matriz_a[i])):
                matriz_c[i][j] = matriz_a[i][j] + matriz_b[i][j]
        retorno = matriz_c
    return retorno

def multiplicar_matriz_escalar(matriz:list[list], escalar:int)->list[list] | None:
    """Documentacion"""
    retorno = None
    if len(matriz) != 0 and len(matriz[0]) != 0:
        matriz_r = inicializar_matriz(len(matriz), len(matriz[0]))
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz_r[i][j] = matriz[i][j] * escalar
        retorno = matriz_r
    return retorno

matriz_a = inicializar_matriz(3, 4)
# matriz_b = inicializar_matriz(3, 4)
cargar_matriz_secuencialmente(matriz_a)
# cargar_matriz_secuencialmente(matriz_b)

mostrar_matriz(matriz_a)
print("===============================")
matriz_r = multiplicar_matriz_escalar(matriz_a, 2)
mostrar_matriz(matriz_r)
# mostrar_matriz(matriz_b)
# matriz_r = sumar_matrices(matriz_a, matriz_b)
# print("===============================")
# if matriz_r != None:
#     mostrar_matriz(matriz_r)
#     print("===============================")
#     print(matriz_r) # PRINT PROHIBIDO
# else:
#     print("Error, la matriz no se pudo generar.")