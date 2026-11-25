# 1) Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

lista_enteros = [4, 8, 15, 16, 23]

suma = 0
for i in range(len(lista_enteros)): #range:trabaja con enteros
    suma += lista_enteros[i]

print("La suma de los elementos es:", suma)

# 2) Definir una lista que almacene los nombres de los primeros seis meses del año. Mostrar el primer y último
# elemento de la lista solamente.
#              0        1          2        3         4       5
lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]

print("Primer mes:", lista_meses[0])
# print("Ultimo mes:", lista_meses[5]) #esta mal harcodeado
# print("Ultimo mes:", lista_meses[-1])
print("Último mes:", lista_meses[len(lista_meses) - 1])

# 3) Definir una lista que almacene como primer elemento el nombre de un alumno y en las dos siguientes sus
# notas. Imprimir luego el nombre y el promedio de las dos notas.
#nosotros queremos que lo ingrese devuelta hasta que ingrese una nota valida por eso usamos while
nombre = input("Ingrese su nombre: ")

nota1 = int(input("Ingrese la primer nota: "))
while nota1 < 1 or nota1 > 10:
    nota1 = int(input("Error, ingrese la primer nota (del 1 al 10): "))

nota2 = int(input("Ingrese la sugunda nota: "))
while nota2 < 1 or nota2 > 10:
    nota2 = int(input("Error, ingrese la segunda nota (del 1 al 10): "))

#                0        1      2
lista_alumno = [nombre, nota1, nota2, 7, 6]

# promedio = (lista_alumno[1] + lista_alumno[2]) / 2

acumulador = 0
contador = 0

# for i in range(1, len(lista_alumno)): #Arranca 1, va hasta el ultimo elemento, inclusive.
  
for i in range(len(lista_alumno)):
    if i == 0:
        continue
acumulador += lista_alumno[i]
contador += 1

    # if i != 0:
    #     acumulador += lista_alumno[i]
    #     contador += 1

if contador != 0:
    promedio = acumulador / contador 
    print(f"El alumno {lista_alumno[0]} tiene {promedio} de promedio.")
else:
    print(f"El alumno {lista_alumno[0]} toavia no tiene notas.")


# 4) Definir una lista con 7 elementos enteros. Contar cuántos de dichos valores almacenan un valor superior a 33.
lista_numeros = [12, 45, 33, 80, 5, 60, 34]

contador = 0
for i in range(len(lista_numeros)):
    if lista_numeros[i] > 33:
        contador += 1

print("Cantidad de valores superiores a 33:", contador)

# 5) Definir una lista con 7 elementos enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores
# a 5.
lista_numeros = [3, 5, 8, 1, 6, 4, 9]

for i in range(len(lista_numeros)):
    if lista_numeros[i] >= 5:
        print(lista_numeros[i])

# 6) Definir y cargar una lista con 10 números enteros aleatorios (utilizar random), entre 1 y 10. Contar y mostrar por
# pantalla la cantidad de números pares
import random

lista_random = []
for i in range(10):
    lista_random += [random.randint(1, 10)]

contador_pares = 0
for i in range(len(lista_random)):
    if lista_random[i] % 2 == 0:
        contador_pares += 1

for i in range(len(lista_random)):
    print(lista_random[i], end=" ")
print()
print("Cantidad de numeros pares:", contador_pares)

# 7) Definir una lista que almacene los nombres de 4 personas. Contar cuántos de esos nombres tienen 5 o más
# caracteres.
lista_nombres = ["Juan", "Alejandro", "Ana", "Rodrigo"]

contador = 0
for i in range(len(lista_nombres)):
    if len(lista_nombres[i]) >= 5:
        contador += 1

print("Cantidad de nombres con 5 o mas caracteres:", contador)

# 8) Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista
# generada.
lista = []
for i in range(5):
    valor = int(input(f"Ingrese el {i + 1}° numero entero: "))
    lista += [valor]

for i in range(len(lista)):
    print(lista[i], end=" ")
print()

