# 1) Desarrollar una función que determine si un número entero es par o impar. Debe recibir un número por
# parámetro y devolver True en caso de que sea par, de lo contrario devolverá False.

def verificar_es_par(numero: int) -> bool:
    """
    Determina si un numero entero es par.
    Parametros:
        - numero (int): el numero a evaluar.
    Return:
        - bool: True si es par, False en caso contrario.
    """
    es_par = numero % 2 == 0
    return es_par

# 2) Desarrollar una función que reciba un carácter y determine si ese carácter está comprendido entre a…z o
# A…Z, en caso afirmativo devolverá True, de lo contrario False.

def verificar_es_letra(caracter: str) -> bool:
    """
    Determina si un caracter esta comprendido entre a...z o A...Z.
    Parametros:
        - caracter (str): el caracter a evaluar.
    Return:
        - bool: True si es una letra (sin ñ ni acentos), False en caso contrario.
    """
    es_letra = (caracter >= "a" and caracter <= "z") or (caracter >= "A" and caracter <= "Z")
    return es_letra


# 3) Desarrollar una función que reciba un carácter y determine si ese carácter está comprendido entre 0…9,
# devolverá un valor boolean indicando si el carácter recibido es numérico o no.

def verificar_es_digito(caracter: str) -> bool:
    """
    Determina si un caracter esta comprendido entre 0...9.
    Parametros:
        - caracter (str): el caracter a evaluar.
    Return:
        - bool: True si es numerico, False en caso contrario.
    """
    es_digito = caracter >= "0" and caracter <= "9"
    return es_digito


#4) Desarrollar una función que permita validar un número entero. Deberá recibir por parámetro el número a
# validar, y dos números que representan el rango mínimo y máximo permitido. Devolverá True en caso de
# ser válido, False de lo contrario.

def validar_numero_entero(numero: int, minimo: int, maximo: int) -> bool:
    """
    Valida que un numero entero este dentro de un rango (inclusive).
    Parametros:
        - numero (int): el numero a validar.
        - minimo (int): valor minimo permitido.
        - maximo (int): valor maximo permitido.
    Return:
        - bool: True si minimo <= numero <= maximo, False en caso contrario.
    """
    es_valido = numero >= minimo and numero <= maximo
    return es_valido


#7) Desarrollar una función que se encargue de medir el largo de una cadena de caracteres, deberá recibir por
# parámetro la cadena de caracteres a evaluar y devolverá un número entero representando la longitud de
# la cadena recibida.
# (Va antes porque otras funciones la reutilizan.)

def medir_largo_cadena(cadena: str) -> int:
    """
    Mide el largo de una cadena de caracteres.
    Parametros:
        - cadena (str): la cadena a evaluar.
    Return:
        - int: la cantidad de caracteres de la cadena.
    """
    largo = len(cadena)
    return largo


#5) Desarrollar una función que se encargue de solicitar un número entero al usuario, validarlo (reutilizando la
# función del punto anterior) y retornar el número validado y transformado a entero. Deberá recibir por
# parámetro un mensaje que se le mostrará al usuario y los rangos de validación.

def verificar_es_cadena_entera(texto: str) -> bool:
    """
    Verifica que un texto represente un entero (signo "-" opcional), para poder convertirlo sin errores.
    Parametros:
        - texto (str): el texto a evaluar.
    Return:
        - bool: True si se puede convertir a int, False en caso contrario.
    """
    largo = medir_largo_cadena(texto)
    inicio = 0
    if largo > 0 and texto[0] == "-":
        inicio = 1
    es_entera = largo > inicio
    for i in range(inicio, largo):
        if verificar_es_digito(texto[i]) == False:
            es_entera = False
            break
    return es_entera


def solicitar_entero_validado(mensaje: str, minimo: int, maximo: int) -> int:
    """
    Solicita un entero al usuario, lo valida (formato y rango) y lo retorna como int.
    Parametros:
        - mensaje (str): mensaje que se le muestra al usuario.
        - minimo (int): valor minimo permitido.
        - maximo (int): valor maximo permitido.
    Return:
        - int: el numero validado.
    """
    es_valido = False
    numero = 0
    while es_valido == False:
        texto = input(mensaje)
        if verificar_es_cadena_entera(texto):
            numero = int(texto)
            es_valido = validar_numero_entero(numero, minimo, maximo)
        if es_valido == False:
            print(f"ERROR, ingrese un entero entre {minimo} y {maximo}.")
    return numero


#6) Desarrollar una función que se encargue de solicitar una cadena de caracteres al usuario, validarla y
# retornar la misma. Deberá recibir como parámetro un mensaje para indicarle al usuario y 1, 2 o 3 cadenas
# de caracteres que representarán las opciones válidas de ingreso.

