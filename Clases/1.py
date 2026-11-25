# Tipos de Dato:

# TODOS ESTOS TIPOS DE DATOS SON INMUTABLES:
# int (numeros enteros): -5, 0, 100, 1000000
# float (numero con decimales): 3.14, -5.15, 0.0
# str (string / cadena de caracteres): "hola", 'Juan', "123 !%" 
# bool (verdadero y falso): True, False
# NoneType (Nada, vacio): None

# Caracter de escape -> \
# cadena = 'hola "PEPE", como estas?'
# cadena_dos = "PEPE'S"
# cadena_tres = "Mi restaurante se llama \"PEPE\'S\""
# cadena_multilinea = """
# qiuwheiuqidh
# qwiojheiuqhjew
# qw
# hola
# chau"""

# # \n -> Salto de linea

# print(cadena_tres)


# Funcion type() -> nos dice que tipo de dato almacena la variable
# mi_variable = input("Ingresame tu edad: ") # Por defecto input devuelve str.
# mi_variable = int(mi_variable)
# mi_variable = int(input("Ingresame tu edad: ")) # Es lo mismo que las 2 lineas anteriores

# tipo_de_dato = type(mi_variable)    # snake_case
# print(tipo_de_dato) # Ignoren el class.
# print(type(mi_variable))

# mi_variable = None
# print(mi_variable, type(mi_variable))


# CASTING: intenta transformar un TIPO de dato a otro.
# int() -> Valores numericos positivos/negativos.
# float() -> Valores numericos positivos/negativos, los decimales con punto.
# bool() -> False solamente: 0, "", otros valores vacios.
# str(5) -> "5"


# Python tipado dinamico. (No indica/restringe el tipo de dato de la variable)
# numero = 7
# numero = False
# numero = "Hola"
# numero = 3.14


# Hay lenguajes que son fuertemente tipados. (JAVA / C / C++)
# int numero = 7;
# numero = 10;
# numero = "Hola"; # NO LO PERMITE


# Funcion id()
# numero_a = 3768127368678123
# identificador = id(numero_a) # Nos devuelve el identificador UNICO del valor.
# print(identificador) # 140714494256168
# print(id(numero_a))






# ======================== MEMORIA RAM ===============================

# 127963678126783 ->>>>> "Hola"
# 127831386643434 ->>>>> 5
# 317238126367344 ->>>>> True

# saludo = "Hola"
# print(id(saludo))
# print(saludo) # Valor
# print(type(saludo)) # Tipo de dato
# print(id(saludo)) # ID

# saludo = 57
# print(saludo)
# print(id(saludo))




# INMUTABILIDAD.

# numero = 5 
# print("CON EL VALOR 5", id(numero))
# numero = numero + 1
# print("CON EL VALOR 6", id(numero))
# print(numero)

# saludo = "Hola"
# print(saludo, id(saludo))
# saludo = saludo + " Juan"
# print(saludo, id(saludo))



# OPERADORES.

# resultado = 16 / 3 # 5.33...
# print(resultado, type(resultado))

# resultado = 16 // 3 # 5
# print(resultado, type(resultado))

# resultado = 16 % 3 # 1 (16//3)-> 5 * 3 -> 15; 16-15 -> 1
# print(resultado, type(resultado))

# resultado = 2 ** 3
# print(resultado)

# resultado = 12 == "12"
# print(resultado) # False
# print(12 == "12") # False
# print(12 == 12) # True

# print("Hola" == "hola") # Python es case sensitive, importan las minus/mayus.


# Operadores Logicos:

# AND (&&)
# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False

# OR (||)
# True or True -> True
# True or False -> True
# False or True -> True
# False or False -> False

# NOT (!)
# not True -> False
# not False -> True

# not 5 -> # TODO MENOS EL 5
# not "Juan" -> # TODO LO QUE NO SEA "Juan"






# CONDICIONALES (IF-ELIF-ELSE):

# Solicitar la edad del usuario por consola/terminal y determinar e informar si es MAYOR de edad.

# 1. Le pedimos que nos ingrese la edad por consola.
# 2. Pasamos la edad a entero.
# 3. Determinar si es igual o mayor de 18 años.
# 4. Informar el resultado.

# MAYORIA_EDAD = 18
# edad = input("Ingrese su edad: ") # "33"
# edad = int(edad) # 33
# # edad = int(input("Ingrese su edad: "))

  
# # if edad >= MAYORIA_EDAD:
# # if edad > 17:
# if edad >= 18: # VERDADERO
#     # Bloque de codigo del IF (verdadero)
#     # Todo lo que este tabulado despues de los : del if, se va a ejecutar si la condicion se cumple.
#     print("Usted es mayor de edad (ADULTO).")
# elif edad > 12:  # Adolescente (13-17)
#     # Bloque de codigo del ELIF (falso-verdadero)
#     print("Usted es adolescente.")
# elif edad > -1:
#     print("Usted es un niño/a.")
# # elif edad > -1:
# #     print("Usted es un niño/a.")
# else:
#     # Bloque de codigo del ELSE (falso)
#     print("ERROR, edad invalida.")

# print("Programa terminado.")


# IF en otro lenguaje: if (condicion){print("usted es adulto");}






# ===============================  MATCH (switch) ==================================
# Las comparaciones se hacen con == igualdad pura.
# Si tiene 4 o mas casos.
# ("niño" != "Niño")
# Menu (ABM = alta, baja, modificacion) CRUD (crear, leer, actualizar y eliminar)

rango_edad = input("A que rango de edades perteneces? (Niño / Adolescente / Adulto): ")

match rango_edad:
    case "Niño" | "Niña": # | pipe, es un or logico.
        # Bloque de codigo de cada case.
        print("Toda la vida por delante!")
    case "Adolescente":
        print("Etapa complicada.")
    case "Adulto":
        print("Dolores de espalda.")
        edad = input("Ingresa la edad numerica: ")
        # if edad > 18 and edad < 35:
    case _: # Caso por defecto (default), debe ir como ultimo caso.
        print("Error, rango invalido.")


