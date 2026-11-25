# METODOS DE LISTAS:


# ==================================================
# APPEND: agrega un nuevo elemento (recibido por parametro) al FINAL de la lista.
# lista = [5, 3, 2]
# lista.append(4) # Reemplaza: lista += [4]
# print(lista) # PRINT PROHIBIDO [5, 3, 2, 4]

# for i in range(3): # [0, 1, 2]
#     lista.append(i)

# print(lista) # PRINT PROHIBIDO [5, 3, 2, 4, 0, 1, 2]


# lista = ["a", "b", "c"]
# lista.append(True)
# print(lista)



# ==================================================
# COUNT: Cuenta la cantidad de veces que aparezca el valor que recibe por parametro.
# lista = [5, 3, 2, 5]
# cantidad_repetida = lista.count(5) # 0 si no encontro el valor
# print(cantidad_repetida)


# ==================================================
# EXTEND: une una lista con otra (funciona con cualquier iterable).
# lista = [5, 3, 2, 5]
# lista.extend([1, 3, 5])
# print(lista) # [5, 3, 2, 5, 1, 3, 5]

# lista.extend(True)
# print(lista)

# def extender_propio(lista:list, iterable:str|list)->None:
#     """Documentacion"""
#     for i in range(len(iterable)):
#         lista.append(iterable[i])



# ==================================================
# INSERT: inserta el valor recibido por parametro, en un indice especifico (tambien lo recibe por parametro)
#        0  1  2  3
# lista = [5, 3, 2, 5]
# lista.insert(1, "R")

# #               0   1   2  3  4
# print(lista) # [5, "R", 3, 2, 5]

# lista.insert(0, "A")

# print(lista) # ["A", 5, "R", 3, 2, 5]

# # lista.insert(len(lista), "Z")
# lista.insert(100, "Z") # Funciona aun con indices MUY fuera de rango.

# print(lista) # ["A", 5, "R", 3, 2, 5, "Z"]   



# ==================================================
# CLEAR: Limpia la lista (dejandola vacia)
# lista = [5, 3, 2, 5]
# print(lista, id(lista))
# lista.clear()
# print(lista, id(lista)) # Mantiene el ID.




# ==================================================
# SORT: ordena la lista.
# lista = [5, 3, 2, 5]
# lista = ["Rodrigo", "Juan", "Pepe"]
# lista = [1, 8, 5, True, False, 3.14, 0.5, 5] # False lo toma como 0 y True como 1.
# lista.sort() # Si no recibe parametros, ordena ASC.
# lista.sort(reverse=True) # Con reverse en True, ordena DESC.
# print(lista)




# ==================================================
# REVERSE: Invierte el orden de los elementos en la lista.
# lista = [7, 3, 2, 5]
# lista.reverse() # NO ORDENA, SOLO INVIERTE!
# print(lista) # [5, 2, 3, 7]




# ========================== LOS PROXIMOS 3 PUEDEN ROMPER EL PROGRAMA! ========================
# INDEX: Busca y Devuelve el PRIMER INDICE del valor que le pasemos por parametro.
# SI el valor buscado NO EXISTE, arroja ERROR!
# lista = [7, 5, 3, 2, 5]
# resultado = lista.index(3)

# Estructura de control de exepciones: try-except (try-catch)
# lista = ["B", "C", "Z", "H", "C"]
# try: # La estructura try INTENTA ejecutar su bloque de codigo: 
#     # - Si NO se produce un error, sale del bloque sin ejecutar el except.
#     # - Si se produce un EXCEPCION, deja de ejecutar el bloque try EN ESA LINEA, y VA a ejecutar el bloque except.
#     resultado = lista.index("C", 0, 2) # tiene DESDE y HASTA Opcionales
#     print("Lo encontramos en el indice:", resultado)
#     # edad = int(input("Ingresa tu edad: "))
#     #print(5 / 0)
# except:
#     print("ERROR, el valor NO existe.")
# # except ZeroDivisionError:
# #     print("ERROR, NO se puede dividir por cero.")



# NO LO COMPAREN CON IF - ELSE (Ya que son mutuamente excluyentes, NO ASI el try-except).
# NO LO ABUSEN, LO RESERVAMOS SOLO PARA ESTOS 3 METODOS y ARCHIVOS.




# =================================================
# REMOVE: Elimina la primera ocurrencia del valor recibido por parametro de la lista.
# En caso de NO encontrar el valor, arroja una excepcion.
# lista = [7, 5, 3, 2, 5]
# lista.remove(5)
# print(lista) # [7, 3, 2, 5]
# print(len(lista)) # 4

# lista = ["Juan", "Pepe", "Sofia"]
# # lista.remove("Pepe")
# try:
#     lista.remove("Rodrigo")
# except:
#     print("Error, valor a eliminar no encontrado")

# print(lista)


# =================================================
# POP: Elimina el valor del indice que recibe por parametro, devolviendo el valor del mismo.
# En caso de NO existir el indice, arroja una excepcion.

# lista = ["Juan", "Pepe", "Sofia"]
# try:
#     # valor_eliminado = lista.pop(1)
#     valor_eliminado = lista.pop(5)
#     print("Se elimino de la lista a: ", valor_eliminado)
# except:
#     print("Error, indice a eliminar fuera de rango.")
    
# print(lista)




# =================================================
# COPY: copia todos los elementos de la lista. Es una copia SUPERFICIAL / Shallow.
# La copia superficial funciona SIEMPRE y CUANDO los elementos a copiar sean INMUTABLES.
# lista = ["Juan", "Pepe", "Sofia"]
# copia = lista.copy() # Metodo copy de listas
# copia = lista[:] # Slicing
# Tambien se puede copiar con funcion propia.
# print(lista, id(lista))
# print(copia, id(copia))


matriz = [[3, 5], 
          [1, 2]]

# SI intentamos copiar SUPERFICIALMENTE UNA MATRIZ.
# Para copiar una matriz o estructuras mas avanzadas:
# - Podemos hacer una funcion RECURSIVA.
# - Usamos el modulo COPY con su funcion deepcopy.
import copy # Arriba de todo.
copia = copy.deepcopy(matriz)

copia[0][0] = 0
print(matriz, id(matriz))
print(copia, id(copia))