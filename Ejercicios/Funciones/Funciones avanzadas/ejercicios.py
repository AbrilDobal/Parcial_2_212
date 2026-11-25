#Funciones auxiliares
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
 
 
def verificar_solo_letras(texto: str) -> bool:
    """
    Verifica que todos los caracteres de un texto sean letras (el texto no puede ser vacio).
    Parametros:
        - texto (str): el texto a evaluar.
    Return:
        - bool: True si todos los caracteres son letras, False en caso contrario.
    """
    son_letras = medir_largo_cadena(texto) > 0
    for i in range(medir_largo_cadena(texto)):
        if verificar_es_letra(texto[i]) == False:
            son_letras = False
            break
    return son_letras
 
 
def verificar_solo_digitos(texto: str) -> bool:
    """
    Verifica que todos los caracteres de un texto sean digitos (el texto no puede ser vacio).
    Parametros:
        - texto (str): el texto a evaluar.
    Return:
        - bool: True si todos los caracteres son digitos, False en caso contrario.
    """
    son_digitos = medir_largo_cadena(texto) > 0
    for i in range(medir_largo_cadena(texto)):
        if verificar_es_digito(texto[i]) == False:
            son_digitos = False
            break
    return son_digitos
 
 
def verificar_dni(dni: str) -> bool:
    """
    Verifica la cantidad de caracteres de un DNI.
    Parametros:
        - dni (str): el DNI a verificar.
    Return:
        - bool: True si tiene entre 6 y 8 caracteres, False en caso contrario.
    """
    largo = medir_largo_cadena(dni)
    es_valido = largo >= 6 and largo <= 8
    return es_valido
 
 
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

# 1) Desarrollar una función que reciba como parámetros fecha actual y fecha de nacimiento; y retorne la edad.
def obtener_partes_fecha(fecha: str) -> list:
    """
    Separa una fecha con formato "dd/mm/aaaa" en dia, mes y anio.
    Parametros:
        - fecha (str): la fecha, con formato "dd/mm/aaaa".
    Return:
        - list: [dia, mes, anio], los tres como enteros.
    """
    dia = int(fecha[0:2])
    mes = int(fecha[3:5])
    anio = int(fecha[6:10])
    partes = [dia, mes, anio]
    return partes
 
 
def calcular_edad(fecha_actual: str, fecha_nacimiento: str) -> int:
    """
    Calcula la edad en anios cumplidos.
    Parametros:
        - fecha_actual (str): la fecha de hoy, con formato "dd/mm/aaaa".
        - fecha_nacimiento (str): la fecha de nacimiento, con formato "dd/mm/aaaa".
    Return:
        - int: la edad. Si la fecha de nacimiento es posterior a la actual devuelve None.
    """
    actual = obtener_partes_fecha(fecha_actual)
    nacimiento = obtener_partes_fecha(fecha_nacimiento)
 
    edad = actual[2] - nacimiento[2]
    # Si todavia no cumplio anios este anio, se resta uno.
    if actual[1] < nacimiento[1] or (actual[1] == nacimiento[1] and actual[0] < nacimiento[0]):
        edad -= 1
    if edad < 0:
        edad = None
    return edad

# 2) Desarrollar una función que reciba una patente que tendrá tres letras y tres números o tres números y tres
# letras. Deberá retornar auto o moto, si la patente es tres letras y tres números o tres números y tres letras
# respectivamente.
def identificar_tipo_vehiculo(patente: str) -> str:
    """
    Identifica si una patente corresponde a un auto o a una moto.
    Parametros:
        - patente (str): la patente, de 6 caracteres.
    Return:
        - str: "auto" si son 3 letras y 3 numeros, "moto" si son 3 numeros y 3 letras.
          Devuelve None si la patente no tiene ninguno de los dos formatos.
    """
    tipo = None
    if medir_largo_cadena(patente) == 6:
        if verificar_solo_letras(patente[0:3]) and verificar_solo_digitos(patente[3:6]):
            tipo = "auto"
        elif verificar_solo_digitos(patente[0:3]) and verificar_solo_letras(patente[3:6]):
            tipo = "moto"
    return tipo


