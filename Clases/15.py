# TDA: Colecciones (Tuplas, Sets y Diccionarios)
import random


# ============================================= Tupla ========================================
# Caracteres que encierran una tupla -> ()
# mi_tupla = (1, 2, 3.14, True, "Hola", [1, 2], ("A", "B"))

# Caracteristicas de tuplas:
# Heterogeneas: puede almacenar distintos tipos de datos.
# Iterable: se puede recorrer con un bucle.
# Indexable: tiene indices, que empiezan en 0 y terminan en len()-1
# Ordenadas: todos los elementos estan ordenados por su indice.
# Inmutables: una vez creadas, NO se pueden modificar.

# print(mi_tupla)
# print("LEN", len(mi_tupla)) # 7

# for i in range(len(mi_tupla)):
#     print(mi_tupla[i])

# mi_tupla[0] = 0 # ERROR, las tuplas NO se pueden modificar.

# Como generar una tupla de enteros aleatorios:
# lista = []
# for i in range(5):
#     lista.append(random.randint(1, 9))
# otra_tupla = tuple(lista) # Casteamos la lista con entero aleatorios a tupla
# print(otra_tupla)

# USO de tuplas
# COLOR_ROJO = (255, 0, 0)
# COLOR_VERDE = (0, 255, 0)


# mi_tupla = (1, 2, 3.14, True, "Hola", [1, 2], ("A", "B"))
# mi_tupla[5].append(3)
# # print(mi_tupla[5]) # [1, 2]
# print(mi_tupla)

# def crear_tupla_aleatoria(cantidad:int, desde:int, hasta:int)->tuple:
#     lista = []
#     for _ in range(cantidad):
#         lista.append(random.randint(desde, hasta))
#     tupla = tuple(lista) # Casteamos la lista con entero aleatorios a tupla
#     return tupla

# def test()->tuple: # Retorna tupla
#     valor_a = random.randint(1, 9)
#     valor_b = random.randint(1, 9)
#     return valor_a, valor_b # Esta sintaxis retorna una TUPLA

# a, b = test() # Desempaquetado / Desestructuramiento de tuplas, extrae elementos en la misma linea

# c = test()
# d = c[0]
# e = c[1]
# print("A", a) # X (int)
# print("B", b) # X (int)
# print("C", c) # (x, x) (tuple)



# ============================================== Set / Conjunto ============================================:
# Set: caracteres que delimitan el set {}
# set vacio -> set()
# Caracteristicas:
# - Almacena valores que NO se pueden repetir (unicos).
# - Desordenado.
# - No es indexable.
# - Iterable (con for-each)
# - Mutable.
# - Heterogeneo. (limitado a tipos de datos inmutables)

# mi_set = {"juan", 1, False, 3.14, (2, 5), True, 3.14, "juan", (1, 3), (2, 5)}
# print(mi_set)
# # print(len(mi_set)) # Mide el set.
# # for dato in mi_set:
# #     print(dato)

# mi_set.clear()
# mi_set.add(5)
# mi_set.add(True)
# mi_set.add(5) # No lo agrega ya que tiene un 5.
# print(mi_set)


# for i in range(len(mi_set)):
#     print(mi_set[i])

# lista = ["Juan", "Pepe", "Sofia", "Juan", "Rodrigo", "Pepe"]
# nombres_unicos = set(lista) # Suprime valores repetidos.
# print(nombres_unicos)




# ============================================= Diccionarios ======================================
# Caracteres que delimitan un diccionario: {}
# Diccionario vacio -> {}
# Se compone de Items: donde cada item es un par (clave:valor).
# Caracteristicas del Diccionario:
# - Mutable.
# - Indexable: por clave.
# - Heterogeneo: en sus valores! || Claves: ideal que sean str (DEBEN SER UNICAS en un MISMO diccionario!)
# - Ordenado: segun el orden de ingreso / agregacion de elementos.
# - Iterable: 3 formas de iterar. 

