def intercambiar_elementos(lista: list, i: int, j: int):
    """Intercambia dos elementos de una lista dados sus índices."""
    aux = lista[i]
    lista[i] = lista[j] 
    lista[j] = aux

# 1) Desarrollar una función que reciba una lista y ordene sus elementos utilizando un criterio
# pasado por parámetro, devolverá un booleano indicando si pudo ordenar los elementos o
# no.

def ordenar_lista(lista: list, ascendente: bool = True) -> bool:
    retorno = True
    if len(lista) < 2:
        retorno = False
    else:
        for i in range(len(lista) - 1): 
            for j in range(i + 1, len(lista)):
                if (ascendente and lista[i] > lista[j]) or (not ascendente and lista[i] < lista[j]): 
                    intercambiar_elementos(lista, i, j)
    return retorno

# 2) Desarrollar una función que reciba 3 listas paralelas y un criterio y las ordene utilizando
# como base la primera lista que reciba por parámetro, devolverá un booleano indicando si
# pudo ordenar los elementos o no.

def ordenar_tres_listas_paralelas(lista_1: list, lista_2: list, lista_3: list, ascendente: bool = True) -> bool:
    retorno = True
    if len(lista_1) < 2:
        retorno = False
    else:
        for i in range(len(lista_1) - 1): 
            for j in range(i + 1, len(lista_1)):
                if (ascendente and lista_1[i] > lista_1[j]) or (not ascendente and lista_1[i] < lista_1[j]): 
                    intercambiar_elementos(lista_1, i, j)
                    intercambiar_elementos(lista_2, i, j)
                    intercambiar_elementos(lista_3, i, j)
    return retorno

# 3) Desarrollar una función que reciba 2 listas paralelas y un criterio (asc/desc), si los valores
# de la lista principal son iguales, deberá ordenar las listas utilizando la segunda lista
# (Ordenamiento por doble criterio). Devolverá un booleano indicando si pudo ordenar los
# elementos o no.

def ordenar_doble_criterio(lista_1: list, lista_2: list, ascendente: bool = True) -> bool:
    retorno = True
    if len(lista_1) < 2:
        retorno = False
    else:
        for i in range(len(lista_1) - 1):
            for j in range(i + 1, len(lista_1)):
                debe_intercambiar = False
                
                # Si los elementos de la lista principal son distintos
                if lista_1[i] != lista_1[j]:
                    if ascendente == True:
                        if lista_1[i] > lista_1[j]:
                            debe_intercambiar = True
                    else:
                        if lista_1[i] < lista_1[j]:
                            debe_intercambiar = True
                else:
                    # Empate en la principal: evaluamos la segunda lista
                    if ascendente == True:
                        if lista_2[i] > lista_2[j]:
                            debe_intercambiar = True
                    else:
                        if lista_2[i] < lista_2[j]:
                            debe_intercambiar = True
                
                # Si corresponde, hacemos el swap en ambas listas
                if debe_intercambiar == True:
                    intercambiar_elementos(lista_1, i, j)
                    intercambiar_elementos(lista_2, i, j)
                    
    return retorno

# 4) Desarrollar una función que reciba una matriz y la ordene de acuerdo al criterio recibido
# por parámetro. Devolverá un booleano indicando si pudo ordenar los elementos o no

def ordenar_matriz(matriz: list, columna: int = 0, ascendente: bool = True) -> bool:
    retorno = True
    
    if len(matriz) < 2:
        retorno = False
    else:
        for i in range(len(matriz) - 1):
            for j in range(i + 1, len(matriz)):
                
                intercambiar = False
                
                if ascendente == True:
                    if matriz[i][columna] > matriz[j][columna]:
                        intercambiar = True
                else:
                    if matriz[i][columna] < matriz[j][columna]:
                        intercambiar = True
                
                if intercambiar == True:
                    aux = matriz[i]
                    matriz[i] = matriz[j]
                    matriz[j] = aux
                    
    return retorno