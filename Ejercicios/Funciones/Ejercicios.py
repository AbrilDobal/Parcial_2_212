
# 1. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def solicitar_entero(mensaje: str) -> int:
    """
    Solicita al usuario un numero entero por consola.
    Parametros:
        - mensaje (str): el texto que se le muestra al usuario.
    Return:
        - int: el numero ingresado.
    """
    numero = int(input(mensaje))
    return numero


entero = solicitar_entero("Ingrese un numero entero: ")
print(entero)

# 2. Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def  solicitar_flotante(mensaje: str) -> float:
    """
    Solicita al usuario un numero flotante por consola.
    Parametros:
        - mensaje (str): el texto que se le muestra al usuario.
    Return:
        - float: el numero ingresado.
    """
    numero = float(input(mensaje))
    return numero
 
 
flotante = solicitar_flotante("Ingrese un numero flotante: ")
print(flotante)

# 3. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def solicitar_cadena(mensaje: str) -> str:
    """
    Solicita al usuario una cadena por consola.
    Parametros:
        - mensaje (str): el texto que se le muestra al usuario.
    Return:
        - str: la cadena ingresada.
    """
    cadena = input(mensaje)
    return cadena


texto = solicitar_cadena("Ingrese una cadena: ")
print(texto)

# 4. Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

def calcular_area_rectangulo(base: float, altura: float) -> float:
    """
    Calcula el area de un rectangulo.
    Parametros:
        - base (float): la base del rectangulo.
        - altura (float): la altura del rectangulo.
    Return:
        - float: el area del rectangulo.
    """
    area = base * altura
    return area

print("Area rectangulo 4x5:", calcular_area_rectangulo(4, 5))


