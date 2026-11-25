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
