# Matrices:

# Que son las matrices? : una lista de listas o listas anidadas.

# matriz = [[{"nombre": "Juan", "nota": 6}, {....}], [3, 4]] # Filas y columnas
#          [FILA][COLUMNA]
# print(matriz[1][0]) # 3

# Iterar la matriz:
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end=" ")
#     print()

# print(type(matriz[1])) # list
# print(type(matriz[0][1])) # int
# print(type(matriz))  # list
# print(matriz[2][2]) # ERROR, nos pasamos de rango.


# # A: 2x3
# matriz_a = [[3, 7, 5],
#             [12, 2, 11]]
# # B: 3x2
# matriz_b = [[3, 16],
#             [1, 4],
#             [4, 22]]

# A * B -> 2x2
# B * A -> 3x3

# 3 fors (i, j, k)
# acum = 0
# acum += A[0][0] * B[0][0] # 9
# acum += A[0][1] * B[1][0] # 7
# acum += A[0][2] * B[2][0] # 20
# acum = 36
# R[0][0] = acum
# acum = 0
# acum += A[0][0] * B[0][1] #  48
# acum += A[0][1] * B[1][1] #  28
# acum += A[0][2] * B[2][1] #  110
# acum = 186
# R[0][1] = acum
# acum = 0
# acum += A[1][0] * B[0][0] # 
# acum += A[1][1] * B[1][0] #  
# acum += A[1][2] * B[2][0] #  
# acum = ?
# R[0][1] = acum
# acum = 0
# acum += A[1][0] * B[0][1] #  
# acum += A[1][1] * B[1][1] # 
# acum += A[1][2] * B[2][1] #  
# acum = ?
# R[0][1] = acum
# acum = 0


# 12 iteraciones
# 3 * 2 * 2
# for i in range(len(matriz_a)):
#    for j in range(len(matriz_b[0])):
#        acum = 0
#        for k in range(len(matriz_b)):
#            acum += matriz_a[i][k] * matriz_b[k][j]
#        matriz_r[i][j] = acum




# Metodos de Listas:
# Que diferencia hay entre un metodo y una funcion? Y como reconocen uno y el otro?
# Las funciones son bloques de codigo independiente.
# Los metodos son funciones que le pertenecer a una clase (tipo de dato) especifico.
# TODOS los metodos son funciones, PERO NO todas las funciones son metodos.

# Funciones:
# import random
# random.random()
# len()
# input()
# print()
# ord()
# chr()
# def sumar(num_a:int, num_b:int)->int:
#     """Documentacion"""
#     return num_a + num_b
# resultado = sumar(1, 2)

# import funciones
# funciones.sumar()

# from funciones import *
# sumar()

# Metodos de listas:
# lista = [1, 2, 3]
# Metodos invocados desde una variable del tipo lista:
# lista.append() # agrega un nuevo elemento al final de la lista.
# lista.extend() # union de listas. (une dos listas).
# lista.index() # busca el indice de un valor. *  Arroja un error / excepcion.
# lista.sort() # ordena, por defecto ASC, reverse=True -> DESC.
# lista.clear() # limpia la lista (dejandola vacia).
# lista.count() # cuenta las veces que aparezca un elemento.
# lista.copy() # copia una lista Superficial / Shallow.
# Metodos invocados desde una lista literal.
# [1, 2].pop() # elimina un valor, retornando el valor. Recibe un indice. *  Arroja un error / excepcion.
# [1, 2].remove() # elimina un valor. Recibe el valor. * Arroja un error / excepcion.
# [1, 2].insert() # inserta un elemento en el indice especifico.
# [1, 2].reverse() # invierte el orden de la lista.

# lista.upper() # No existe.
# "hola".upper() # Funcion / existe

# Metodos constructors:
# int()
# float()
# bool()
# list()

# Control de errores / excepciones:
# try - except:
# - Si se produce un error en el bloque try: corta en la linea del error y nos manda al bloque except.
# - Si NO se produce ningun error, termina el bloque y ignora/evita el except.
# try:
#     print("Bloque Try.")
#     print("if, else, bucles, etc")
# except:
#     print("Bloque Except.")