# 3) Desarrollar una función que reciba como parametros numero de DNI y
# [MASCULINO|FEMENINO|EMPRESA]. Deberá retornar el CUIL/CUIT formado por:
# CUIL/T: Son 11 números en total:
# XY–12345678– Z
# XY: Indican el tipo (Masculino, Femenino o una empresa)
# 12345678: Número de DNI
# Z: Código Verificador
# Algoritmo: Se determina XY con las siguientes reglas:
# Masculino: 20
# Femenio: 27
# Empresa: 30
# Se multiplica XY 12345678 por un número de forma separada:
# X*5
# Y *4
# 1 * 3
# 2 * 2
# 3 * 7
# 4 *6
# 5 * 5
# 6 *4
# 7 * 3
# 8*2
# Se suman dichos resultados. El resultado obtenido se divide por 11. De esa división se obtiene un Resto que
# determina Z.
# Si el resto es 0 = Entonces Z = 0.
# Si el resto es 1 = Entonces se aplica la siguiente regla:
# *Si es hombre: Z = 9 y XY pasa a ser 23
# *Si es mujer: Z = 4 y XY pasa a ser 23
# Caso contrario Z pasa a ser (11- Resto).
# 2
def obtener_prefijo_tipo(tipo: str) -> int:
    """
    Obtiene el prefijo XY segun el tipo de persona.
    Parametros:
        - tipo (str): "MASCULINO", "FEMENINO" o "EMPRESA".
    Return:
        - int: 20 (masculino), 27 (femenino) o 30 (empresa). None si el tipo no es valido.
    """
    prefijo = None
    if tipo == "MASCULINO":
        prefijo = 20
    elif tipo == "FEMENINO":
        prefijo = 27
    elif tipo == "EMPRESA":
        prefijo = 30
    return prefijo
 
 
def calcular_suma_ponderada(digitos: str) -> int:
    """
    Multiplica cada uno de los 10 digitos (XY + DNI de 8) por su factor y suma los resultados.
    Factores: 5, 4, 3, 2, 7, 6, 5, 4, 3, 2.
    Parametros:
        - digitos (str): cadena de 10 digitos (prefijo + DNI completo).
    Return:
        - int: la suma de los productos.
    """
    factores = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    suma = 0
    for i in range(10):
        suma += int(digitos[i]) * factores[i]
    return suma
 
 
def generar_cuil_cuit(dni: str, tipo: str) -> str:
    """
    Genera el CUIL/CUIT con formato "XY-DNI-Z".
    Parametros:
        - dni (str): el DNI (solo digitos, de 6 a 8 caracteres). Se completa con ceros a 8.
        - tipo (str): "MASCULINO", "FEMENINO" o "EMPRESA".
    Return:
        - str: el CUIL/CUIT. Ej: ("12345678", "MASCULINO") -> "20-12345678-6".
          Devuelve None si el DNI o el tipo no son validos.
    """
    resultado = None
    prefijo = obtener_prefijo_tipo(tipo)
    dni_es_valido = verificar_solo_digitos(dni) and verificar_dni(dni)
 
    if prefijo != None and dni_es_valido:
        dni_completo = completar_dni(dni)
        suma = calcular_suma_ponderada(str(prefijo) + dni_completo)
        resto = suma % 11
 
        if resto == 0:
            verificador = 0
        elif resto == 1:
            if tipo == "EMPRESA":
                prefijo = 33
                verificador = 3
            elif tipo == "MASCULINO":
                prefijo = 23
                verificador = 9
            else:
                prefijo = 23
                verificador = 4
        else:
            verificador = 11 - resto
 
        resultado = f"{prefijo}-{dni_completo}-{verificador}"
    return resultado
 
