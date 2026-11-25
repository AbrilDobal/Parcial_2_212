# Sucesión de Fibonacci.
# 1) Desarrollar función calcular_fibonacci.
# Parámetros: La misma recibirá un número entero (int) mayor o igual a cero (0).
# Funcionalidad: La función deberá calcular el número n-ésimo en la sucesión de Fibonacci.
# Si n = 0, deberá devolver 0.
# Si n = 1, deberá devolver 1.
# Para cualquier n > 1, el resultado será la suma de los dos números anteriores de la secuencia.
# Retorno: El resultado calculado previamente.
# Por ejemplo:
# ● f0=0
# ● f1=1
# ● f2=1
# ● f3=2
# ● f4=3
# ● f5=5
# ● f6=8
# ●
# 2) Desarrollar función mostrar_serie_fibonacci.
# Parámetros: La misma recibirá un número entero (int) mayor o igual a cero (0).
# Funcionalidad: La función deberá mostrar la secuencia completa hasta el número n-ésimo en la sucesión de
# Fibonacci, incluyendo a este último.
# Retorno: None
# Por ejemplo:
# 1 + 2=3
# 2 +3=5
def calcular_fibonacci(numero: int) -> int:
    """
    Calcula el numero n-esimo de la sucesion de Fibonacci.
    f0 = 0, f1 = 1 y, para n > 1, fn = f(n-1) + f(n-2).
    Parametros:
        - numero (int): la posicion n en la sucesion (mayor o igual a 0).
    Return:
        - int: el numero n-esimo de Fibonacci. Si numero es negativo devuelve None.
    """
    if numero < 0:
        resultado = None
    elif numero == 0 or numero == 1:
        resultado = numero
    else:
        anteultimo = 0
        ultimo = 1
        for _ in range(numero - 1):
            proximo = anteultimo + ultimo
            anteultimo = ultimo
            ultimo = proximo
        resultado = ultimo
    return resultado
 
 
def mostrar_serie_fibonacci(numero: int) -> None:
    """
    Muestra la sucesion de Fibonacci completa hasta el numero n-esimo (inclusive),
    indicando la suma que genera cada termino.
    Parametros:
        - numero (int): la posicion n hasta la cual se muestra la serie (mayor o igual a 0).
    Return:
        None
    """
    if numero < 0:
        print("ERROR, el numero debe ser mayor o igual a cero.")
    else:
        for i in range(numero + 1):
            if i < 2:
                print(f"f{i} = {calcular_fibonacci(i)}")
            else:
                anterior_dos = calcular_fibonacci(i - 2)
                anterior_uno = calcular_fibonacci(i - 1)
                print(f"f{i} = {anterior_dos} + {anterior_uno} = {anterior_dos + anterior_uno}")
 
        print("Serie completa:", end=" ")
        for i in range(numero + 1):
            print(calcular_fibonacci(i), end=" ")
        print()
 

# Sumadenúmeros consecutivos.
# 1) Desarrollar función determinar_suma_consecutiva.
# Parámetros: La misma recibirá un número entero (int), y cualquier otro parámetro que considere necesario.
# Funcionalidad: Deberá determinar si el número ingresado como parámetro se puede obtener con la suma
# de dos (2) números consecutivos anteriores.
# Retorno:
# True si el número se puede obtener de la suma de números consecutivos anteriores.
# False si el número NO se obtiene de la suma de números consecutivos anteriores

def determinar_suma_consecutiva(numero: int, inicio: int = 1) -> bool:
    """
    Determina si un numero se obtiene sumando dos numeros consecutivos anteriores a el.
    Ej: 3 = 1 + 2, 5 = 2 + 3.
    Parametros:
        - numero (int): el numero a evaluar.
        - inicio (int): el menor numero permitido para la suma. 1 por defecto
          (con 0, el 1 tambien se obtiene: 0 + 1).
    Return:
        - bool: True si numero = base + (base + 1) para alguna base anterior, False en caso contrario.
    """
    es_suma_consecutiva = False
    for base in range(inicio, numero):
        if base + (base + 1) == numero:
            es_suma_consecutiva = True
            break
    return es_suma_consecutiva