# NO ES LO MISMO QUE UN CONDICIONAL!
# if 1 == 1:
#     print("Bloque IF")
# else:
#     print("Bloque Else")


# Copia Superficial: itera superficialmente y va copiando elemento por elemento, sin revisar y son o no mutables.
# Copia Shallow (superficial) y Deep (profunda):
# Copia Shallow:
# lista = [1, 2]
# copia_a = lista.copy() # Metodo
# copia_b = lista[:] # Slicing
# # Funcion propia
# def copiar_lista_superficialmente(lista:list)->list:
#     """Documentacion"""
#     copia = []
#     for i in range(len(lista)):
#         copia.append(lista[i])
#     return copia
# import copy
# copy.copy() # Modulo copy

# Deep copy hace una copia REALMENTE / TOTALMENTE INDEPENDIENTE.
# Copia Profunda (Deep):
# copia_deep = copy.deepcopy(lista)



# ================== TUPLAS ====================:
# Es una COLECCION que se representa con (), parecida a una lista, con la excepcion de que la tupla 
# es inmutable y la lista es mutable, comparten el resto de las caracteristicas.
# Es indexable, heterogenea, iterable, ordenada.
# Las tuplas se pueden desempaquetar.
# def test_desempaquetar()->tuple:
#     num_a = 5
#     num_b = 7
#     return num_a, num_b

# mi_tupla = test_desempaquetar()
# print(mi_tupla, type(mi_tupla))
# num_x, num_z = test_desempaquetar() # Desempaquetado de tuplas.
# print(num_x, type(num_x))
# print(num_z, type(num_z))


# ================== SETS ======================:
# Es una coleccion, que guarda elementos separados con comas (lo mismo que tuplas  y listas), se representa
# con llaves {}, no almacena valores repetidos (son unicos), solo almacena valores inmutables (Heterogenea).
# Es una coleccion DESORDENADA, no mantiene el mismo orden de elementos. No tiene indices. Es mutable.
# Es iterable con un for-each. Un set vacio se ve asi: set().


# ================= Diccionarios ===============:
# Es una coleccion que se compone de items, y cada item a su vez se compone en pares -> clave:valor.
# Se representa con llaves {}. Diccionario vacio -> {}. 
# Mutable. (con metodo update y asignacion directa) 
# Indexable: por su clave.
# Es heterogeneo en sus valores.
# Ordenados: mantiene el orden de ingreso.
# Iterable: 3 maneras diferentes.
# Las claves: deben ser str, no se deben repetir en un mismo diccionario.
# Metodo update(): actualiza el diccionario:
# - Si la clave que le pasamos NO existe agrega un nuevo item con esa clave y valor.
# - Si la clave ya existe, modifica el valor en esa clave.

# alumno = {"nombre": "Juan", "edad": 30, "nota_pp": 6}
# alumno_dos = {"nombre": "Pepe", "edad": 25, "nota_pp": 7}
# alumno.update({"nota_sp": 8})
# print(alumno)
# alumno.update({"edad": 31})
# print(alumno)

# alumno["nota_pp"] = 10 # Soporta asignacion directa.
# print(alumno)

# NO ES LA FORMA CORRECTA DE ITERAR:
# for algo in alumno:
#     print(algo)

# Las 3 correctas son:
# alumno = {"nombre": "Juan", "edad": 30, "nota_pp": 6}

# Solo lectura
# for valor in alumno.values():
#     print(valor) # Valor

# Lectura y escritura
# for clave in alumno.keys():
#     print(clave, alumno[clave]) # Clave y Valor

# Lectura y escritura
# for item in alumno.items():
#     print(item)

# Version de items con desempaquetado de tuplas.
# for clave, valor in alumno.items():
#     print(clave, valor, alumno[clave])


