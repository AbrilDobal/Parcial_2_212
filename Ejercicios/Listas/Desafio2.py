def contiene(lista: list, elemento) -> bool:
    """
    Determina si un elemento se encuentra dentro de una lista.
    Parametros:
        - lista (list): la lista donde buscar.
        - elemento: el elemento a buscar.
    Return:
        - bool: True si el elemento esta en la lista, False caso contrario.  
    """
    encontrado = False
    for i in range(len(lista)):
        if lista[i] == elemento:
            encontrado = True
    return encontrado


def producto_en_todas(listas: list, producto) -> bool:
    """
    Determina si un producto esta presente en todas las listas de una coleccion de listas.
    Parametros:
        - listas (list): lista de listas de productos (una por usuario).
        - producto: el producto a buscar.
    Return:
        - bool: True si el producto esta en todas las listas, False caso contrario.
    """
    esta_en_todas = True
    for i in range(len(listas)):
        if not contiene(listas[i], producto):
            esta_en_todas = False
    return esta_en_todas


def producto_solo_en(listas: list, indice_propio: int, producto) -> bool:
    """
    Determina si un producto solo aparece en la lista propia y en ninguna otra.
    Parametros:
        - listas (list): lista de listas de productos (una por usuario).
        - indice_propio (int): indice del usuario que se esta analizando.
        - producto: el producto a evaluar.
    Return:
        - bool: True si el producto no aparece en ninguna otra lista, False caso contrario.
    """
    es_exclusivo = True
    for i in range(len(listas)):
        if i != indice_propio and contiene(listas[i], producto):
            es_exclusivo = False
    return es_exclusivo


def productos_comunes_todos(listas: list) -> list:
    """
    Determina los productos que aparecen en TODAS las listas, sin repetir.
    Parametros:
        - listas (list): lista de listas de productos (una por usuario).
    Return:
        - list: productos comprados por todos los usuarios.
    """
    comunes = []
    for i in range(len(listas[0])):
        producto = listas[0][i]
        if producto_en_todas(listas, producto) and not contiene(comunes, producto):
            comunes += [producto]
    return comunes


def productos_exclusivos_de(listas: list, indice_propio: int) -> list:
    """
    Determina los productos que un usuario compro y ningun otro, sin repetir.
    Parametros:
        - listas (list): lista de listas de productos (una por usuario).
        - indice_propio (int): indice del usuario a analizar.
    Return:
        - list: productos exclusivos de ese usuario.
    """
    exclusivos = []
    for i in range(len(listas[indice_propio])):
        producto = listas[indice_propio][i]
        if producto_solo_en(listas, indice_propio, producto) and not contiene(exclusivos, producto):
            exclusivos += [producto]
    return exclusivos


def catalogo_total_de_todos(listas: list) -> list:
    """
    Determina el conjunto total de productos comprados entre todos los usuarios, sin repetir.
    Parametros:
        - listas (list): lista de listas de productos (una por usuario).
    Return:
        - list: catalogo con todos los productos, sin duplicados.
    """
    catalogo = []
    for i in range(len(listas)):
        for j in range(len(listas[i])):
            producto = listas[i][j]
            if not contiene(catalogo, producto):
                catalogo += [producto]
    return catalogo


def recomendaciones_para(listas: list, indice_propio: int) -> list:
    """
    Determina que productos comprados por otros usuarios podrian recomendarse a un usuario,
    por no haberlos comprado todavia.
    Parametros:
        - listas (list): lista de listas de productos (una por usuario).
        - indice_propio (int): indice del usuario al que se le va a recomendar.
    Return:
        - list: productos recomendados para ese usuario.
    """
    recomendaciones = []
    for i in range(len(listas)):
        if i != indice_propio:
            for j in range(len(listas[i])):
                producto = listas[i][j]
                if not contiene(listas[indice_propio], producto) and not contiene(recomendaciones, producto):
                    recomendaciones += [producto]
    return recomendaciones


def mostrar_lista(lista: list, titulo: str) -> None:
    """
    Muestra por pantalla los elementos de una lista con un titulo, uno por linea.
    Parametros:
        - lista (list): la lista a mostrar.
        - titulo (str): el encabezado a imprimir antes de la lista.
    Return:
        None
    """
    print(titulo)
    if len(lista) == 0:
        print(" (ninguno) ")
    else:
        for i in range(len(lista)):
            print("  -", lista[i])


