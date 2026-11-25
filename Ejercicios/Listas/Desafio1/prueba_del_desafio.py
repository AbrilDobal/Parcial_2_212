
# ===== Funciones especificas =====
def es_positivo(numero: int) -> bool:
    """
    Determina si un numero es positivo.
    Parametros:
        - numero (int): el numero a evaluar.
    Return:
        - bool: True si es positivo, False caso contrario.
    """
    resultado = numero > 0
    return resultado


def es_negativo(numero: int) -> bool:
    """
    Determina si un numero es negativo.
    Parametros:
        - numero (int): el numero a evaluar.
    Return:
        - bool: True si es negativo, False caso contrario.
    """
    resultado = numero < 0
    return resultado


def es_par(numero: int) -> bool:
    """
    Determina si un numero es par.
    Parametros:
        - numero (int): el numero a evaluar.
    Return:
        - bool: True si es par, False caso contrario.
    """
    resultado = numero % 2 == 0
    return resultado

def es_impar(numero: int) -> bool:
    """
    Determina si un numero es impar.
    Parametros:
        - numero (int): el numero a evaluar.
    Return:
        - bool: True si es impar, False caso contrario.
    """
    resultado = numero % 2 != 0
    return resultado


# ===== Funciones generales =====

def ingresar_numeros(cantidad: int) -> list:
    """
    Solicita al usuario el ingreso de una cantidad de numeros enteros, validando el rango -1000 a 1000.
    Parametros:
        - cantidad (int): cantidad de numeros a ingresar.
    Return:
        - list: lista con los numeros ingresados, en orden.
    """
    lista = []
    for i in range(cantidad):
        numero = int(input(f"Ingrese el numero {i + 1} (-1000 a 1000): "))
        while numero < -1000 or numero > 1000:
            numero = int(input(f"ERROR, debe estar entre -1000 y 1000. Reingrese el numero {i + 1}: "))
        lista += [numero]
    return lista


def contar_positivos_negativos(lista: list) -> list:
    """
    Cuenta cuantos elementos de la lista son positivos y cuantos son negativos.
    Parametros:
        - lista (list): lista de numeros enteros.
    Return:
        - list: [cantidad_positivos, cantidad_negativos]
    """
    cantidad_positivos = 0
    cantidad_negativos = 0
    for i in range(len(lista)):
        if es_positivo(lista[i]):
            cantidad_positivos += 1
        elif es_negativo(lista[i]):
            cantidad_negativos += 1
    resultado = [cantidad_positivos, cantidad_negativos]
    return resultado


def sumar_pares(lista: list) -> int:
    """
    Suma los elementos pares de una lista de numeros.
    Parametros:
        - lista (list): lista de numeros enteros.
    Return:
        - int: la suma de los numeros pares.
    """
    suma = 0
    for i in range(len(lista)):
        if es_par(lista[i]):
            suma += lista[i]
    return suma


def mayor_impar(lista: list) -> int:
    """
    Busca el mayor numero impar de una lista.
    Parametros:
        - lista (list): lista de numeros enteros.
    Return:
        - int: el mayor numero impar encontrado (None si no hay ninguno).
    """
    mayor = None
    for i in range(len(lista)):
        if es_impar(lista[i]):
            if mayor == None or lista[i] > mayor:
                mayor = lista[i]
    return mayor


def listar_elementos(lista: list) -> None:
    """
    Muestra por pantalla todos los elementos de una lista, en el orden ingresado.
    Parametros:
        - lista (list): lista de numeros enteros.
    Return:
        None
    """
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()


def listar_pares(lista: list) -> None:
    """
    Muestra por pantalla unicamente los numeros pares de una lista.
    Parametros:
        - lista (list): lista de numeros enteros.
    Return:
        None
    """
    for i in range(len(lista)):
        if es_par(lista[i]):
            print(lista[i], end=" ")
    print()


def listar_posiciones_impares(lista: list) -> None:
    """
    Muestra por pantalla los numeros que se encuentran en posiciones (indices) impares de una lista.
    Parametros:
        - lista (list): lista de numeros enteros.
    Return:
        None
    """
    for i in range(len(lista)):
        if i % 2 != 0:
            print(lista[i], end=" ")
    print()


# ===== Prueba individual de cada funcion =====

lista_prueba = [4, -7, 10, 0, -3, 15, -1000, 999, 8, 2]

print("Lista de prueba:", end=" ")
listar_elementos(lista_prueba)

conteo = contar_positivos_negativos(lista_prueba)
print(f"Positivos: {conteo[0]}, Negativos: {conteo[1]}")

print("Suma de pares:", sumar_pares(lista_prueba))
print("Mayor impar:", mayor_impar(lista_prueba))

print("Numeros pares:", end=" ")
listar_pares(lista_prueba)

print("Numeros en posiciones impares:", end=" ")
listar_posiciones_impares(lista_prueba)


# ===== Programa principal =====

lista_numeros = []
datos_cargados = False

menu = """
 == MENU DE NUMEROS ==
1) Ingresar datos
2) Cantidad de positivos y negativos
3) Suma de los numeros pares
4) Mayor numero impar
5) Listar los numeros ingresados
6) Listar los numeros pares
7) Listar los numeros en posiciones impares
8) Salir

Seleccione una opcion: """

while True:
    opcion = input(menu)

    match opcion:
        case "1":
            lista_numeros = ingresar_numeros(10)
            datos_cargados = True
            print("Numeros cargados correctamente.")

        case "2":
            if datos_cargados == False:
                print("ERROR, primero debe ingresar los datos (opcion 1).")
            else:
                conteo = contar_positivos_negativos(lista_numeros)
                print(f"Positivos: {conteo[0]}, Negativos: {conteo[1]}")

        case "3":
            if datos_cargados == False:
                print("ERROR, primero debe ingresar los datos (opcion 1).")
            else:
                print("Suma de los numeros pares:", sumar_pares(lista_numeros))

        case "4":
            if datos_cargados == False:
                print("ERROR, primero debe ingresar los datos (opcion 1).")
            else:
                resultado = mayor_impar(lista_numeros)
                if resultado == None:
                    print("No hay numeros impares en la lista.")
                else:
                    print("El mayor numero impar es:", resultado)

        case "5":
            if datos_cargados == False:
                print("ERROR, primero debe ingresar los datos (opcion 1).")
            else:
                print("Numeros ingresados:", end=" ")
                listar_elementos(lista_numeros)

        case "6":
            if datos_cargados == False:
                print("ERROR, primero debe ingresar los datos (opcion 1).")
            else:
                print("Numeros pares:", end=" ")
                listar_pares(lista_numeros)

        case "7":
            if datos_cargados == False:
                print("ERROR, primero debe ingresar los datos (opcion 1).")
            else:
                print("Numeros en posiciones impares:", end=" ")
                listar_posiciones_impares(lista_numeros)

        case "8":
            print("Programa terminado.")
            break

        case _:
            print("Opcion Incorrecta")