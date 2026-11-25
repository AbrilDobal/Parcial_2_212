# Listas (COLECCION)
# es un tipo de dato nuevo: list

# CARACTERISTICAS de listas:
# 1) Heterogeneas: pueden almacenar distintos tipos de datos.
# 2) Indexable: cada elemento tiene asignado un indice numerico entero, por defecto empiezan en 0.
# 3) Iterables: una estructura repetitiva puede recorrer la lista.
# 4) Ordenadas: mantienen un orden. El orden de los indices. (El primer elemento de la lista esta en indice 0).
# 5) Mutable: se puede modificar despues de ser creada.

# mi_lista_vacia = [] # Corchetes
# print(mi_lista_vacia, type(mi_lista_vacia)) # [] list

#             0  1    2      3      4     5  6   7    8
# otra_lista = [5, 7, 8.555, "Juan", True, -3, 0, 100, None] # una lista que almacena 8 enteros.
# print(otra_lista)

# lista_notas = [5, 6, 2, 10, 8, 2, 8, 9, 6]
#                    0        1       2       3       4
# lista_nombres = ["Juan", "Jose", "Sofia", "Ana", "Rodri"]

# Lectura de un elemento especifico de la lista
# mi_dato = otra_lista[3]
# print(mi_dato)
# print(otra_lista[7]) # 100

# Escritura de un elemento especifico de la lista
# otra_lista[2] = 3.14 # Asignamos 3.14 en el indice 2, pisando el valor anterio (8.555)
# print(otra_lista)



# AGREGAR UN NUEVO DATO A LA LISTA (con syntaxis algoritmica)

# lista = ["Juan"]  
# print(lista, id(lista))   #   876
# lista = ["Juan"] + ["Rodri"] # CREA UNA NUEVA LISTA
# print(lista, id(lista)) # 962
# #  lista = ["Juan", "Rodri"] + ["Sofia", "Ana"]
# lista += ["Sofia", "Ana"] # MANTIENE LA LISTA ORIGINAL
# print(lista, id(lista)) # 962

# int + int -> suma
# str + str -> concantea
# list + list -> union de listas
# int + str -> ERROR.


#           0       1       2
#lista = ["Juan", "Pepe", "Sofia"]

#print(lista[2]) # Sofia
# print(lista[3]) # Si se pasan del indice, arroja error.

# lista += ["Rodri"]
# print(lista[3]) # Rodri

#lista = ["Rodri"] + lista
# lista = lista + ["Rodri"]
#                  0        1      2       3 
#print(lista) # ["Rodri", "Juan", "Pepe", "Sofia"]



# Indices Negativos (Python)
#          0        1       2         3        4         5         6       7      8        9
# lista = ["Juan", "Pepe", "Sofia", "Mariel", "Gaston", "Yanina", "Jose", "Maria", "Ana", "Rodri"]

# print(lista[-1]) # -1 es el indice del ultimo elemento.
# print(lista[-2]) # -2 es el anteultimo indice de la lista.


# Funcion len() -> length
# Funcion len: mide cualquier objeto iterable. Devuelve la cantidad de elementos que lo componen.

# largo_lista = len(lista)
# print("El largo de la lista es:", largo_lista) # 10

# print("El largo de la lista es:", len(lista)) # 10


# ultimo_indice = len(lista) - 1
# anteultimo = len(lista) - 2
# print(lista[ultimo_indice])
# print(lista[anteultimo])


# print(lista[-1])
# print(lista[len(lista) - 1])
# print(lista[-2])
# print(lista[len(lista) - 2])




# Formas de recorrer / iterar una lista:

#          0        1       2
# lista = ["Juan", "Pepe", "Sofia"]

# un_nombre = lista[1]
# print(un_nombre)
# un_nombre = "Jose"
# print(un_nombre)
# print(lista)

# print(lista) # Print Prohibido!

# # Solo lectura.
# for nombre in lista:
#     nombre = "NADA"
#     print(nombre)
#     #nombre = "NADA"

# print(lista) # ["Juan", "Pepe", "Sofia"]


# For con indices (Mucho mas poderoso)
#          0        1      2          3       4
# lista = ["Juan", "Pepe", "Sofia", "Rodrigo", "Ana"]
# print(lista, id(lista))

#   [0, 1, 2, 3, 4]
# largo_lista = len(lista)
#for indice in range(largo_lista): # [0, 1, 2, 3, 4]
# for i in range(len(lista)):
#     print(i, lista[i])
    