def ingresar_cantidad(mensaje: str, minimo: int) -> int:
    """
    Solicita al usuario un numero entero, validando que sea mayor o igual a un minimo.
    Parametros:
        - mensaje (str): el texto a mostrar al pedir el dato.
        - minimo (int): el valor minimo aceptado.
    Return:
        - int: el numero ingresado, valido.
    """
    cantidad = int(input(mensaje))
    while cantidad < minimo:
        cantidad = int(input(f"ERROR, debe ingresar un numero mayor o igual a {minimo}. Reingrese: "))
    return cantidad


def ingresar_lista_productos(nombre_usuario: str) -> list:
    """
    Solicita al usuario el historial de compras de un usuario en particular.
    Parametros:
        - nombre_usuario (str): el nombre del usuario a mostrar en los mensajes.
    Return:
        - list: la lista de productos ingresados.
    """
    cantidad_productos = ingresar_cantidad(f"Cuantos productos compro {nombre_usuario}?: ", 1)
    lista = []
    for i in range(cantidad_productos):
        producto = input(f"Ingrese el producto {i + 1} de {nombre_usuario}: ")
        lista += [producto]
    return lista


def cargar_listas_predefinidas() -> list:
    """
    Devuelve un conjunto predefinido de nombres e historiales de compra de 2 usuarios.
    Parametros:
        None
    Return:
        - list: [nombres_usuarios, listas_productos]
    """
    nombres_usuarios = ["Usuario 1", "Usuario 2"]
    listas_productos = [
        ["Zapatillas", "Mochila", "Auriculares", "Notebook", "Remera"],
        ["Mochila", "Auriculares", "Celular", "Remera", "Cargador"],
    ]
    resultado = [nombres_usuarios, listas_productos]
    return resultado


def cargar_listas_manual() -> list:
    """
    Solicita por teclado la cantidad de usuarios (minimo 2) y el historial de compras de cada uno.
    Parametros:
        None
    Return:
        - list: [nombres_usuarios, listas_productos]
    """
    cantidad_usuarios = ingresar_cantidad("Cuantos usuarios va a cargar? (minimo 2): ", 2)

    nombres_usuarios = []
    listas_productos = []
    for i in range(cantidad_usuarios):
        nombre = input(f"Ingrese el nombre del usuario {i + 1}: ")
        nombres_usuarios += [nombre]

        lista = ingresar_lista_productos(nombre)
        listas_productos += [lista]

    resultado = [nombres_usuarios, listas_productos]
    return resultado


# ===== Programa principal =====

nombres_usuarios = []
listas_productos = []
datos_cargados = False

menu = """
 == RECOMENDACION DE PRODUCTOS ==
1) Cargar listas predefinidas
2) Cargar listas manualmente
3) Ver productos en comun (entre todos)
4) Ver productos exclusivos por usuario
5) Ver catalogo total
6) Ver recomendaciones por usuario
7) Salir

Seleccione una opcion: """

while True:
    opcion = input(menu)

    match opcion:
        case "1":
            datos = cargar_listas_predefinidas()
            nombres_usuarios = datos[0]
            listas_productos = datos[1]
            datos_cargados = True
            print("Listas predefinidas cargadas.")

        case "2":
            datos = cargar_listas_manual()
            nombres_usuarios = datos[0]
            listas_productos = datos[1]
            datos_cargados = True
            print("Listas cargadas correctamente.")

        case "3":
            if datos_cargados == False:
                print("ERROR, primero debe cargar las listas (opcion 1 o 2).")
            else:
                comunes = productos_comunes_todos(listas_productos)
                mostrar_lista(comunes, "Productos en comun entre todos los usuarios:")

        case "4":
            if datos_cargados == False:
                print("ERROR, primero debe cargar las listas (opcion 1 o 2).")
            else:
                for i in range(len(listas_productos)):
                    exclusivos = productos_exclusivos_de(listas_productos, i)
                    mostrar_lista(exclusivos, f"Productos exclusivos de {nombres_usuarios[i]}:")
                    print()

        case "5":
            if datos_cargados == False:
                print("ERROR, primero debe cargar las listas (opcion 1 o 2).")
            else:
                catalogo = catalogo_total_de_todos(listas_productos)
                mostrar_lista(catalogo, "Catalogo total de productos:")

        case "6":
            if datos_cargados == False:
                print("ERROR, primero debe cargar las listas (opcion 1 o 2).")
            else:
                for i in range(len(listas_productos)):
                    recomendaciones = recomendaciones_para(listas_productos, i)
                    mostrar_lista(recomendaciones, f"Recomendaciones para {nombres_usuarios[i]}:")
                    print()

        case "7":
            print("Programa terminado.")
            break

        case _:
            print("Opcion Incorrecta")