# 5. Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
# preguntar 
def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el area de un circulo.
    Parametros:
        - radio (float): el radio del circulo
    Return:
        - float: el area del circulo.
    """
    area = 3.14159 * radio ** 2
    return area

print("Area circulo radio 3:", calcular_area_circulo(3))

# 6. Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def verificar_par_impar(numero: int) -> None:
    """
    Verifica si un numero es par o impar e imprime el resultado por consola.
    Parametros:
        - numero (int): el numero a verificar.
    Return:
        None
    """
    if numero % 2 == 0:
        print(f"El numero {numero} es PAR.")
    else:
        print(f"El numero {numero} es IMPAR.")

verificar_par_impar(7)
verificar_par_impar(10)

# 7. Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def es_par(numero: int) -> bool:
    """
    Determina si un numero es par.
    Parametros:
        - numero (int): el numero a evaluar.
    Return:
        - bool: True si el numero es par, False en caso contrario.
    """
    resultado = numero % 2 == 0
    return resultado
 
print(es_par(10))   # True
print(es_par(7))    # False
 

# 8. Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def encontrar_maximo_tres(num_a: float, num_b: float, num_c: float) -> float:
    """
    Encuentra el mayor de tres numeros.
    Parametros:
        - num_a (float): primer numero.
        - num_b (float): segundo numero.
        - num_c (float): tercer numero.
    Return:
        - float: el numero mas grande.
    """
    maximo = num_a
    if num_b > maximo:
        maximo = num_b
    if num_c > maximo:
        maximo = num_c
    return maximo


print(encontrar_maximo_tres(3, 9, 5))      # 9
print(encontrar_maximo_tres(-1, -8, -3))   # -1
print(encontrar_maximo_tres(4, 4, 4))      # 4

# 9. Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def calcular_potencia(base: float, exponente: int) -> float:
    """
    Calcula la potencia de un numero.
    Parametros:
        - base (float): la base.
        - exponente (int): el exponente.
    Return:
        - float: la base elevada al exponente.
    """
    resultado = base ** exponente
    return resultado


print(calcular_potencia(2, 10))   # 1024
print(calcular_potencia(5, 0))    # 1
print(calcular_potencia(2, -2))   # 0.25

# 10. Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def es_primo(numero: int) -> bool:
    """
    Determina si un numero es primo.
    Parametros:
        - numero (int): el numero a evaluar.
    Return:
        - bool: True si el numero es primo, False en caso contrario.
    """
    if numero < 2:
        es_primo_resultado = False
    else:
        es_primo_resultado = True  # bandera
        for divisor in range(2, numero):
            if numero % divisor == 0:
                es_primo_resultado = False
                break  # ya encontramos un divisor, no hace falta seguir
 
    return es_primo_resultado

print(es_primo(13))   # True
print(es_primo(15))   # False
print(es_primo(2))    # True
print(es_primo(1))    # False
print(es_primo(-7))   # False


# 11. Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

def verificar_es_primo(numero: int) -> bool:
    """
    Verifica si un numero es primo.
    Parametros:
        - numero (int): el numero a evaluar.
    Return:
        - bool: True si es primo, False en caso contrario.
    """
    es_primo = numero > 1
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
            break
    return es_primo


def mostrar_primos_hasta(limite: int) -> int:
    """
    Muestra todos los numeros primos entre 1 y el limite (inclusive).
    Parametros:
        - limite (int): el numero hasta el cual se buscan primos.
    Return:
        - int: la cantidad de primos encontrados.
    """
    cantidad_primos = 0
    for numero in range(2, limite + 1):
        if verificar_es_primo(numero):
            print(numero)
            cantidad_primos += 1
    return cantidad_primos


cantidad = mostrar_primos_hasta(20)   # 2 3 5 7 11 13 17 19
print("Cantidad de primos:", cantidad)  # 8

# 12. Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.


def mostrar_tabla_multiplicar(numero: int, inicio: int = 1, fin: int = 10) -> None:
    """
    Imprime la tabla de multiplicar de un numero.
    Parametros:
        - numero (int): el numero de la tabla.
        - inicio (int): primer multiplicador (incluido). 1 por defecto.
        - fin (int): ultimo multiplicador (incluido). 10 por defecto.
    Return:
        None
    """
    for multiplicador in range(inicio, fin + 1):
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")


mostrar_tabla_multiplicar(7)
print("==========")
mostrar_tabla_multiplicar(7, 5, 8)
print("==========")
mostrar_tabla_multiplicar(3, fin=4)

# 13. Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

# 13. Funciones de los puntos 1, 2 y 3 especializadas, reutilizables y con validaciones.

def verificar_es_entero(texto: str) -> bool:
    """
    Verifica que un texto represente un numero entero (con signo "-" opcional).
    Parametros:
        - texto (str): el texto a evaluar.
    Return:
        - bool: True si representa un entero valido, False en caso contrario.
    """
    es_valido = len(texto) > 0
    inicio = 0
    if es_valido and texto[0] == "-":
        inicio = 1
        es_valido = len(texto) > 1
    for i in range(inicio, len(texto)):
        if texto[i] < "0" or texto[i] > "9":
            es_valido = False
            break
    return es_valido


def verificar_es_flotante(texto: str) -> bool:
    """
    Verifica que un texto represente un flotante (signo "-" opcional, un solo punto).
    Parametros:
        - texto (str): el texto a evaluar.
    Return:
        - bool: True si representa un flotante valido, False en caso contrario.
    """
    es_valido = len(texto) > 0
    inicio = 0
    if es_valido and texto[0] == "-":
        inicio = 1
    cant_puntos = 0
    cant_digitos = 0
    for i in range(inicio, len(texto)):
        if texto[i] == ".":
            cant_puntos += 1
        elif texto[i] >= "0" and texto[i] <= "9":
            cant_digitos += 1
        else:
            es_valido = False
            break
    if cant_puntos > 1 or cant_digitos == 0:
        es_valido = False
    return es_valido


def solicitar_entero_validado(mensaje: str, mensaje_error: str = "ERROR, ingrese un entero valido.",
                              minimo=None, maximo=None) -> int:
    """
    Solicita un entero y lo revalida hasta que sea correcto (formato y rango opcional).
    Parametros:
        - mensaje (str): texto que se le muestra al usuario.
        - mensaje_error (str): texto que se muestra ante un dato invalido.
        - minimo (int): valor minimo permitido (incluido). None = sin limite.
        - maximo (int): valor maximo permitido (incluido). None = sin limite.
    Return:
        - int: el entero validado.
    """
    es_valido = False
    numero = 0
    while es_valido == False:
        texto = input(mensaje)
        if verificar_es_entero(texto):
            numero = int(texto)
            es_valido = True
            if minimo != None and numero < minimo:
                es_valido = False
            if maximo != None and numero > maximo:
                es_valido = False
        if es_valido == False:
            print(mensaje_error)
    return numero


def solicitar_flotante_validado(mensaje: str, mensaje_error: str = "ERROR, ingrese un flotante valido.",
                                minimo=None, maximo=None) -> float:
    """
    Solicita un flotante y lo revalida hasta que sea correcto (formato y rango opcional).
    Parametros:
        - mensaje (str): texto que se le muestra al usuario.
        - mensaje_error (str): texto que se muestra ante un dato invalido.
        - minimo (float): valor minimo permitido (incluido). None = sin limite.
        - maximo (float): valor maximo permitido (incluido). None = sin limite.
    Return:\n
        - float: el flotante validado.
    """
    es_valido = False
    numero = 0.0
    while es_valido == False:
        texto = input(mensaje)
        if verificar_es_flotante(texto):
            numero = float(texto)
            es_valido = True
            if minimo != None and numero < minimo:
                es_valido = False
            if maximo != None and numero > maximo:
                es_valido = False
        if es_valido == False:
            print(mensaje_error)
    return numero


def solicitar_cadena_validada(mensaje: str, mensaje_error: str = "ERROR, largo de cadena invalido.",
                              largo_minimo: int = 1, largo_maximo=None) -> str:
    """
    Solicita una cadena y la revalida hasta que su largo sea correcto.
    Parametros:
        - mensaje (str): texto que se le muestra al usuario.
        - mensaje_error (str): texto que se muestra ante un dato invalido.
        - largo_minimo (int): largo minimo permitido. 1 por defecto (no vacia).
        - largo_maximo (int): largo maximo permitido. None = sin limite.
    Return:\n
        - str: la cadena validada.
    """
    cadena = input(mensaje)
    while len(cadena) < largo_minimo or (largo_maximo != None and len(cadena) > largo_maximo):
        print(mensaje_error)
        cadena = input(mensaje)
    return cadena


edad = solicitar_entero_validado("Ingrese su edad (18-120): ", "ERROR, edad invalida.", 18, 120)
altura = solicitar_flotante_validado("Ingrese su altura en metros (0.5-2.5): ", "ERROR, altura invalida.", 0.5, 2.5)
nombre = solicitar_cadena_validada("Ingrese su nombre (1-20 letras): ", "ERROR, largo invalido.", 1, 20)
print(edad, altura, nombre)