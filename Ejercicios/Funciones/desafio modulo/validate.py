def validate_number(texto: str, minimo: float, maximo: float, es_entero: bool = True) -> bool:
    """
    Valida que un texto represente un numero (entero o flotante) dentro de un rango.
    Parametros:
        - texto (str): el dato ingresado por el usuario.
        - minimo (float): valor minimo admitido (inclusive).
        - maximo (float): valor maximo admitido (inclusive).
        - es_entero (bool): True valida un entero, False valida un flotante. True por defecto.
    Return:
        - bool: True si el texto es un numero valido dentro del rango, False en caso contrario.
    """
    es_valido = len(texto) > 0
    inicio = 0
    if es_valido and texto[0] == "-":
        inicio = 1
    cant_puntos = 0
    cant_digitos = 0
    for i in range(inicio, len(texto)):
        if texto[i] == "." and es_entero == False:
            cant_puntos += 1
        elif texto[i] >= "0" and texto[i] <= "9":
            cant_digitos += 1
        else:
            es_valido = False
            break
    if cant_puntos > 1 or cant_digitos == 0:
        es_valido = False

    if es_valido:
        if es_entero:
            numero = int(texto)
        else:
            numero = float(texto)
        if numero < minimo or numero > maximo:
            es_valido = False
    return es_valido


def validate_length(cadena: str, longitud: int) -> bool:
    """
    Valida que una cadena no este vacia y no supere la longitud maxima.
    Parametros:
        - cadena (str): la cadena ingresada por el usuario.
        - longitud (int): cantidad maxima de caracteres admitida (inclusive).
    Return:
        - bool: True si 1 <= len(cadena) <= longitud, False en caso contrario.
    """
    es_valido = len(cadena) > 0 and len(cadena) <= longitud
    return es_valido