# SOBRE ESCRITURA DE LOS ELEMENTOS.
# for i in range(len(lista)):
#     print(lista[i])
#     lista[i] = "NADA"
    
# print(lista, id(lista)) # ["NADA","NADA","NADA","NADA","NADA"]




# # Agregar nombres a una lista vacia.
# lista = []
# # Ingresar por input 3 nombres y agregarlos a la lista.
# # [0, 1, 2]
# for _ in range(3): # range(0) -> DESDE 0, HASTA 0, SALTO +1
#     nombre = input("Ingrese un nombre: ")
#     # [] += ["Juan"]
#     lista += [nombre]

# print(lista)


# Iteramos una lista con bucle while:
#          [0,       1,      2,        3,      4]
# lista = ["Juan", "Pepe", "Sofia", "Rodrigo", "Ana"]

# contador_indices = 0
# while contador_indices < len(lista):
#     print(lista[contador_indices])
#     contador_indices += 1

# # 
# for i in range(len(lista)): # len(lista) -> 5 -> range(5) -> [0, 1, 2, 3, 4]
#     print(lista[i])



# #                 4
# cant_letras = len("hola") # Medimos la cantidad de elementos.
# # indices, numeros enteros que por defecto empiezan en 0.
# range(3) # -> [0, 1, 2]
# for index in range(3):
#     print(lista[index])


# lista = [6, 5, 3, 2, 1, 6]
# cadena = "hola mundo"
# print("Cantidad de elementos en la lista:", len(lista)) # 6
# print("Cantidad de letras en cadena:", len(cadena)) # 10

# ctrl + C -> copiar
# ctrl + V -> Pegar
# ctrl + A -> Selecciona todo
# ctrl + } -> Comenta / Descomenta

# ============== MUTABILIDAD ================

# num_a = 5
# num_b = num_a
# num_a = 7

# print("A", num_a) # 7
# print("B", num_b) # 5



# #            0        1       2
# lista_a = ["Juan", "Pepe", "Sofia"]
# # print(len(lista_a)) # 3
# lista_b = ["Juan", "Pepe", "Sofia"]
# lista_a[1] = "Jose"
# # lista_a[1] = lista_a[1] + "Jose"

# print("A", lista_a, id(lista_a)) #  [Juan Jose Sofia]
# print("B", lista_b, id(lista_b)) #  [Juan Jose Sofia]


# "Hola"
# [1, True, "Pepe"]
# print(type(lista_b[2])) # str

# # 
# print(lista_b[2][0]) # S




# ========================= Cargar una lista. ================================
# Carga secuencial: cargamos la lista desde el principio hasta el final.
# La lista tiene indices -> cargamos iterando esos indices.
# La lista esta vacia -> vamos agregando nuevos elementos a la lista.

# Lista vacia:
# lista = [] # += [elemento]

# Lista vacia inicializada.
# RGB (0-255)
# lista = [None, None, None] # lista[i] = elemento

# lista = [None] * 100 # Genera una lista de 100 elementos None
# print("W" * 5)


# Carga aleatorio: el usuario nos indica DONDE cargar el dato.

# lista = [0, 0, 255] # lista[1] = elemento
#                     lista[1] = elemento2





# ====================== PRINT PRIHIBIDO (PARA LISTAS)=====================

# lista = ["Juan", "Pepe", "Sofia"]

# print(lista) # INCORRECTA

# for i in range(len(lista)): # CORRECTA
#     # print(lista[i]) # en lineas separadas
#     print(lista[i], end=" ") # en la misma linea





# =========================== LISTAS PARALELAS ================================
lista_notas = [6, 4, 8, 2, 10, 7, 5, "Juan", "Pepe", "Sofia", "Rodrigo", "Matias", "Ana", "Gonzalo"]

lista_notas = ["Juan", 6, "Pepe", 4, "Sofia", 8, "Rodrigo", 2, "Matias", 10, "Ana", 7, "Gonzalo", 5]

#                  0        1       2          3         4       5        6
lista_notas =   [  6,       4,      8,         2,       10,      7,       5    ]
lista_nombres = ["Juan", "Pepe", "Sofia", "Rodrigo", "Matias", "Ana", "Gonzalo"]


# Deben tener el mismo tamaño.
# COMPARTEN INDICES.

for i in range(len(lista_notas)):
    print(f"{lista_nombres[i]} se saco un {lista_notas[i]}.")
