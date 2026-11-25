import random as r

# 1) Generar matriz de 9x9 con números aleatorios del 1 al 9 inclusive
def generar_matriz_9x9() -> list[list]:
    matriz = []
    for _ in range(9):
        fila = []
        for _ in range(9):
            fila += [r.randint(1, 9)]
        matriz += [fila]
    return matriz


# 2) Guardar la matriz generada en un archivo CSV (columnas con comas, filas con \n)
def guardar_matriz_csv(matriz: list[list], ruta: str) -> None:
    with open(ruta, "w") as archivo:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                archivo.write(str(matriz[i][j]))
                # Si no es el último elemento de la fila, agregamos coma
                if j < len(matriz[i]) - 1:
                    archivo.write(",")
            # Agregamos salto de línea al terminar cada fila
            archivo.write("\n")
    print(f"Matriz guardada exitosamente en '{ruta}'.")


# 3) Leer archivo CSV y construir una matriz en Python
def leer_matriz_csv(ruta: str) -> list[list]:
    matriz = []
    with open(ruta, "r") as archivo:
        datos = archivo.read()
    
    datos_limpios = datos.strip()
    if len(datos_limpios) > 0:
        lineas = datos_limpios.split("\n")
        for i in range(len(lineas)):
            valores_str = lineas[i].split(",")
            fila = []
            for j in range(len(valores_str)):
                fila += [int(valores_str[j])]
            matriz += [fila]
            
    return matriz


# 4) Mostrar la matriz construida dándole formato en la terminal
def mostrar_matriz(matriz: list[list]) -> None:
    print("\n--- MATRIZ ---")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()


# 5) Recibir matriz y guardar pares en "numeros_pares.txt" e impares en "numeros_impares.txt"
def separar_pares_impares(matriz: list[list]) -> None:
    pares = []
    impares = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numero = matriz[i][j]
            if numero % 2 == 0:
                pares += [str(numero)]
            else:
                impares += [str(numero)]
                
    # Guardar pares
    with open("numeros_pares.txt", "w") as archivo_pares:
        for i in range(len(pares)):
            archivo_pares.write(pares[i] + ",")
            
    # Guardar impares
    with open("numeros_impares.txt", "w") as archivo_impares:
        for i in range(len(impares)):
            archivo_impares.write(impares[i] + ",")
            
    print("Archivos 'numeros_pares.txt' y 'numeros_impares.txt' generados con éxito.")


# 6) Agregar nombre, apellido y división al final del archivo CSV de la matriz
def agregar_datos_personales(ruta: str, nombre: str, apellido: str, division: str) -> None:
    with open(ruta, "a") as archivo:
        archivo.write(f"\nAlumno: {nombre},{apellido},Division: {division}\n")
    print("Datos personales agregados al final del archivo CSV.")


# =====================================================================
# PRUEBA DE LAS FUNCIONES DE MATRICES
# =====================================================================
def probar_modulo_matrices():
    ruta_archivo = "matriz_9x9.csv"
    
    # 1. Generar matriz aleatoria 9x9
    mi_matriz = generar_matriz_9x9()
    
    # 2. Guardar en CSV
    guardar_matriz_csv(mi_matriz, ruta_archivo)
    
    # 3. Leer la matriz desde el archivo CSV
    matriz_leida = leer_matriz_csv(ruta_archivo)
    
    # 4. Mostrar la matriz leída en la terminal
    mostrar_matriz(matriz_leida)
    
    # 5. Guardar pares e impares en archivos TXT separados
    separar_pares_impares(matriz_leida)
    
    # 6. Agregar nombre, apellido y división al archivo CSV
    agregar_datos_personales(ruta_archivo, "Juan", "Perez", "212")

# Para probar:
probar_modulo_matrices()