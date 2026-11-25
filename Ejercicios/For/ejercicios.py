# 1. Mostrar los números ascendentes desde el 1 al 10
for num in range(1, 11):
    print(num)

# 2. Mostrar los números descendentes desde el 10 al 1
for num in range(10, 0, -1):
    print(num)

# 3. Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
numero = int(input("Ingrese un número: "))
while numero < 0:
    numero = int(input("ERROR, ingrese un número mayor o igual a 0: "))

for num in range(0, numero + 1):
    print(num)

# 4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:
# 	5 x 0 = 0
# 	5 x 1  = 5
# 	5 x 2 = 10
# 	5 x 3  = 15 …
numero = int(input("Ingrese un número: "))

for i in range(0, 11):
    print(f"{numero} x {i} = {numero * i}")

# 5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
suma = 0       # ACUMULADOR
contador = 0   # CONTADOR

for i in range(10):
    numero = int(input(f"Ingrese el {i + 1} número (0 para salir): "))

    if numero == 0:
        break

    suma = suma + numero
    contador += 1

if contador != 0:
    promedio = suma / contador
    print(f"La suma es: {suma}")
    print(f"El promedio es: {promedio}")
else:
    print("No se ingresaron números.")

# 6. Imprimir los números múltiplos de 3 entre el 1 y el 10.
for num in range(1, 11):
    if num % 3 == 0:
        print(num)

# 7. Mostrar los números pares que hay desde la unidad hasta el número 50.
for num in range(2, 51, 2):
    print(num)

# 8. Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:
# 1
# 12
# 123
# 1234
# 12345
numero = int(input("Ingrese un número: "))

for i in range(1, numero + 1):
    linea = ""  # ACUMULADOR (se reinicializa en cada fila)
    for j in range(1, i + 1):
        linea = linea + str(j)  # linea += str(j)
    print(linea)

# 9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.
numero = int(input("Ingrese un número: "))
contador = 0   # CONTADOR

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
        contador += 1

print(f"Cantidad de divisores: {contador}")

# 10. Ingresar un número. Determinar si el número es primo o no.
numero = int(input("Ingrese un número: "))
es_primo = True   # BANDERA

if numero < 2:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

if es_primo == True:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")

# 11. Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.
numero = int(input("Ingrese un número: "))
contador_primos = 0   # CONTADOR

for num in range(2, numero + 1):
    es_primo = True   # BANDERA

    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break

    if es_primo == True:
        print(num)
        contador_primos += 1

print(f"Cantidad de primos encontrados: {contador_primos}")