def solicitar_opcion(mensaje: str, opcion_uno: str, opcion_dos: str = None, opcion_tres: str = None) -> str:
    """
    Solicita una cadena al usuario y la valida contra 1, 2 o 3 opciones validas.
    Distingue mayusculas de minusculas.
    Parametros:
        - mensaje (str): mensaje que se le muestra al usuario.
        - opcion_uno (str): primera opcion valida (obligatoria).
        - opcion_dos (str): segunda opcion valida (opcional).
        - opcion_tres (str): tercera opcion valida (opcional).
    Return:
        - str: la cadena ingresada, que coincide con alguna opcion valida.
    """
    cadena = input(mensaje)
    while cadena != opcion_uno and cadena != opcion_dos and cadena != opcion_tres:
        print("ERROR, opcion invalida.")
        cadena = input(mensaje)
    return cadena


# 8) Desarrollar una función que determine si un número que recibirá por parámetro es primo. Si es primo
# deberá devolver un True, de lo contrario False.

def verificar_es_primo(numero: int) -> bool:
    """
    Determina si un numero es primo.
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


#9) Desarrollar una función que recibirá un número entero por parámetro, y devolverá el resultado del
# factorial de ese número.

def calcular_factorial(numero: int) -> int:
    """
    Calcula el factorial de un numero entero.
    Parametros:
        - numero (int): el numero del que se calcula el factorial.
    Return:
        - int: el factorial (0! = 1). Si el numero es negativo devuelve None.
    """
    if numero < 0:
        resultado = None
    else:
        resultado = 1
        for multiplicador in range(1, numero + 1):
            resultado *= multiplicador
    return resultado


#10) Desarrollar una función que verifique el DNI de una persona, la misma recibirá una cadena de caracteres
# (se asume que solamente contiene caracteres numéricos). Si la cantidad de caracteres es menor a 6 o
# mayor a 8, retornara False. Si la cantidad de caracteres está comprendida entre 6 y 8 devolverá True.

def verificar_dni(dni: str) -> bool:
    """
    Verifica la cantidad de caracteres de un DNI (se asume que solo tiene digitos).
    Parametros:
        - dni (str): el DNI a verificar.
    Return:
        - bool: True si tiene entre 6 y 8 caracteres, False en caso contrario.
    """
    largo = medir_largo_cadena(dni)
    es_valido = largo >= 6 and largo <= 8
    return es_valido


#11) Desarrollar una función que complete el número de DNI de una persona. Recibirá una cadena de
# caracteres (se asume que solamente contiene caracteres numéricos), deberá medirla y completar con ceros
# a la izquierda hasta llegar a un total de 8 caracteres, y devolviendo la cadena resultante. Ej: Se ingresa
# “123456”, y devolverá “00123456”.

def completar_dni(dni: str) -> str:
    """
    Completa un DNI con ceros a la izquierda hasta llegar a 8 caracteres.
    Parametros:
        - dni (str): el DNI a completar (solo digitos).
    Return:
        - str: el DNI de 8 caracteres. Ej: "123456" -> "00123456".
    """
    ceros_faltantes = 8 - medir_largo_cadena(dni)
    dni_completo = ("0" * ceros_faltantes) + dni
    return dni_completo


#12) Desarrollar una función que transforme una cadena de caracteres numérica a su equivalente en letras.
# Recibirá por parámetro la cadena a transformar y devolverá el resultado en letras. Ej: “987”->
# "novecientos ochenta y siete". Como máximo tomar el número más grande de 3 dígitos.

def convertir_menor_cien_a_letras(numero: int) -> str:
    """
    Convierte un numero entre 0 y 99 a su equivalente en letras.
    Parametros:
        - numero (int): el numero a convertir (0 a 99).
    Return:
        - str: el numero en letras. Ej: 42 -> "cuarenta y dos".
    """
    unidades = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince",
                  "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    veintis = ["veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro",
               "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
    decenas = ["", "", "", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

    if numero < 10:
        texto = unidades[numero]
    elif numero < 20:
        texto = especiales[numero - 10]
    elif numero < 30:
        texto = veintis[numero - 20]
    else:
        texto = decenas[numero // 10]
        if numero % 10 != 0:
            texto = texto + " y " + unidades[numero % 10]
    return texto


def convertir_numero_a_letras(cadena: str) -> str:
    """
    Transforma una cadena numerica (hasta 3 digitos) a su equivalente en letras.
    Parametros:
        - cadena (str): la cadena numerica a transformar (maximo "999").
    Return:
        - str: el numero en letras. Ej: "987" -> "novecientos ochenta y siete".
          Devuelve None si la cadena esta vacia, tiene mas de 3 caracteres o algun caracter no es un digito.
    """
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos",
                "seiscientos", "setecientos", "ochocientos", "novecientos"]
    largo = medir_largo_cadena(cadena)
    es_valida = largo >= 1 and largo <= 3
    for i in range(largo):
        if verificar_es_digito(cadena[i]) == False:
            es_valida = False
            break

    if es_valida:
        numero = int(cadena)
        cientos = numero // 100
        resto = numero % 100
        if cientos == 0:
            texto = convertir_menor_cien_a_letras(resto)
        elif resto == 0:
            if cientos == 1:
                texto = "cien"
            else:
                texto = centenas[cientos]
        else:
            texto = centenas[cientos] + " " + convertir_menor_cien_a_letras(resto)
    else:
        texto = None
    return texto