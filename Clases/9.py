# CADENAS DE CARACTERES:
# ' '   o    " "     o     """  """

# \ -> es un caracter de escape (sirve para deshabilitar la funcionalidad especial de un caracter del string)
# print('Su descripcion es "COMERCIAL", y por ejemplo: \'NO\'')
# print("Su descripcion es \"COMERCIAL\", y por ejemplo: 'NO'")


# Modificamos el parametro opcional "sep" del print
# otro_nombre = "Rodrigo"
# print("Juan", "Pepe", otro_nombre, "Sofia", sep="=|=")


# ===================  Las cadenas son INDEXABLES. =================== 

#         012345678910
# saludo = "Hola mundo!"

# print(saludo[5]) # m
## saludo[0] = "h" # ERROR, Los strings no se pueden modificar una vez creados.

# cant_elementos = len(saludo) # len() -> mide la cantidad de elementos de un objeto iterable.

# print(f"La variable saludo tiene {cant_elementos} caracteres") # 11

#  =================== Son ITERABLES. =================== 

# For-each (solo lectura)
# for caracter in saludo:
#     print(caracter, end=" ")
# print()

# For-each (lectura y escritura) *!!! Los strings NO se puede modificar, son INMUTABLES.
# for i in range(len(saludo)): # [0,1,2,3,4,5,6,7,8,9,10]
#     print(saludo[i], end=" ")

#         0123456789
# saludo = "Hola mundo!"

# Busqueda de UN caracter (el primero):
# for indice in range(len(saludo)):
#     if saludo[indice] == "o":
#         print("Encontramos el espacio en el indice:", indice)
#         break



# ===================== CONCATENACION (+) =====================
# sal = "Hola "
# udo = "mundo!"
# saludo = sal + udo + " JUAN "
# print(saludo)


# str + str -> Concatenacion        |    "Hola " + "mundo" -> "Hola mundo"
# int + int -> Suma                 |     2 + 3 -> 5
# float + float -> Suma             |     3.13 + 0.01 -> 3.14
# list + list -> Union / Extension  |     [1.3, 5] + [True, "Juan"] -> [1.3, 5, True, "Juan"]
# str + int -> ERROR!!!!!!!!!!!




# ======================= REPETICION DE CADENAS (*) (Usando en python y no tanto en otros lenguajes )=======================

# print("Hola" * 5)

# saludo_repetido = "Hola" * 5 # "HolaHolaHolaHolaHola"
# print(saludo_repetido)


# sep_inicial = "===================== MENU ======================"
# cadena_uno =  "| 1) Ingrese numeros."
# cadena_dos =  "| 2) Muestre resultados."
# cadena_tres = "| 3) CADENA SUPER DUPER LARGAAAAAAAA"
# sep_final =   "====================================================" # Largo fijo, no esta bueno.

# largo_cadena_larga = len(cadena_tres)
# largo_inicial_mitad = int((largo_cadena_larga - 6) / 2)
# sep_inicial = ("=" * largo_inicial_mitad) + " MENU " + ("=" * largo_inicial_mitad)
# sep_final = "=" * largo_cadena_larga 


# print(sep_inicial, cadena_uno, cadena_dos, cadena_tres, sep_final, sep="\n")



# ========================== SLICING (REBANADO) ===============================
# [::]
# Si alguno de los valores se deja vacio, se toman los valores por defecto [0:len(saludo):1]
# Tiene parametros parecidos al range() --> (DESDE (incluidi) , HASTA (excluido), SALTO)

#         012345...
# saludo = "Hola mundo!"
# extracto = saludo[0:4] # Imprime "Hola"
# print(extracto, end=".")

# extracto = saludo[5:]  # Imprime "mundo!"
# print(extracto, end=".")

# extracto = saludo[:] # Imprime "Hola mundo!"
# print(extracto)

# extracto = saludo[::2] # Imprime "Hl ud!"
# print(extracto)

# extracto = saludo[::-1] # Imprime "!odnum aloH"
# print(extracto)




# ========================= SLICING CASERO ===========================

# def rebanar_cadena_casero(cadena:str, desde:int, hasta:int, salto:int=1)->str:
#     """Documentacion"""
#     extracto = ""
#     # for i in range(desde, len(cadena)):
#     #     if i != hasta:
#     #         extracto += cadena[i]
#     #     else:
#     #         break

#     # for i in range(desde, len(cadena)):
#     #     if i == hasta:
#     #         break
#     #     extracto += cadena[i]

#     for i in range(desde, hasta, salto):
#         extracto += cadena[i]
#     return extracto



# saludo = "Hola mundo!"
# extracto = rebanar_cadena_casero(saludo, 5, 11)
# print(extracto) # "Hola"




#  ========================= COMPARACION DE CADENAS =====================================
#  Python soporta comparacion de cadenas.
#  Lexicograficamente: el mismo orden que los diccionarios fisicos.

# if "A" > "a":
#     print("Mayuscula es mayor")
# else:
#     print("Minuscula es mayor")

# if "Lunes" > "Martes":
#     print("Lunes es mayor")
# else:
#     print("Martes es mayor")

# "Algo"
# "Puerco"
# "Puerta"
# "Puerto"


# if "-" > "a":
#     print("Es mayor el guion")
# else:
#     print("Es mayor la letra 'a' minuscula")



# ============== CODIGO ASCII ALGORITMICAMENTE =================

# ord() y chr()

# caracter = chr(75)
# print(caracter) # "K"

# ordinal = ord("s")
# print(ordinal) # 115



# NO PUEDE UTILIZAR METODOS ANTES DEL PRIMER EXAMEN PARCIAL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# UPPER() es un metodo de strings

# saludo = "hOLa muNdo!1"
# print(saludo.upper()) # NO MODIFICA EL STRING ORIGINAL. Sino que crea un nuevo string y lo devuelve.
# print(saludo)



# =================== FUNCION UPPER PROPIA ==============================
#                          "hOLa muNdo!1"
# def transformar_a_mayusculas(cadena:str)->str:
#     """Documentacion"""
#     resultado = ""
#     for i in range(len(cadena)):
#         #    "h"                   "h"
#         if cadena[i] >= "a" and cadena[i] <= "z":
#             codigo_ascii = ord(cadena[i]) # 104
#             nuevo_codigo_ascii = codigo_ascii - 32 # 72
#             nuevo_caracter = chr(nuevo_codigo_ascii) # "H"
#             resultado += nuevo_caracter # "H"
#         else:
#             resultado += cadena[i]
#         # si el caracter es minuscula: 
#         #   lo convierto a mayus.
#         # sino:
#         #   lo dejo asi como esta.
#     return resultado


def transformar_a_mayusculas(cadena:str)->str:
    """Documentacion"""
    resultado = ""
    for i in range(len(cadena)):
        if cadena[i] >= "a" and cadena[i] <= "z":
            resultado += chr(ord(cadena[i]) - 32) 
        else:
            resultado += cadena[i]
    return resultado


# saludo = "hOLa muNdo!1" # -> "HOLA MUNDO!1"
saludo = "níño, NIÑO"

resultado = transformar_a_mayusculas(saludo)
print(resultado)
