# 1- Crear y cargar una matriz de 4x4 con datos numéricos aleatorios entre 1 y 9 inclusive, en formato string.
# Mostrar los números pares de esa matriz (en filas y columnas) y reemplazar los números impares con
# cadenas vacías para ocultarlos.

import random as r

def punto_1():
    matriz = []
    # 1. Crear y cargar la matriz 4x4 con strings aleatorios del '1' al '9'
    for _ in range(4):
        fila = []
        for _ in range(4):
            num_str = str(r.randint(1, 9))
            fila += [num_str]
        matriz += [fila]
        
    print("--- Matriz Original ---")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()
        
    print("\n--- Matriz Procesada (Pares visibles, impares ocultos) ---")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            # Convertimos a entero para evaluar si es par
            numero = int(matriz[i][j])
            if numero % 2 == 0:
                print(matriz[i][j], end=" ")
            else:
                print(" ", end=" ") # Reemplazamos por cadena vacía / espacio
        print()

# 2- Generar una matriz de 3x3 cargando datos numéricos del 1 al 9 inclusive en celdas aleatorias, sin que se
# repitan los números (al estilo Sudoku).

def punto_2() -> list[list]:
    # Creamos una lista con los números del 1 al 9
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    r.shuffle(numeros) # Mezcla los elementos de forma aleatoria sin repetirlos
    
    matriz = []
    contador = 0
    for i in range(3):
        fila = []
        for j in range(3):
            fila += [numeros[contador]]
            contador += 1
        matriz += [fila]
        
    return matriz

# 3- Desarrollar una función que reciba 2 matrices, los sume y devuelva la matriz resultante, sin modificar las
# matrices originales.

def sumar_matrices_inmutable(matriz_a: list[list], matriz_b: list[list]) -> list[list] | None:
    retorno = None
    # Validamos que no estén vacías y que tengan las mismas dimensiones
    if len(matriz_a) != 0 and len(matriz_a) == len(matriz_b) and len(matriz_a[0]) != 0 and len(matriz_a[0]) == len(matriz_b[0]):
        matriz_c = []
        for i in range(len(matriz_a)):
            fila = []
            for j in range(len(matriz_a[i])):
                suma = matriz_a[i][j] + matriz_b[i][j]
                fila += [suma]
            matriz_c += [fila]
        retorno = matriz_c
    return retorno

# 4- Desarrollar una función que reciba una matriz y un número escalar, multiplicar la matriz por el número
# escalar y retornar la matriz resultante, sin modificar la matriz original.

def multiplicar_matriz_escalar_inmutable(matriz: list[list], escalar: int) -> list[list] | None:
    retorno = None
    if len(matriz) != 0 and len(matriz[0]) != 0:
        matriz_r = []
        for i in range(len(matriz)):
            fila = []
            for j in range(len(matriz[i])):
                multiplicacion = matriz[i][j] * escalar
                fila += [multiplicacion]
            matriz_r += [fila]
        retorno = matriz_r
    return retorno

# 5- Desarrollar una función que reciba dos matrices, y las multiplique entre sí. Se debe validar que las matrices
# recibidas por parámetro se puedan multiplicar entre sí y devolver la matriz resultante, sin alterar las matrices
# originales, caso contrario la función devolverá un None.

def multiplicar_dos_matrices(matriz_a: list[list], matriz_b: list[list]) -> list[list] | None:
    retorno = None
    # Validar que no estén vacías y que se cumpla la regla de multiplicación
    if len(matriz_a) != 0 and len(matriz_a[0]) != 0 and len(matriz_b) != 0 and len(matriz_b[0]) != 0:
        if len(matriz_a[0]) == len(matriz_b):
            filas_a = len(matriz_a)
            cols_b = len(matriz_b[0])
            cols_a = len(matriz_a[0])
            
            # Inicializamos la matriz resultado en ceros
            matriz_r = []
            for i in range(filas_a):
                fila = []
                for j in range(cols_b):
                    fila += [0]
                matriz_r += [fila]
                
            # Algoritmo de producto punto
            for i in range(filas_a):
                for j in range(cols_b):
                    suma = 0
                    for k in range(cols_a):
                        suma += matriz_a[i][k] * matriz_b[k][j]
                    matriz_r[i][j] = suma
            retorno = matriz_r
            
    return retorno

# 6- Desarrollar un programa que cuente con un menú y las siguientes opciones:
# a) Generar una matriz con números aleatorios. Las dimensiones y los rangos de números se deben pasar
# por parámetros de la función generadora. No se debe poder acceder a las demás opciones si la matriz
# no fue generada.
# b) Mostrar la matriz generada.
# c) Determinar si la matriz contiene series de números consecutivos (en horizontal o en vertical).
# d) Determinar la cantidad total de series (las series de números consecutivos de más de dos números
# cuentan como una sola).
# e) Determinar el largo de la serie más corta, y mostrar todas las series de ese largo.
# f) Determinar el largo de la serie más larga, y mostrar todas las series de ese largo.
# g) Salir.