# alumnos = [{"nombre": "Juan", "edad": 30, "nota_pp": 6}, {"nombre": "pepe", "edad": 25, "nota_pp": 7}]

# print(type(alumnos)) # list
# print(type(alumnos[1])) # dict
# print(type(alumnos[1]["edad"])) # int



# =============================== ARCHIVOS ===============================:

# 2 tipos de archivos:
# - Texto (txt, py, csv, json, etc) -> Esta categoria, trabajamos este cuatrimestre.
# - Binarios (mp3, wave, mp4, pdf, docx, jpg, exe, dll, etc)

# Abrimos archivos con:
# funcion open() que recibe 2 parametros:
# - ruta (absolutas y relativas) # * OJO NO ES EL NOMBRE SOLAMENTE SINO QUE ES LA RUTA!!!!
# Absoluta: C:\Users\valer\OneDrive\Escritorio\Curso de Ingreso\Programacion_I_2C_2026\212\repaso.py
# Relativa (Recomendada): 212\repaso.py 
# - MODO de apertura (r, w, a) # * OJO NO ES EL METODO DE APERTURA sino el MODO!!!!!!

# 1) Clasico
# ruta = "212/clase_12.py"
# archivo = open(ruta, "r") # 1) Apertura
# datos = archivo.read() # 2) Manipulacion
# archivo.close() # 3) Cierre


# 2) con with (cierre automatico)
# with open(ruta, "r") as archivo: # 1) Apertura
#     datos = archivo.read() # 2) Manipulacion
#     print(datos) # Achivo sigue abierto
#     # 3) Cierre automatico.
# print(datos) # El archivo ya esta cerrado


# MODOS de Apertura:
# r -> lectura 
# w -> escritura
# a -> anexado

# 5 situaciones de apertura:
# - MODO r, el archivo existe: lo abre y lo prepara para ser leido.
# - MODO r, el archivo NO existe: ERROR! * Lo pueden manejar con try-except.
# - MODO w/a, el archivo NO existe: crear el archivo.
# - MODO w, el archivo existe: lo abre, y lo vacia preparandolo para su escritura.
# - MODO a, el archivo existe: lo abre, no lo vacia, al final del archivo, donde esta parado el cursor.

# Metodos de archivos:
# - close(): cerrar el archivo.
# - read(): extrae los datos del archivo, retornando UN string.
# - write(): escribe datos al archivo, recibe por parametro UN string.
# - readlines(): lee lineas del archivo y retorna esa informacion en formato: list[str]
# - writelines(): escribe lo que recibe por parametro: list[str]


# NO SE PUEDE UTILIZAR EL MODULO CSV!
# Metodos de STRINGS utiles para manejar archivos CSV (Comma separated values):

# - strip(): limpiaba cadena en el inicio y el final. Por defecto limpia caracteres en blanco (espacio, tabulacion, salto de linea, etc)
#            Recibe por parametro el caracter a limpiar.
#            print("....ho.la.....".strip("."))
# - join(): Recibe un iterable y concatena los elementos entre si utilizando un separador. Retorna la cadena resultante.
#           lista = ["A", "B", "C"]
#           resultado = "_".join(lista)
#           print(resultado)
# - split(): Recibe un separador por parametro y separa una cadena usando ese separador. Retorna una list[str]
#           print("hola mundo".split(" "))
#           cadena = "chau mundo"
#           print(cadena.split(" "))

# Normalizacion de cadenas: minusculas y mayusculas
# - upper()
# - lower()
# - capitalize()
# - title()


# PUEDE UTILIZAR EL MODULO JSON
# import json

# Escritura JSON
# alumnos = [{"nombre": "Juan", "edad": 30, "nota_pp": 6}, {"nombre": "pepe", "edad": 25, "nota_pp": 7}]
# archivo = open("212/test.json", "w")
# json.dump(alumnos, archivo, indent=4)
# archivo.close()

# Lectura JSON
# archivo = open("212/test.json", "r")
# datos = json.load(archivo)
# archivo.close()
# print(datos)