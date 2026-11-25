# Abril Dobal
# 1. Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.
clave_real = "UTN750"

clave_ingresada = input("Ingrese su clave: ")

while clave_ingresada != clave_real:
    clave_ingresada = input("ERROR, reingrese su clave: ")

print("Clave correcta")

# 2. Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.
clave_real = "UTN750"
intentos = 0  # CONTADOR

while True:
    clave_ingresada = input("Ingrese su clave: ")
    intentos += 1

    if clave_ingresada == clave_real:
        print("Clave correcta")
        break

    if intentos == 3:
        print("ERROR, se agotaron los intentos")
        break

# 3. Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
nota = int(input("Ingrese una nota (1-10): "))

while nota < 1 or nota > 10:
    nota = int(input("ERROR, reingrese la nota (1-10): "))

print(f"La nota ingresada es: {nota}")

# 4. Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.
color = input("Ingrese un color (Rojo/Verde/Azul): ")

while color != "Rojo" and color != "Verde" and color != "Azul":
    color = input("ERROR, reingrese el color (Rojo/Verde/Azul): ")

print(f"El color ingresado es: {color}")

# Integrador Validaciones
# 1. Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
# Los datos requeridos son:
# a. Apellido
# b. Edad, entre 18 y 90 años inclusive.
# c. Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# d. Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

# Una vez ingresados y validados los datos, mostrarlos por pantalla.

apellido = input("Ingrese su apellido: ")

edad = int(input("Ingrese su edad (18-90): "))
while edad < 18 or edad > 90:
    edad = int(input("ERROR, reingrese su edad (18-90): "))

estado_civil = input("Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a, Viudo/a): ")
while estado_civil != "Soltero/a" and estado_civil != "Casado/a" and estado_civil != "Divorciado/a" and estado_civil != "Viudo/a":
    estado_civil = input("ERROR, reingrese su estado civil (Soltero/a, Casado/a, Divorciado/a, Viudo/a): ")

legajo = int(input("Ingrese su número de legajo (4 cifras, sin ceros a la izquierda): "))
while legajo < 1000 or legajo > 9999:
    legajo = int(input("ERROR, reingrese su número de legajo (4 cifras, sin ceros a la izquierda): "))

print("---- DATOS CARGADOS ----")
print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado civil: {estado_civil}")
print(f"Legajo: {legajo}")