#Funciones

# print("Hola mundo")
# input("Ingrese el nombre: ")
# len("Hola")

# edad = input("Ingrese su edad: ")
# largo_saludo = len("Hola")

#Reglas para nombrar funciones
# nombre descriptivo
# nomenclatura snake_case
# deben llevar un verbo en infinitivo, representan acciones.

#def a():


# def sumar_enteros(): #la firma de la funcion
#     # cuerpo de la funcion
#     suma = 10 + 5 
#     print(suma)

# sumar_enteros() #llamada/invocacion de la funcion
# sumar_enteros()
# sumar_enteros()
# #saludar() no nos deja invocar una funcion antes si no esta definida
# def saludar():
#     print("Hola mundo")
#     print("chau")

# saludar()
# saludar()

#Parametros
#punto de entrada de datos que recibe la funcion
#Primera clasificacion
#Parametros formales: estan en la firma de la funcion

# def restar(num_a, num_b):
#     resta = num_a - num_b
#     print(resta) #resta es un parametro actual de la funcion print

# numero = int(input("Ingrese un numero: "))
# restar(int("10"), numero) #parametros actuales: estan en la llamada de la funcion
# restar(10,20) #-10
# restar(5,2) #3

#Segunda clasificacion
#Parametros obligatorios por ejemplo num_a necesita un valor en la llamada de la funcion
#Parametro opcional: tiene un valor asignado por defecto
# def dividir(num_a, num_b=8):
#     resultado = num_a / num_b
#     print(resultado)

# dividir(16) #2   si no se le asigna divide 16 por 8 (valor por defecto)
# dividir(16,2) #8
# dividir(32)

# def calcular_iva(precio: int | float, porcentaje_iva:int | float = 21)-> None:
#     """
#     Aplica el impuesto iva sobre un precio base.\n
#     Parametros:\n
#         - precio (int | float): el precio base.\n
#         - porcentaje_iva (int | float): el porcentaje del impuesto a aplicar. 21% por defecto.\n
#     Return:\n
#         None
#     """
#     resultado = precio * ((100 + porcentaje_iva)/100)
#     print(f"El precio con iva es {resultado}")

# calcular_iva(1000)

# calcular_iva(1000, 10.5)
# calcular_iva(10.5, 1000) #Parametros por posicion
# calcular_iva(precio=2000, porcentaje_iva=11.5) #Parametros por nombre
# calcular_iva(porcentaje_iva=5, precio=2000)

#Regla: primero los parametros obligatorios, luego los opcionales

#Una funcion podria tener o no un retorno
#Retorno/ return: 
# indica que termina la funcion
# devuelve un valor

# Buenas practicas 
# un unico return por funcion al final de la misma
# funciones ideales con parametros y con retorno

# def calcular_promedio(num_a: int | float, num_b: int | float)-> float:
#     """
#     Calcula el promedio de dos números.\n
#     Parametros:\n
#         - num_a (int o float): es uno de los valores para calcular el promedio\n
#         - num_b (int o float): es uno de los valores para calcular el promedio\n
#     Return:\n
#         - float: el resultado del promedio
#     """
#     resultado = (num_a + num_b)/ 2 #resultado es una variable local
#     #print(resultado)
#     return resultado

# resultado = calcular_promedio(100, 200)
# print(resultado)


# print("Juan", "Pepe", "Maria", sep="_")

#input()                    
#len("")

#DOCUMENTACION
#TODAS LAS FUNCIONES deben tener documentacion
"""
1. ¿Que hace la funcion? - descripcion breve / objetivo
2. ¿Que parametros acepta? - nombrar los parametros..
3. ¿Que devuelve? - return ....
"""

#Tipos de datos en parametros y retorno
#sirve como documentacion/indicacion del tipo, no es una restriccion

#Variables locales: Nacen, cumplen su proposito y mueren dentro de la funcion. 
#Pertenencen al SCOPE (ambito) de la funcion

#Variables globales: CUIDADO NO USAR, mala practica !!
# saludo = "Hola mundo"

# def probar_codigo():
#     global saludo
#     print(saludo)

# probar_codigo()

def extraer_datos(mensaje_uno: str, mensaje_dos: str)-> list:
    nombre = input(mensaje_uno)
    edad = int(input(mensaje_dos))
    datos = [nombre, edad] # metemos los datos a una lista
    return datos # retornamos en una lista
    #print()
    # return nombre , edad -> NO HACER


resultado = extraer_datos("Ingrese nombre: ", "Ingrese edad: ")

print(f"Nombre: {resultado[0]}, Edad: {resultado[1]}")

#el break(afecta solo los bucles) y el return(afecta solo funciones y 
# devuelve resultado) no son lo mismo