#    set:        {"Pepe", "Perez", 35, 20123123}
# mi_diccionario = {"nombre":"Pepe", "apellido":"Perez", "edad": 35, "dni": 20123123}
# mi_diccionario_dos = {"nombre":"Juan", "apellido":"Lopez", "edad": 53, "dni": 20123124}
# print(mi_diccionario["nombre"]) # Pepe
# print(mi_diccionario["dni"])  # 20123123
# # mi_diccionario["apellido"] = "Lopez" # asigna un nuevo valor a la clave "apellido"
# # Metodo Update: 
# # - SI la clave NO existe: agrega un nuevo item con esa clave.
# # - SI la clave EXISTE: actualiza el valor en ESA clave.
# item_a_agregar = {"alumno_regular": True}
# mi_diccionario.update(item_a_agregar) # Agrega un item nuevo al diccionario.

# valor_a_modificar = {"edad": 36}
# mi_diccionario.update(valor_a_modificar) # Actualiza el valor en clave "edad"

# mi_diccionario.update({"alumno_regular": False}) # Actualiza el valor en clave "alumno_regular"

# print(mi_diccionario) # print prohibido del diccionario

# Python acepta claves que no sean str, pero no es lo recomendable.
# otro_dicc = {0:"Pepe", 9:"Perez"}
# print(otro_dicc)

# fecha_nacimiento = {"dia": 28, "mes": "octubre", "anio": 2026}
# mi_diccionario.update({"fecha_nacimiento": fecha_nacimiento})
# mi_diccionario.update({"fecha_nacimiento": {"dia": 28, "mes": "octubre", "anio": 2026}})

# print(mi_diccionario)

# # mi_diccionario["fecha_nacimiento"]["anio"] = 2000
# # mi_diccionario["fecha_nacimiento"].update({"anio": 2000})
# # mi_diccionario.update({"fecha_nacimiento":{"dia": 28, "mes": "octubre", "anio": 2020}})

# print(mi_diccionario)



# 3 formas de ITERAR:

# mi_diccionario = {"nombre":"Pepe", "apellido":"Perez", "edad": 35, "dni": 20123123}

# 1) Por Valores. (SOLO LECTURA)
# for valor in mi_diccionario.values(): # ["Pepe", "Perez", 35, 20123123]
#     print(valor)


# 2) Por Claves. (LECTURA Y ESCRITURA)
# for clave in mi_diccionario.keys(): # ["nombre", "apellido", "edad", "dni"]
#     #     calve, valor
#     print(clave, mi_diccionario[clave])

# 3) Por items. 
# for item in mi_diccionario.items(): # [("nombre", "Pepe"), ("apellido", "Perez"), ("edad", 35), ("dni", 20123123)]
#     print(item) # lectura
#     print(item[0], item[1]) # lectura
#     print(mi_diccionario[item[0]]) # lectura y escritura

# Otra variante de items.
# for clave, valor in mi_diccionario.items():
#     print(clave, valor, mi_diccionario[clave]) # lectura y escritura
#     mi_diccionario[clave] = None # Pisamos todos los valores del diccionario con None



diccionario_vacio = {}
diccionario_vacio.update({"legajo": 12734})

print(diccionario_vacio)

datos_a_agregar = {"legajo": 5555, "regularidad": True}
diccionario_vacio.update(datos_a_agregar)

print(diccionario_vacio)


# tuplas -> ()
# sets   -> set(), {1, 2, 3, False}
# diccionarios -> {} se compone de items (clave:valor)

# print(diccionario_vacio["legajo"]) # 5555
# print(diccionario_vacio.get("legajo")) # 5555

# retorno_pop = diccionario_vacio.pop("regularidad")
# print("Eliminamos: ", retorno_pop)
# print(diccionario_vacio)

# matriz = [[[]]]
# matriz[0][0]["nombre"]

# print(type(matriz)) # lista
# print(type(matriz[0])) # lista
# print(type(matriz[0][0])) # diccionario
# print(type(matriz[0][0]["nombre"])) # str

# # matriz:list[list[dict]]

# matriz[0][0].update({"apellido": "Perez"})


# numero = 5
# numero_b = 3.14
# valor_aletorio = True
# print(type(numero)) # int
# print(type(numero_b)) # float
# print(type(valor_aletorio)) # bool


# lista[0] # accediendo al indice 0 de la lista.
# [0] # lista con un unico elemento -> 0
# lista = [1, 2, 3, 4]
# print(lista[:2]) # [1, 2]
# lista = [1, 2, 3, 4]
# print(lista[2:]) # [3, 4]


# saludo = "Hola mundo!"
# print(saludo[2:7])