#MODULOS

# import funciones
# import random

# resultado = funciones.sumar(3, 5)
# aleatorio = random.randint(1,2)



# print(resultado)

##################

#from funciones import saludar, sumar, generar_aleatorio
# from funciones import *
# #import funciones
# #saludar()

# #resultado = sumar(7,10)

# #print(resultado)
# #print(edad)
# #print(generar_aleatorio())
# edad = 23

# print(edad)

###############

# import funciones as f
# import random as aleatorio

# resultado = f.sumar(3, 5)
# respuesta = aleatorio.randint(1,2)


# print(resultado)
# print(respuesta)



# def incrementar_numero(num:int)->int:
#     """DOCUMENTACION"""
#     num += 1 # num = num + 1
#     print("DENTRO DE LA FUNCION ", num)
#     return num


# numero = 3
#             # 4
# numero = incrementar_numero(numero)
# print("FUERA DE LA FUNCION ", numero) 




# def agregar_elemento(lista:list, cadena:str):
#     """DOCUMENTACION"""
#     lista += [cadena]
#     # return lista

### lista = lista_nombres # Indirectamente, estamos asignando la lista de nombres al parametro lista.

# id(lista_nombres) -> 53
# lista_nombres = ["Juan", "Maria", "Rodrigo"]
# agregar_elemento(lista_nombres, "Pepe")

# print(lista_nombres) # | [Juan Maria Rodrigo Pepe] 

# agregar_elemento(lista_nombres, "Sofia")
# print(lista_nombres) #  [Juan Maria Rodrigo Pepe Sofia] 






# #        0  1
# lista = [1, 2]  # ID DE LISTA = 79
# lista_b = lista # ID DE LISTA_B = 79
# lista[1] = 7
# lista_b[0] = 3

# print(lista, id(lista)) # [3, 7]
# print(lista_b, id(lista_b)) # [3, 7]