# 9) Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al
# ingresar el cero. Mostrar finalmente todos los elementos cargados y el tamaño de la lista.
lista = []
numero = int(input("Ingrese un numero entero (0 para terminar): "))
while numero != 0:
    lista += [numero]
    numero = int(input("Ingrese un numero entero (0 para terminar): "))

for i in range(len(lista)):
    print(lista[i], end=" ")
print()
print("Cantidad de elementos:", len(lista))


# 10) Almacenar en una lista los sueldos (valores float) de 7 operarios. Imprimir la lista y el promedio de sueldos.
lista_sueldos = [1500.0, 2200.5, 1800.0, 2500.75, 1950.25, 2100.0, 1750.5]

suma = 0
for i in range(len(lista_sueldos)):
    print(lista_sueldos[i], end=" ")
    suma += lista_sueldos[i]
print()

promedio = suma / len(lista_sueldos)
print(f"El promedio de sueldos es: {promedio:.2f}")

# 11) Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float). Obtener el promedio de las
# mismas. Contar cuántas personas son más altas que el promedio.
lista_alturas = []
for i in range(5):
    altura = float(input(f"Ingrese la altura de la persona {i + 1}: "))
    lista_alturas += [altura]

suma = 0
for i in range(len(lista_alturas)):
    suma += lista_alturas[i]

promedio = suma / len(lista_alturas)

contador = 0
for i in range(len(lista_alturas)):
    if lista_alturas[i] > promedio:
        contador += 1

print(f"El promedio de alturas es: {promedio:.2f}")
print("Cantidad de personas mas altas que el promedio:", contador)

# 12) Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.
lista_numeros = [12, 45, 3, 78, 22]

for i in range(len(lista_numeros)):
    if i == 0:
        mayor = lista_numeros[i]
    elif lista_numeros[i] > mayor:
        mayor = lista_numeros[i]

print("El mayor valor es:", mayor)

# 13) Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor de
# la lista y su posición.
lista_numeros = []
for i in range(5):
    valor = int(input(f"Ingrese el {i + 1}° numero: "))
    lista_numeros += [valor]

for i in range(len(lista_numeros)):
    if i == 0:
        menor = lista_numeros[i]
        posicion = i
    elif lista_numeros[i] < menor:
        menor = lista_numeros[i]
        posicion = i

print(f"El menor valor es {menor} y se encuentra en la posicion {posicion}.")

# 14) Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre de la persona
# con el nombre más corto.
lista_nombres = []
for i in range(5):
    nombre = input(f"Ingrese el nombre {i + 1}: ")
    lista_nombres += [nombre]

for i in range(len(lista_nombres)):
    if i == 0:
        mas_corto = lista_nombres[i]
    elif len(lista_nombres[i]) < len(mas_corto):
        mas_corto = lista_nombres[i]

print("El nombre mas corto es:", mas_corto)

# 15) Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir
# si dicho valor se encuentra en 2 o más posiciones en la lista)
lista_numeros = [8, 3, 8, 5, 1]

for i in range(len(lista_numeros)):
    if i == 0:
        mayor = lista_numeros[i]
    elif lista_numeros[i] > mayor:
        mayor = lista_numeros[i]

contador_repetidos = 0
for i in range(len(lista_numeros)):
    if lista_numeros[i] == mayor:
        contador_repetidos += 1

print("El mayor valor es:", mayor)
if contador_repetidos >= 2:
    print("El valor se repite en la lista.")

# 16) Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de
# realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o
# iguales a 18 años). Utilizar listas paralelas.
lista_nombres = []
lista_edades = []

for i in range(5):
    nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
    lista_nombres += [nombre]

    edad = int(input(f"Ingrese la edad de {nombre}: "))
    lista_edades += [edad]

print("Personas mayores de edad:")
for i in range(len(lista_nombres)):
    if lista_edades[i] >= 18:
        print(lista_nombres[i])


# 17) Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Mostrar la
# cantidad de productos que tienen un precio mayor al primer producto ingresado.
lista_productos = []
lista_precios = []

for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i + 1}: ")
    lista_productos += [producto]

    precio = float(input(f"Ingrese el precio de {producto}: "))
    lista_precios += [precio]

