#Abril Dobal
# 1. Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
contador = 0

while contador < 10:
    contador += 1
    print(contador)

# 2. Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
contador = 11

while contador > 1:
    contador -= 1
    print(contador)

# 3. Mostrar la suma de los números desde el 1 hasta el 10.
suma = 0       # ACUMULADOR
contador = 0   # CONTADOR

while contador < 10:
    contador += 1
    suma = suma + contador

print(f"La suma es: {suma}")

# 4. Mostrar la suma de los números pares desde el 1 hasta el 10.
suma = 0       # ACUMULADOR
contador = 0   # CONTADOR

while contador < 10:
    contador += 1
    if contador % 2 == 0:
        suma = suma + contador

print(f"La suma de los pares es: {suma}")

# 5. Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.
suma = 0       # ACUMULADOR
contador = 0   # CONTADOR

while contador < 5:
    contador += 1
    numero = int(input(f"Ingrese el {contador} número: "))
    suma = suma + numero

promedio = suma / 5
print(f"La suma es: {suma}")
print(f"El promedio es: {promedio}")

# 6. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.
suma = 0       # ACUMULADOR
contador = 0   # CONTADOR

while True:
    contador += 1
    numero = int(input(f"Ingrese el {contador} número: "))
    suma = suma + numero

    continuar = input("¿Desea ingresar otro número? (s/n): ")
    if continuar == "n":
        break

if contador != 0:
    promedio = suma / contador
    print(f"La suma es: {suma}")
    print(f"El promedio es: {promedio}")

# 7. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.
suma_positivos = 0      # ACUMULADOR
producto_negativos = 1  # ACUMULADOR
contador = 0             # CONTADOR

while True:
    contador += 1
    numero = int(input(f"Ingrese el {contador} número: "))

    if numero > 0:
        suma_positivos = suma_positivos + numero
    elif numero < 0:
        producto_negativos = producto_negativos * numero

    continuar = input("¿Desea ingresar otro número? (s/n): ")
    if continuar == "n":
        break

print(f"La suma de los positivos es: {suma_positivos}")
print(f"El producto de los negativos es: {producto_negativos}")

# 8. Ingresar 10 números enteros. Determinar el máximo y el mínimo.
contador = 0                  # CONTADOR
bandera_primer_valor = True   # BANDERA

while contador < 10:
    contador += 1
    numero = int(input(f"Ingrese el {contador} número: "))

    if bandera_primer_valor == True:
        maximo = numero
        minimo = numero
        bandera_primer_valor = False
    else:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

print(f"El máximo es: {maximo}")
print(f"El mínimo es: {minimo}")

# Anexo:
# 9. Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.
suma = 0       # ACUMULADOR
contador = 0   # CONTADOR

while True:
    contador += 1
    numero = int(input(f"Ingrese el {contador} número: "))
    suma = suma + numero

    if contador >= 5:
        continuar = input("¿Desea ingresar otro número? (s/n): ")
        if continuar == "n":
            break

promedio = suma / contador
print(f"La suma es: {suma}")
print(f"El promedio es: {promedio}")

# 10. Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.
suma = 0       # ACUMULADOR
contador = 0   # CONTADOR

while True:
    contador += 1
    numero = int(input(f"Ingrese el {contador} número: "))
    suma = suma + numero

    if contador >= 10:
        break

    if contador >= 5:
        continuar = input("¿Desea ingresar otro número? (s/n): ")
        if continuar == "n":
            break

promedio = suma / contador
print(f"La suma es: {suma}")
print(f"El promedio es: {promedio}")

# Integrador While
# 1. Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
# a. La suma acumulada de los números negativos.
# b. La suma acumulada de los números positivos.
# c. La cantidad de números negativos ingresados.
# d. El promedio de los números positivos.
# e. El número positivo más grande.
# f. El porcentaje de números negativos ingresados, respecto del total de ingresos.

suma_negativos = 0             # ACUMULADOR
suma_positivos = 0             # ACUMULADOR
cantidad_negativos = 0         # CONTADOR
cantidad_positivos = 0         # CONTADOR
cantidad_total = 0              # CONTADOR
bandera_primer_positivo = True  # BANDERA

while True:
    numero = int(input("Ingrese un número (0 para salir): "))

    if numero == 0:
        break

    cantidad_total += 1

    if numero < 0:
        suma_negativos = suma_negativos + numero
        cantidad_negativos += 1
    else:
        suma_positivos = suma_positivos + numero
        cantidad_positivos += 1

        if bandera_primer_positivo == True:
            mayor_positivo = numero
            bandera_primer_positivo = False
        elif numero > mayor_positivo:
            mayor_positivo = numero

print(f"1. Suma de negativos: {suma_negativos}")
print(f"2. Suma de positivos: {suma_positivos}")
print(f"3. Cantidad de negativos: {cantidad_negativos}")

if cantidad_positivos != 0:
    promedio_positivos = suma_positivos / cantidad_positivos
    print(f"4. Promedio de positivos: {promedio_positivos}")
    print(f"5. Mayor positivo: {mayor_positivo}")
else:
    print("4. No se ingresaron números positivos.")
    print("5. No hay un mayor positivo.")

if cantidad_total != 0:
    porcentaje_negativos = (cantidad_negativos / cantidad_total) * 100
    print(f"6. Porcentaje de negativos: {porcentaje_negativos}%")
else:
    print("6. No se ingresaron números.")