# ORDENAMIENTO
# Bubble Sort (UNA DE SUS VERSIONES) ASCENDENTE

# v0.5
# def ordenar_lista(lista:list):
#     """Documentacion"""
#     for i in range(len(lista) - 1):
#         for j in range(i + 1, len(lista)):
#             # print("I", i, "J", j)
#             if lista[i] > lista[j]: 
#                 # Intercambio o SWAP
#                 aux = lista[i]
#                 lista[i] = lista[j] 
#                 lista[j] = aux
                

# EXCLUIMOS EL ULTIMO ELEMENTO
#        0  1  2  3  4
# lista = [5, 3, 7, 2, 3]
# len(lista) ->         5 
# len(lista) - 1 ->     4
# range(4)  ->          [0, 1, 2, 3]

#            0  1  2  3  4  5   6  7
# lista_dos = [5, 3, 7, 2, 3, 1, -5, 0]
# len(lista) ->       8  
# len(lista) - 1 ->   7 
# range(4)  ->        [0, 1, 2, 3, 4, 5, 6] 


# lista_nombres = ["Sofia", "Juan", "Pepe", "Rodrigo", "Alan", "Jose"]


# ordenar_lista(lista)

# i = [0, 1, 2, 3]
# j =   [1, 2, 3, 4]
# j =      [2, 3, 4]
# j =         [3, 4]
# j =            [4]

# i j

# 0 1
# 0 2
# 0 3
# 0 4

# 1 2
# 1 3
# 1 4

# 2 3
# 2 4

# 3 4



# SWAP / INTERCAMBIO:
# num_a = 5
# num_b = 7

# aux = num_a  # aux = 5
# num_a = num_b  # num_a = 7, num_b = 7
# num_b = aux  # num_a = 7, num_b = 5

# aux = num_b
# num_b = num_a
# num_a = aux

# print(num_a) # 7
# print(num_b) # 5

# print(lista) # PRINT PROHIBIDO
# ordenar_lista(lista)
# print(lista) # PRINT PROHIBIDO

# print(lista_dos) # PRINT PROHIBIDO
# ordenar_lista(lista_dos)
# print(lista_dos) # PRINT PROHIBIDO

# print(lista_nombres) # PRINT PROHIBIDO
# ordenar_lista(lista_nombres)
# print(lista_nombres) # PRINT PROHIBIDO



# v0.9
def ordenar_lista(lista:list, ascendente:bool=True):
    """Documentacion"""
    if ascendente == True:
        for i in range(len(lista) - 1):
            for j in range(i + 1, len(lista)):
                if lista[i] > lista[j]: 
                    aux = lista[i]
                    lista[i] = lista[j] 
                    lista[j] = aux
    else:
        for i in range(len(lista) - 1):
            for j in range(i + 1, len(lista)):
                if lista[i] < lista[j]: 
                    aux = lista[i]
                    lista[i] = lista[j] 
                    lista[j] = aux

def intercambiar_elementos(lista:list, i:int, j:int):
    """Documentacion"""
    aux = lista[i]
    lista[i] = lista[j] 
    lista[j] = aux


#v1.0
def ordenar_lista(lista:list, ascendente:bool=True)->bool:
    """Documentacion"""
    retorno = True
    if len(lista) < 2:
        retorno = False
    for i in range(len(lista) - 1): 
        for j in range(i + 1, len(lista)):
            if (ascendente == True and lista[i] > lista[j]) or (
                ascendente == False and lista[i] < lista[j]): 
                intercambiar_elementos(lista, i, j) # Swap en una funcion aparte
                # aux = lista[i]
                # lista[i] = lista[j] 
                # lista[j] = aux
    return retorno

lista = [5, 3, 7, 2, 3]
lista_dos = [5, 3, 7, 2, 3, 1, -5, 0]
lista_nombres = ["Sofia", "Juan", "Pepe", "Rodrigo", "Alan", "Jose"]

print(lista) # PRINT PROHIBIDO
ordenar_lista(lista)
print(lista) # PRINT PROHIBIDO

print(lista_dos) # PRINT PROHIBIDO
ordenar_lista(lista_dos, False)
print(lista_dos) # PRINT PROHIBIDO

print(lista_nombres) # PRINT PROHIBIDO
ordenar_lista(lista_nombres)
print(lista_nombres) # PRINT PROHIBIDO




# LISTAS PARALELAS:

#                   0        1      2
lista_nombres = ["Sofia", "Juan", "Pepe"]
lista_notas =   [  7,       2,      4   ]

def ordenar_listas_paralelas(lista:list, lista_dos:list, ascendente:bool=True):
    """Documentacion"""
    for i in range(len(lista) - 1): 
        for j in range(i + 1, len(lista)):
            if (ascendente == True and lista[i] > lista[j]) or (
                ascendente == False and lista[i] < lista[j]): 
                intercambiar_elementos(lista, i, j)
                intercambiar_elementos(lista_dos, i, j)

# Por nombres, ASC.
# ordenar_listas_paralelas(lista_nombres, lista_notas)
# print(lista_nombres)
# print(lista_notas)

# Por nota, DESC.
# ordenar_listas_paralelas(lista_notas, lista_nombres, False)
# print(lista_nombres)
# print(lista_notas)

# Por nota, ASC.
# ordenar_listas_paralelas(lista_notas, lista_nombres)
# print(lista_nombres)
# print(lista_notas)

# Por nombres, DESC.
ordenar_listas_paralelas(lista_nombres, lista_notas, False)
print(lista_nombres)
print(lista_notas)

# el primer for itera desde el primer hasta el penultimo y el for de j empieza desde del proximo y va hasta el ultimo. 
# swap para no perder el elemento lo guardamos en un aux, y hacemos el intercambio 

