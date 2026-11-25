# BUCLE FOR
# El bucle FOR se utiliza cuando se conoce/se puede determinar la cantidad de iteraciones.

# contador = 0
# edad_ingresada = input()

# while contador < 10:
#     contador += 1
#     print(contador)



# FOR CLASICO (NO EXISTE EN PYTHON)
# for (contador = 0; contador < 10; contador += 1):


# FOR - EACH (Recorre objetos iterables)
# saludo = "hola mundo"

# for elem in saludo: # el for itera 10 veces
#     print(elem)


# for numero in "12345":
#     print(numero, type(numero))


# =====================================================
# RANGE: es una funcion que genera una secuencia de valores enteros.

# Range con UN solo parametro.
# mi_rango = range(4) # UN SOLO PARAMETRO -> es el HASTA (EXCLUYENTE)
# 0, 1, 2, 3
#print(mi_rango, type(mi_rango))
#print(list(mi_rango)) # [0, 1, 2, 3]

# for num in mi_rango:
#     print(num, type(num))


# for num in range(5): # [0, 1, 2, 3, 4]
#     # print(num)
#     nota = int(input(f"Ingrese su {num + 1}° nota: "))


# for elemento in range(100):
#     print(elemento)


# RANGE con DOS parametros: el primero es el DESDE (INCLUIDO), el segundo es el HASTA (EXCLUIDO).
# for num in range(3, 9): # [3, 4, 5, 6, 7, 8]
#     print(num)

# print(range(5)) # range(0, 5)
# print(list(range(5))) # [0, 1, 2, 3, 4]
# print("======================")

# for num in range(5):
#     print(num)

# for char in "hola":
#     print(char)


# RANGE con TRES parametros:
# El primero es el DESDE (INCLUIDO),
# El segundo es el HASTA (EXCLUIDO),
# El tercero es el SALTO/PASO: de cuanto en cuanto avanza.

# for num in range(4, 15, 3): # [4, 7, 10, 13]
#     print(num)




# ===========================================================
# for num in range(1, 1, 1): # [] # NO SE CREA LA SECUENCIA, EL FOR NO ITERA.
#     print(num)

# print("FUERA")

# for num in range(10, -5, -2): # [10, 8, 6, 4, 2, 0, -2, -4]
#     print(num)


# desde = int(input("DESDE que valor queres iterar: ")) # 10
# hasta = int(input("HASTA: ")) * 5 # 5

# for num in range(desde, hasta, 2):
#     print(num)

# for i in range(5):
#     print()

# for i in range(10, 0, -1):
#     dato = input(f"Ingresame {i}°: ")




# =====================================================================

# SENTENCIAS BREAK y CONTINUE: aplican a ambos bucles.



# BREAK: ROMPE/INTERRUMPE/TERMINA el bucle MAS CERCANO/PROXIMO.
# for num in range(5):
#     print(num)
#     if num == 3:
#         break


# while True:
#     nombre = input("Ingrese su nombre (para salir aprete ENTER): ")
#     if nombre == "":
#         break


# for i in range(3): # [0, 1, 2]
#     for j in range(4): # [0, 1, 2, 3]
#         print(i, j) #  0, 0 | 0, 1 | 0, 2 | 0, 3
#                     #  1, 0 | 1, 1 | 1, 2 | 1, 3
#                     #  2, 0 | 2, 1 | 2, 2 | 2, 3


# CUANTAS ITERACIONES EN TOTAL HAY?
# 3
# 4
# 7
# 12 (3*4)

# QUE SE IMPRIME POR CONSOLA?
# 0, 0
# 1, 1
# 2, 2
# 3, 3

# 0, 0
# 0, 1
# 0, 2
# 0, 3
# 1, 0
# 1, 1
# 1, 2
# 1, 3
# 2, 0
# 2, 1
# 2, 2
# 2, 3


# for char in "hola mundo":
#     if char == " ":
#         break
#     print(char)


# CONTINUE: termina la iteracion y va a la proxima. Salta a la proxima iteracion/vuelta. 


# for i in range(10): # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     if i % 2 == 0: # i es par?
#         continue
#     print(i)


# for i in range(5): # [0, 1, 2, 3, 4]
#     if i == 2:
#         continue
#     print(i)



# for i in range(5): # [0, 1, 2, 3, 4]
#     # ESTO NO SE DEBE HACER!
#     if i == 2:
#         pass # pass no hace nada
#     else:
#         print(i)

#     # CORREGIDO:
#     if i != 2:
#         print(i)



# =================================================================================

# Valores al azar (valores aleatorios)
# import random # Los imports se hacen arriba de todo, en las primeras lineas.
# # Incluye ambos extremos (DESDE y HASTA)
# valor_aleatorio = random.randint(1, 10) # Funcion que genera un valor entero aleatorio (al azar)
# print(valor_aleatorio)




# MINIMOS Y MAXIMOS.

# Bandera / Flag: es una variable que maneja un estado y nos indica si algo ya sucedio o no.
# minimo = 0 # Es mala practica inicializar minimos/maximos.
# bandera_primer_valor = True

# # Buscar el producto mas barato (precio mas bajo). (500, 100, 400, 700)
# while True:
#     precio = int(input("Ingrese el precio del producto (0 para salir): ")) # 0->inf+
#     while precio < 0: # Validamos que los precios no sean negativos.
#         precio = int(input("ERROR, reingrese el precio del producto (0 para salir): ")) 

#     if precio == 0:
#         break

#     if bandera_primer_valor == True:
#         minimo = precio
#         bandera_primer_valor = False
#     elif precio < minimo:
#         minimo = precio

# print("El producto mas barato tiene un precio de: $", minimo)
    




# 5 precios de productos, quiero encontrar el mas barato.

# bandera_primero = True

# for i in range(5):
#     precio = int(input("Ingrese el precio del producto: "))

#     if bandera_primero == True:
#         minimo = precio
#         bandera_primero = False
#     elif precio < minimo:
#         minimo = precio


# print("El menor precio es: ", minimo)





for i in range(5):
    precio = int(input("Ingrese el precio del producto: "))

    if i == 0:
        minimo = precio
    elif precio < minimo:
        minimo = precio


print("El menor precio es: ", minimo)
