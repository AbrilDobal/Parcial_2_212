# Abril Dobal 
# Desafío: Encuesta Tecnológica en UTN Technologies
# UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo en Python, con el objetivo de revolucionar el mercado.
# Las tecnologías en evaluación son:
#  🔹 Inteligencia Artificial (IA)
#  🔹 Realidad Virtual/Aumentada (RV/RA)
#  🔹 Internet de las Cosas (IOT)
# Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito de analizar ciertas métricas.
# 🔹 Recolección de Datos
# Cada empleado encuestado deberá proporcionar la siguiente información:
#  ✔️ Nombre
#  ✔️ Edad (debe ser 18 años o más)
#  ✔️ Género (Masculino, Femenino, Otro)
#  ✔️ Tecnología elegida (IA, RV/RA, IOT)
# El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.
# 🔹 Análisis de Datos
# A partir de las respuestas, se deben calcular las siguientes métricas:
# 1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
# 2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
# Su género no sea Femenino 
# Su edad está entre los 33 y 40 años.
# 3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.


# 🔹 Requisitos del Programa
#  ✔️ Los datos deben solicitarse y validarse correctamente.
#  ✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis.
#  ✔️ Presentar los resultados de manera clara y organizada.


contador = 0  # CONTADOR (recorre los 10 empleados)

contador_metrica1 = 0        # ACUMULADOR (masculino + IOT o IA + 25-50 años)
contador_subset_total = 0    # ACUMULADOR (no femenino + 33-40 años)
contador_subset_no_ia = 0    # ACUMULADOR (del subset anterior, los que NO votaron IA)

bandera_primer_masculino = True  # BANDERA

while contador < 10:
    contador += 1

    print(f"--- Empleado {contador} ---")

    nombre = input("Ingrese el nombre: ")

    edad = int(input("Ingrese la edad (18 o más): "))
    while edad < 18:
        edad = int(input("ERROR, reingrese la edad (18 o más): "))

    genero = input("Ingrese el género (Masculino,Femenino,Otro): ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input("ERROR, reingrese el género (Masculino,Femenino,Otro): ")

    tecnologia = input("Ingrese la tecnología elegida (IA,RV/RA,IOT): ")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input("ERROR, reingrese la tecnología (IA,RV/RA,IOT): ")

    # ===== MÉTRICA 1: masculino + (IOT o IA) + edad entre 25 y 50 =====
    if genero == "Masculino" and (tecnologia == "IOT" or tecnologia == "IA"):
        if edad >= 25 and edad <= 50:
            contador_metrica1 += 1

    # ===== MÉTRICA 2: no femenino + edad entre 33 y 40 -> % que NO votó IA =====
    if genero != "Femenino" and edad >= 33 and edad <= 40:
        contador_subset_total += 1
        if tecnologia != "IA":
            contador_subset_no_ia += 1

    # ===== MÉTRICA 3: empleado masculino de mayor edad =====
    if genero == "Masculino":
        if bandera_primer_masculino == True:
            mayor_edad_masculino = edad
            nombre_mayor_masculino = nombre
            tecnologia_mayor_masculino = tecnologia
            bandera_primer_masculino = False
        elif edad > mayor_edad_masculino:
            mayor_edad_masculino = edad
            nombre_mayor_masculino = nombre
            tecnologia_mayor_masculino = tecnologia

# ===================== RESULTADOS =====================
print("===== RESULTADOS DE LA ENCUESTA =====")

print(f"1. Empleados masculinos (25-50 años) que votaron IOT o IA: {contador_metrica1}")

if contador_subset_total != 0:
    porcentaje_no_ia = (contador_subset_no_ia / contador_subset_total) * 100
    print(f"2. Porcentaje que NO votó IA (no femenino, 33-40 años): {porcentaje_no_ia}%")
else:
    print("2. No hubo empleados no-femeninos entre 33 y 40 años.")

if bandera_primer_masculino == False:
    print(f"3. Empleado masculino de mayor edad: {nombre_mayor_masculino} ({mayor_edad_masculino} años)")
    print(f"   Tecnología votada: {tecnologia_mayor_masculino}")
else:
    print("3. No se registraron empleados masculinos.")