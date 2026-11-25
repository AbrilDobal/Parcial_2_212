# BUCLES

# While: se usa cuando DESCONOCEMOS la cantidad de repeticiones (iteraciones).

# Ingresar por consola 3 NOTAS, calcular la nota promedio de mi cursada.

# nota_uno = int(input("Ingrese la nota del 1° parcial: "))
# nota_dos = int(input("Ingrese la nota del 2° parcial: "))
# nota_tres = int(input("Ingrese la nota del 3° parcial: "))
# nota_cuatro = int(input("Ingrese la nota del 4° parcial: "))
# nota_cinco = int(input("Ingrese la nota del 5° parcial: "))
# nota_seis = int(input("Ingrese la nota del 6° parcial: "))


# suma_notas = nota_uno + nota_dos + nota_tres
# promedio = suma_notas / 3

# promedio = (nota_uno + nota_dos + nota_tres + nota_cuatro + nota_cinco + nota_seis) / 6

# print(f"El promedio es: {promedio:.2f}")

# print(f"El promedio es: {promedio:.0f}")
# print(f"El promedio es: {promedio:.5f}")
# print(promedio)


# ================================= MISMO EJEMPLO PERO CON WHILE =================================

# 3 notas: 
# cantidad_notas = int(input("Cuantos examenes rendiste?: "))
# suma_notas = 0 # ACUMULADOR (SIEMPRE SE DEBE INICIALIZAR) El acumulador suma valores VARIABLES.
# contador_notas = 0 # CONTADOR (SIEMPRE SE DEBE INICIALIZAR) El contador suma valores CONSTANTES.

# while contador_notas < cantidad_notas: # mientras que 
#     contador_notas += 1 #  contador_notas = contador_notas + 1
#     nota = int(input(f"Ingrese la nota del {contador_notas}° parcial: ")) # 0 + 5, 7, 9
#     suma_notas = suma_notas + nota # suma_notas += nota

# if cantidad_notas != 0:
#     promedio = suma_notas / cantidad_notas
#     print(f"El promedio es: {promedio:.2f}")
# else:
#     print("ERROR, Division por cero.")

# if condicion:
    # bloque

# while condicion: # mientras que
#     # bloque verdadero



# ============================================================

# Mostrar del 1-10

# contador = 1
# while contador <= 10: # < 11
#     print(contador)
#     contador += 1


# contador = 0
# while contador < 10:
#     contador += 1
#     print(contador)


# contador = 0
# while True:
#     print(contador)
#     contador += 1

# print("Programa terminado")




# =============================== VALIDACIONES ===============================
# Las validaciones buscan EL ERROR!

# 1) Contraseña.
# contrasenia_real = "UTN750"

# contrasenia_ingresada = input("Ingrese su contraseña: ")

# while contrasenia_ingresada != contrasenia_real:
#     contrasenia_ingresada = input("ERROR, reingrese su contraseña: ")
 
# if contrasenia_real == contrasenia_ingresada:
#     print("Contraseña correcta")
# else:
#     print("ERROR, Contraseña Incorrecta!")


# 2) Rango numerico.

# edad = int(input("Ingrese su edad (18-120): "))
# # VERSION PYTHON     18 <= edad <= 120  # EVITEN UTILIZAR ESTO.
# # POSITIVO: edad >= 18 and edad <= 120
# # while not (edad >= 18 and edad <= 120):
# while edad < 18 or edad > 120:
#     edad = int(input("ERROR, reingrese su edad (18-120): "))



# 3) Cadenas.
# Validos: "Comercial", "Penal", "Tributario"
categoria = input("Ingrese la categoria: ")
# POSITIVA: if categoria == "Comercial" or categoria == "Penal" or categoria == "Tributario":
# NEGACION: not (categoria == "Comercial" or categoria == "Penal" or categoria == "Tributario")
while categoria != "Comercial" and categoria != "Penal" and categoria != "Tributario":
    categoria = input("ERROR, reingrese la categoria (Comercial/Penal/Tributario): ")


print("BIENVENIDO USUARIO!")

# RETOMAR EN LA VALIDACION DE CADENAS, HACER LA NEGACION DE LA CONDICION.