contador = 0
for i in range(len(lista_precios)):
    if lista_precios[i] > lista_precios[0]:
        contador += 1

print("Cantidad de productos con precio mayor al primero:", contador)


# 18) Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. Generar una
# tercer lista que surja de la suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista.
lista_a = []
lista_b = []

for i in range(4):
    valor = int(input(f"Ingrese el {i + 1}° numero de la lista A: "))
    lista_a += [valor]

for i in range(4):
    valor = int(input(f"Ingrese el {i + 1}° numero de la lista B: "))
    lista_b += [valor]

lista_suma = []
for i in range(4):
    lista_suma += [lista_a[i] + lista_b[i]]

for i in range(len(lista_suma)):
    print(lista_suma[i], end=" ")
print()

# 19) Realizar un programa que permita la registración de una cantidad determinada de alumnos y sus respectivas
# notas de exámenes y se deben procesar de acuerdo a lo siguiente:
# a) Ingresar la cantidad total de alumnos. (No se debe poder acceder a las opciones b,c y d si no se ingresó a la
# opción “a”)
# b) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas).
# c) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar
# "Promocionado" si la nota es mayor o igual a 6, "Aprobado" si la nota es 4 o 5, y colocar "Reprobado" si la
# nota es inferior a 4.
# d) Contar e imprimir por consola la cantidad de “Aprobados”, “Promocionados” y “Reprobados”.
cantidad_alumnos = 0
lista_nombres = []
lista_notas = []
cantidad_cargada = False

menu = """
 == GESTION DE ALUMNOS ==
a) Ingresar cantidad de alumnos
b) Ingresar nombre y nota de cada alumno
c) Listado de alumnos y condicion
d) Contar alumnos por condicion
e) Salir

Seleccione una opcion: """

while True:
    opcion = input(menu)

    match opcion:
        case "a":
            cantidad_alumnos = int(input("Ingrese la cantidad total de alumnos: "))
            while cantidad_alumnos < 1:
                cantidad_alumnos = int(input("ERROR, ingrese un numero mayor a 0: "))
            cantidad_cargada = True
            lista_nombres = []
            lista_notas = []
            print(f"Cantidad de alumnos establecida: {cantidad_alumnos}")

        case "b":
            if cantidad_cargada == False:
                print("ERROR, primero debe ingresar la cantidad de alumnos (opcion a).")
            else:
                lista_nombres = []
                lista_notas = []
                for i in range(cantidad_alumnos):
                    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
                    lista_nombres += [nombre]

                    nota = int(input(f"Ingrese la nota de {nombre}: "))
                    while nota < 0 or nota > 10:
                        nota = int(input(f"ERROR, ingrese una nota valida (0-10) para {nombre}: "))
                    lista_notas += [nota]

        case "c":
            if cantidad_cargada == False:
                print("ERROR, primero debe ingresar la cantidad de alumnos (opcion a).")
            else:
                for i in range(len(lista_nombres)):
                    if lista_notas[i] >= 6:
                        condicion = "Promocionado"
                    elif lista_notas[i] >= 4:
                        condicion = "Aprobado"
                    else:
                        condicion = "Reprobado"
                    print(f"{lista_nombres[i]} - Nota: {lista_notas[i]} - Condicion: {condicion}")

        case "d":
            if cantidad_cargada == False:
                print("ERROR, primero debe ingresar la cantidad de alumnos (opcion a).")
            else:
                contador_promocionados = 0
                contador_aprobados = 0
                contador_reprobados = 0

                for i in range(len(lista_notas)):
                    if lista_notas[i] >= 6:
                        contador_promocionados += 1
                    elif lista_notas[i] >= 4:
                        contador_aprobados += 1
                    else:
                        contador_reprobados += 1

                print("Cantidad de Promocionados:", contador_promocionados)
                print("Cantidad de Aprobados:", contador_aprobados)
                print("Cantidad de Reprobados:", contador_reprobados)

        case "e":
            print("Programa terminado.")
            break

        case _:
            print("Opcion Incorrecta")