def inicializar_matriz(cant_filas: int, cant_columnas: int, valor_inicial: any = None) -> list[list]:
    matriz = []
    for _ in range(cant_filas): 
        fila = []
        for _ in range(cant_columnas):
            fila += [valor_inicial]
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz: list[list]) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

def generar_matriz_aleatoria(filas: int, cols: int, min_val: int, max_val: int) -> list[list]:
    matriz = inicializar_matriz(filas, cols)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = r.randint(min_val, max_val)
    return matriz

def encontrar_series(matriz: list[list]):
    # Función auxiliar para detectar series consecutivas (ej: x[j+1] == x[j] + 1)
    series = []
    
    # 1. Buscar en horizontal
    for i in range(len(matriz)):
        serie_actual = [matriz[i][0]]
        for j in range(1, len(matriz[i])):
            if matriz[i][j] == matriz[i][j-1] + 1:
                serie_actual += [matriz[i][j]]
            else:
                if len(serie_actual) >= 2:
                    series += [serie_actual]
                serie_actual = [matriz[i][j]]
        if len(serie_actual) >= 2:
            series += [serie_actual]
            
    # 2. Buscar en vertical
    if len(matriz) > 0:
        cols = len(matriz[0])
        for j in range(cols):
            serie_actual = [matriz[0][j]]
            for i in range(1, len(matriz)):
                if matriz[i][j] == matriz[i-1][j] + 1:
                    serie_actual += [matriz[i][j]]
                else:
                    if len(serie_actual) >= 2:
                        series += [serie_actual]
                    serie_actual = [matriz[i][j]]
            if len(serie_actual) >= 2:
                series += [serie_actual]
                
    return series

def menu_principal():
    matriz_actual = None
    bandera_generada = False
    
    while True:
        print("\n================ MENÚ DE MATRICES ================")
        print("a) Generar matriz con números aleatorios")
        print("b) Mostrar la matriz generada")
        print("c) Determinar si contiene series de números consecutivos")
        print("d) Determinar la cantidad total de series")
        print("e) Determinar el largo de la serie más corta y mostrarlas")
        print("f) Determinar el largo de la serie más larga y mostrarlas")
        print("g) Salir")
        
        opcion = input("Ingrese una opción (a-g): ").lower()
        
        if opcion == 'a':
            f = int(input("Ingrese cantidad de filas: "))
            c = int(input("Ingrese cantidad de columnas: "))
            min_val = int(input("Ingrese valor mínimo: "))
            max_val = int(input("Ingrese valor máximo: "))
            matriz_actual = generar_matriz_aleatoria(f, c, min_val, max_val)
            bandera_generada = True
            print("¡Matriz generada con éxito!")
            
        elif opcion == 'b':
            if bandera_generada == False:
                print("Error: Debe generar la matriz primero (Opción a).")
            else:
                print("\n--- Matriz Actual ---")
                mostrar_matriz(matriz_actual)
                
        elif opcion == 'c':
            if bandera_generada == False:
                print("Error: Debe generar la matriz primero (Opción a).")
            else:
                series = encontrar_series(matriz_actual)
                if len(series) > 0:
                    print(f"Sí, la matriz contiene series consecutivas. Total encontradas: {len(series)}")
                else:
                    print("La matriz no contiene series de números consecutivos.")
                    
        elif opcion == 'd':
            if bandera_generada == False:
                print("Error: Debe generar la matriz primero (Opción a).")
            else:
                series = encontrar_series(matriz_actual)
                print(f"Cantidad total de series consecutivas: {len(series)}")
                
        elif opcion == 'e':
            if bandera_generada == False:
                print("Error: Debe generar la matriz primero (Opción a).")
            else:
                series = encontrar_series(matriz_actual)
                if len(series) == 0:
                    print("No hay series en la matriz.")
                else:
                    min_largo = len(series[0])
                    for s in series:
                        if len(s) < min_largo:
                            min_largo = len(s)
                    print(f"El largo de la serie más corta es: {min_largo}")
                    print("Series de ese largo:")
                    for s in series:
                        if len(s) == min_largo:
                            print(s)
                            
        elif opcion == 'f':
            if bandera_generada == False:
                print("Error: Debe generar la matriz primero (Opción a).")
            else:
                series = encontrar_series(matriz_actual)
                if len(series) == 0:
                    print("No hay series en la matriz.")
                else:
                    max_largo = len(series[0])
                    for s in series:
                        if len(s) > max_largo:
                            max_largo = len(s)
                    print(f"El largo de la serie más larga es: {max_largo}")
                    print("Series de ese largo:")
                    for s in series:
                        if len(s) == max_largo:
                            print(s)
                            
        elif opcion == 'g':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Para ejecutar el menú:
menu_principal()