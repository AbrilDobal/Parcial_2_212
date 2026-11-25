import random


# ============================ ARCHIVO CSV (Lectura y Escritura) ============================

def cargar_juegos(ruta: str) -> list | None: #recibe la ruta del archivo
    """
    Lee el archivo CSV de videojuegos y lo transforma en una lista de diccionarios.
    La primera linea (encabezado) se ignora. Las lineas que no tengan 6 campos se descartan.

    Parametros:
    - ruta (str): ruta relativa del archivo CSV.

    Retorno:
    - list: lista de diccionarios con los videojuegos.
    - None: si el archivo no existe.
    """
    retorno = None
    datos = None

    try:
        with open(ruta, "r") as archivo:
            datos = archivo.read()
    except:
        datos = None

    if datos != None:
        retorno = [] #almacena los dic de cada juego
        lineas = datos.strip().split("\n") #elimina espacios o saltos de linea al inicio/final del archivo y divide el texto en una linea
        for i in range(1, len(lineas)): # omite la primera fila(contiene los encabezados)
            valores = lineas[i].strip().split(",")#limpia la linea actual y la divide por comas
            if len(valores) == 6:
                juego = { #convierto cada dato a su tipo correspondiente
                    "codigo_identificador": int(valores[0]),
                    "nombre": valores[1],
                    "genero": valores[2],
                    "precio": float(valores[3]),
                    "stock": int(valores[4]),
                    "unidades_vendidas": int(valores[5])
                } #juegos[i] accede a un elemento de la lista que es un dic
                retorno.append(juego) #agrega el diccionario del juego a nuestra lista

    return retorno #devuelve la lista con los juegos


def guardar_juegos(ruta: str, juegos: list[dict]) -> bool:
    """
    Sobreescribe el archivo CSV con los videojuegos que estan en memoria.
    Escribe primero el encabezado y luego una linea por juego.

    Parametros:
    - ruta (str): ruta relativa del archivo CSV.
    - juegos (list[dict]): lista de diccionarios con los videojuegos.

    Retorno:
    - bool: True si se escribio el archivo.
    """
    with open(ruta, "w") as archivo: #sobreescribe su contenido anterior
        archivo.write("codigo_identificador,nombre,genero,precio,stock,unidades_vendidas\n") #escribe la cabecera del archivo
        for i in range(len(juegos)):
            juego = juegos[i]
            archivo.write(f"{juego['codigo_identificador']},{juego['nombre']},{juego['genero']},{juego['precio']:.2f},{juego['stock']},{juego['unidades_vendidas']}\n") 
    retorno = True #devuelve true indicando que el archivo se guardo 

    return retorno 


# ============================ VALIDACIONES ============================
#Funciones auxiliares para asegurar que los datos ingresados por el usuario sean correctos

def es_entero_valido(cadena: str) -> bool:
    """
    Determina si una cadena esta formada unicamente por digitos (entero no negativo).

    Parametros:
    - cadena (str): cadena a evaluar.

    Retorno:
    - bool: True si la cadena no esta vacia y todos sus caracteres son digitos.
    """
    retorno = len(cadena) > 0

    for i in range(len(cadena)):
        if cadena[i] < "0" or cadena[i] > "9":
            retorno = False  # si encuentra algun caracter que no sea un digito (0-9), no es un entero valido

    return retorno


def es_decimal_valido(cadena: str) -> bool:
    """
    Determina si una cadena representa un numero decimal(como 199.99) no negativo (digitos y a lo sumo un punto).

    Parametros:
    - cadena (str): cadena a evaluar.

    Retorno:
    - bool: True si tiene al menos un digito, a lo sumo un punto y ningun otro caracter.
    """
    retorno = True
    cantidad_puntos = 0
    cantidad_digitos = 0

    for i in range(len(cadena)): #recorre contando cuantos puntos y cuando digitos tiene
        if cadena[i] == ".":
            cantidad_puntos += 1
        elif cadena[i] >= "0" and cadena[i] <= "9":
            cantidad_digitos += 1
        else:
            retorno = False

    if cantidad_puntos > 1 or cantidad_digitos == 0:
        retorno = False

    return retorno


def contiene_coma(cadena: str) -> bool:
    """
    Determina si una cadena contiene el caracter coma (Evita que el usuario ingrese comas en campos como el nombre del 
    videojuego, , lo cual rompería el formato de columnas al guardar en el archivo CSV.)

    Parametros:
    - cadena (str): cadena a evaluar.

    Retorno:
    - bool: True si la cadena tiene al menos una coma.
    """
    retorno = False

    for i in range(len(cadena)):#recorre caracter por caracter
        if cadena[i] == ",":
            retorno = True

    return retorno


def esta_en_lista(lista: list, valor: str) -> bool:
    """
    Determina si un valor esta dentro de una lista.

    Parametros:
    - lista (list): lista donde se busca.
    - valor (str): valor a buscar.

    Retorno:
    - bool: True si el valor esta en la lista, False si no.
    """
    retorno = False

    for i in range(len(lista)):
        if lista[i] == valor:
            retorno = True

    return retorno


def normalizar_genero(cadena: str, generos: list) -> str | None:
    """
    Compara una cadena con los generos validos sin importar mayusculas o minusculas.

    Parametros:
    - cadena (str): texto ingresado por el usuario.
    - generos (list): lista de generos validos, escritos en su forma canonica.

    Retorno:
    - str: el genero valido en su forma canonica (ej: "rPg" -> "RPG").
    - None: si la cadena no coincide con ningun genero.
    """
    retorno = None #por defecto none. asume que no lo va a encontrar
    texto = cadena.strip().lower()  # quita espacios de los extremos(strip) y pasa a minusculas(lower)

    for i in range(len(generos)):
        if retorno == None and generos[i].lower() == texto: #el género de la lista (convertido a minúsculas) coincide exactamente con lo que escribió el usuario
            retorno = generos[i] #Asigna el género original de la lista (ej. "RPG") a la variable retorno.

    return retorno


# ============================ ENTRADA DE DATOS ============================
#Estas funciones solicitan datos al usuario y no continúan hasta que se ingrese un valor válido.

def pedir_entero_no_negativo(mensaje: str) -> int:
    """
    Pide un entero(como el stock) no negativo por consola, reingresando hasta que sea valido.

    Parametros:
    - mensaje (str): mensaje que se muestra al usuario.

    Retorno:
    - int: el entero ingresado (mayor o igual a 0).
    """
    texto = input(mensaje).strip() #Muestra el mensaje en la pantalla input(), lee la respuesta del usuario y le quita los espacios en los extremos con .strip().
    while es_entero_valido(texto) == False:
        texto = input("ERROR, debe ser un numero entero no negativo. " + mensaje).strip() #Vuelve a pedir el dato mostrando un mensaje de error y limpia los espacios.

    return int(texto)


def pedir_precio(mensaje: str) -> float:
    """
    Pide un precio por consola (decimal con punto, mayor a 0), reingresando hasta que sea valido.

    Parametros:
    - mensaje (str): mensaje que se muestra al usuario.

    Retorno:
    - float: el precio ingresado (mayor a 0).
    """
    texto = input(mensaje).strip() #solicita al usuario el dato y elimina espacios extras
    while es_decimal_valido(texto) == False or float(texto) <= 0:  # si no es decimal, el "or" no llega a evaluar float()
        texto = input("ERROR, el precio debe ser un numero mayor a 0 (ej: 1999.99). " + mensaje).strip()

    return float(texto)


def pedir_nombre(mensaje: str) -> str:
    """
    Pide el nombre de un videojuego (entre 3 y 50 caracteres, sin comas), reingresando hasta que sea valido.
    Se eliminan los espacios sobrantes de los extremos.

    Parametros:
    - mensaje (str): mensaje que se muestra al usuario.

    Retorno:
    - str: el nombre validado.
    """
    nombre = input(mensaje).strip()#Solicita la entrada y remueve espacios en blanco iniciales/finales.
    while len(nombre) < 3 or len(nombre) > 50 or contiene_coma(nombre):
        nombre = input("ERROR, el nombre debe tener entre 3 y 50 caracteres y no puede tener comas. " + mensaje).strip()

    return nombre


def pedir_genero(mensaje: str, generos: list) -> str:
    """
    Pide un genero por consola y lo normaliza, reingresando hasta que sea uno de los validos.

    Parametros:
    - mensaje (str): mensaje que se muestra al usuario.
    - generos (list): lista de generos validos.

    Retorno:
    - str: el genero en su forma canonica.
    """
    genero = normalizar_genero(input(mensaje), generos)
    while genero == None:# el género ingresado no existe en la lista):
        genero = normalizar_genero(input("ERROR, genero invalido. " + mensaje), generos)

    return genero


def pedir_opcion(mensaje: str, opciones: list) -> str:
    """
    Pide una opcion de texto, la normaliza a minusculas sin espacios en los extremos
    y reingresa hasta que coincida con alguna de las opciones validas.
    para los menús de selección de opciones del sistema (como elegir el criterio de ordenamiento).

    Parametros:
    - mensaje (str): mensaje que se muestra al usuario.
    - opciones (list): lista de opciones validas, escritas en minusculas.

    Retorno:
    - str: la opcion elegida, normalizada.
    """
    texto = input(mensaje).strip().lower() #Pide la entrada del usuario, quita espacios y la convierte completamente a minúsculas.
    while esta_en_lista(opciones, texto) == False:
        texto = input("ERROR, opcion invalida. " + mensaje).strip().lower() #solicita nuevamente la opción en minúsculas.

    return texto


# ============================ BUSQUEDAS ============================

def buscar_indice_por_codigo(juegos: list[dict], codigo: int) -> int:
    """
    Busca un videojuego por su codigo identificador.Encontrar la posición exacta en memoria de un juego específico 
    para poder consultar, modificar su stock o registrar ventas.

    Parametros:
    - juegos (list[dict]): lista de videojuegos.
    - codigo (int): codigo identificador a buscar.

    Retorno:
    - int: el indice del juego en la lista, o -1 si no existe.
    """
    # -1 significa "no encontrado": nunca es un indice valido (van de 0 a len-1).
    # Se usa -1 y no None para que la funcion siempre devuelva un int, como dice su firma.
    retorno = -1 #Este será el resultado si el juego no existe en la lista.

    for i in range(len(juegos)):
        if retorno == -1 and juegos[i]["codigo_identificador"] == codigo: #Compara el código del juego en la posición actual i con el código que estamos buscando.
            retorno = i

    return retorno#El índice de posición de tipo entero (int) dentro de la lista (de 0 a N-1), 


def generar_codigo_unico(juegos: list[dict]) -> int:
    """
    Genera un codigo identificador aleatorio de 7 digitos que no este repetido en la lista.
    Asigna un ID único a cada nuevo videojuego que se registre en el sistema.

    Parametros:
    - juegos (list[dict]): lista de videojuegos existentes.

    Retorno:
    - int: codigo de 7 digitos unico dentro de la lista.
    """
    codigo = random.randint(1000000, 9999999)
    while buscar_indice_por_codigo(juegos, codigo) != -1: #(lo que significa que el código ya existe y pertenece a otro juego).
        codigo = random.randint(1000000, 9999999) #busque el código generado -> buscar_indice_por_codigo

    return codigo #porque la búsqueda devolvió -1, garantizando que el número es completamente nuevo y único 


# ============================ OPCION 1: ALTA ============================

def alta_videojuego(juegos: list[dict], generos: list, ruta: str) -> dict:
    """
    Da de alta UN videojuego: pide y valida los datos, genera el codigo unico,
    inicia las unidades vendidas en 0, lo agrega a la lista y actualiza el archivo CSV.

    Parametros:
    - juegos (list[dict]): lista de videojuegos (se modifica).
    - generos (list): lista de generos validos.
    - ruta (str): ruta relativa del archivo CSV.

    Retorno:
    - dict: el videojuego recien creado.
    """
    nombre = pedir_nombre("Ingrese el nombre del juego (3-50 caracteres): ")
    genero = pedir_genero("Ingrese el genero (RPG, Deportes, Carreras, Aventura, Estrategia): ", generos)
    precio = pedir_precio("Ingrese el precio (mayor a 0): ")
    stock = pedir_entero_no_negativo("Ingrese el stock: ")

    juego = { #datos en el dic y lo agrega a la lista juegos en memoria
        "codigo_identificador": generar_codigo_unico(juegos),
        "nombre": nombre,
        "genero": genero,
        "precio": precio,
        "stock": stock,
        "unidades_vendidas": 0
    }
    juegos.append(juego)# Añade el diccionario del juego recién creado al final de la lista juegos que se encuentra temporalmente en la memoria del programa.
    guardar_juegos(ruta, juegos) #llama a esta funcion para actualizar el archivo CSV fisicamente en el disco

    return juego


# ============================ OPCION 2: VENTA ============================

def contar_juegos_con_stock(juegos: list[dict]) -> int:
    """
    Cuenta los videojuegos que tienen stock mayor a 0.
    Para saber si existen productos disponibles para la venta antes de mostrar el menú de transacciones.

    Parametros:
    - juegos (list[dict]): lista de videojuegos.

    Retorno:
    - int: cantidad de juegos con stock.
    """
    contador = 0

    for i in range(len(juegos)):
        if juegos[i]["stock"] > 0:
            contador += 1

    return contador


def obtener_ancho_nombre(juegos: list[dict]) -> int:
    """
    Calcula el ancho necesario para alinear la columna de nombres (minimo: el largo del titulo = nombre).
    Se usa para formatear la salida en tablas de consola de forma que las columnas se alineen de forma ordenada.

    Parametros:
    - juegos (list[dict]): lista de videojuegos.

    Retorno:
    - int: el largo del nombre mas largo (o 6 si ninguno lo supera).
    """
    ancho = len("Nombre")

    for i in range(len(juegos)):
        if len(juegos[i]["nombre"]) > ancho:
            ancho = len(juegos[i]["nombre"]) #actualiza el valor del ancho con esta nueva longitud

    return ancho


def mostrar_juegos_con_stock(juegos: list[dict]) -> None:
    """
    Muestra por consola los videojuegos con stock, junto a su codigo identificador.
    Presenta una lista clara de qué juegos se pueden comprar en ese instante.

    Parametros:
    - juegos (list[dict]): lista de videojuegos.

    Retorno:
    - None.
    """
    ancho = obtener_ancho_nombre(juegos) + 2 #Obtiene el ancho de columna adecuado y le suma 2 espacios de margen.
    encabezado = f"{'Codigo':<12}{'Nombre':<{ancho}}{'Genero':<14}{'Precio':>14}{'Stock':>8}"
    print(encabezado)
    print("-" * len(encabezado)) #Dibuja una línea separadora del mismo largo de la cabecera.
    for i in range(len(juegos)):
        juego = juegos[i] #Obtiene el juego actual.
        if juego["stock"] > 0:
            print(f"{juego['codigo_identificador']:<12}{juego['nombre']:<{ancho}}{juego['genero']:<14}{juego['precio']:>14.2f}{juego['stock']:>8}")


def registrar_venta(juegos: list[dict], ruta: str) -> bool:
    """
    Registra la venta de un videojuego: muestra los juegos con stock, pide el codigo y la cantidad,si todo es correcto
    descuenta el stock, suma las unidades vendidas y actualiza el archivo CSV.
    La cantidad debe estar entre 1 y el stock disponible.
    Realiza y procesa la compra de uno o varios ejemplares de un videojuego.

    Parametros:
    - juegos (list[dict]): lista de videojuegos (se modifica).
    - ruta (str): ruta relativa del archivo CSV.

    Retorno:
    - bool: True si la venta se concreto, False si no (sin stock, codigo inexistente, etc.).
    """
    retorno = False

    if contar_juegos_con_stock(juegos) == 0:
        print("No hay juegos con stock disponible.")
    else:
        mostrar_juegos_con_stock(juegos) #Muestra la tabla de juegos con stock.
        texto = input("Ingrese el codigo identificador del juego a vender: ").strip()

        indice = -1 #Inicializa la posición del juego seleccionado en -1 (no encontrado).
        if len(texto) == 7 and es_entero_valido(texto):
            indice = buscar_indice_por_codigo(juegos, int(texto)) #para buscar el ID.

        if indice == -1:#Si el resultado es -1 (no se encontró ningún juego con ese identificador)
            print("ERROR, no existe un juego con ese codigo.")
        elif juegos[indice]["stock"] == 0:
            print("ERROR, el juego seleccionado no tiene stock.")
        else:
            stock = juegos[indice]["stock"] #Guarda de forma temporal el stock disponible de ese juego.
            cantidad = pedir_entero_no_negativo("Ingrese la cantidad de unidades a vender: ")
            while cantidad < 1 or cantidad > stock:
                cantidad = pedir_entero_no_negativo(f"ERROR, la cantidad debe estar entre 1 y {stock}. Reingrese: ")
            juegos[indice]["stock"] -= cantidad #Resta las unidades compradas del stock del juego.
            juegos[indice]["unidades_vendidas"] += cantidad #Suma las unidades compradas al registro de ventas de ese juego.
            guardar_juegos(ruta, juegos) #Guarda inmediatamente los datos actualizados en el archivo CSV.
            retorno = True

    return retorno


# ============================ OPCION 3: ESTADISTICAS ============================

def obtener_juego_mas_vendido(juegos: list[dict]) -> dict | None:
    """
    Busca el videojuego con mas unidades vendidas (si hay empate, devuelve el primero).
    Obtener información de rendimiento de ventas del catálogo

    Parametros:
    - juegos (list[dict]): lista de videojuegos.

    Retorno:
    - dict: el videojuego mas vendido.
    - None: si la lista esta vacia.
    """
    retorno = None

    for i in range(len(juegos)):
        if retorno == None or juegos[i]["unidades_vendidas"] > retorno["unidades_vendidas"]: #Si es el primer juego que evaluamos, o si el juego actual tiene más ventas que el juego que iba ganando
            retorno = juegos[i] #Guarda el juego actual como el nuevo más vendido de forma temporal.

    return retorno


def calcular_unidades_por_genero(juegos: list[dict], generos: list) -> list:
    """
    Acumula las unidades vendidas de cada genero.
    Crea una lista de acumuladores en cero y suma en ellos las ventas de los videojuegos agrupándolas por su categoría/género.
    Conocer el volumen total de ventas de cada categoría de juegos.

    Parametros:
    - juegos (list[dict]): lista de videojuegos.
    - generos (list): lista de generos validos.

    Retorno:
    - list: lista paralela a 'generos' con el total de unidades vendidas de cada uno.
    """
    acumuladores = [0] * len(generos) #Crea una lista paralela a la de géneros llena de ceros (ej: [0, 0, 0, 0, 0]) para usarlos como sumadores.

    for i in range(len(juegos)):
        for j in range(len(generos)):
            if juegos[i]["genero"] == generos[j]:
                acumuladores[j] += juegos[i]["unidades_vendidas"]#Suma las unidades vendidas de ese juego al acumulador correspondiente.

    return acumuladores #Devuelve la lista con las sumas totales de ventas agrupadas por género.


def calcular_valor_inventario(juegos: list[dict]) -> float:
    """
    Calcula el valor total del inventario (suma de stock * precio de cada juego).
    Permite calcular el valor monetario total de toda la mercancía almacenada.

    Parametros:
    - juegos (list[dict]): lista de videojuegos.

    Retorno:
    - float: valor total del inventario.
    """
    total = 0 #suma acumulada en 0

    for i in range(len(juegos)):
        total += juegos[i]["stock"] * juegos[i]["precio"] #multiplica el stock dispo por el precio unitario y lo suma al acum gnrl

    return total


def calcular_porcentaje_sin_stock(juegos: list[dict]) -> float:
    """
    Calcula qué fracción del total de juegos en el catálogo se encuentra actualmente sin stock (stock igual a 0) y lo convierte a porcentaje.
    Conocer el nivel de desabastecimiento de la tienda.

    Parametros:
    - juegos (list[dict]): lista de videojuegos.

    Retorno:
    - float: porcentaje (0 a 100). Es 0 si la lista esta vacia.
    """
    retorno = 0

    if len(juegos) != 0: #verifica y evita errores de division por cero
        sin_stock = len(juegos) - contar_juegos_con_stock(juegos) #stock - total de juegos
        retorno = sin_stock * 100 / len(juegos)

    return retorno 


def calcular_promedio_precios_por_genero(juegos: list[dict], generos: list) -> list:
    """
    Calcula el promedio de precios de cada genero.
    Suma los precios y cuenta cuántos títulos hay por cada género, para luego dividir la suma entre la cantidad.
    
    Parametros:
    - juegos (list[dict]): lista de videojuegos.
    - generos (list): lista de generos validos.

    Retorno:
    - list: lista paralela a 'generos' con el promedio de cada uno (None si el genero no tiene juegos).
    """
    sumas = [0] * len(generos) #Lista acumuladora para sumar los precios de cada género.
    cantidades = [0] * len(generos) #Lista acumuladora para contar cuántos juegos hay por cada género.
    promedios = [None] * len(generos) #Prepara la lista que guardará los promedios finales, inicializada con None (por si algún género no tiene juegos).
# Si un género no tiene juegos (cantidades[j] == 0), no hago la división para evitar dividir por cero y queda None, que al mostrar se imprime como 'sin juegos'
    for i in range(len(juegos)):
        for j in range(len(generos)):
            if juegos[i]["genero"] == generos[j]:
                sumas[j] += juegos[i]["precio"]
                cantidades[j] += 1

    for j in range(len(generos)): #cant generos procesada
        if cantidades[j] != 0: #si al menos un juego de ese genero
            promedios[j] = sumas[j] / cantidades[j]#suma de precios x cant de titulos

    return promedios


def mostrar_estadisticas(juegos: list[dict], generos: list) -> None:
    """
    Muestra por consola las estadisticas del catalogo: juego mas vendido, genero con mas unidades
    vendidas, valor total del inventario, porcentaje de juegos sin stock y promedio de precios por genero.

    Parametros:
    - juegos (list[dict]): lista de videojuegos.
    - generos (list): lista de generos validos.

    Retorno:
    - None.
    """
    if len(juegos) == 0: 
        print("No hay juegos cargados para calcular estadisticas.")
    else: #si hay juegos 
        mas_vendido = obtener_juego_mas_vendido(juegos) #llama a la funcion
        print(f"Videojuego mas vendido: {mas_vendido['nombre']} ({mas_vendido['unidades_vendidas']} unidades)")

        unidades = calcular_unidades_por_genero(juegos, generos)
        indice_mayor = 0 #genero mas vendido en 0
        for j in range(1, len(generos)): #Busca en la lista cuál es la posición con el número más alto de ventas.
            if unidades[j] > unidades[indice_mayor]: #genero actual supera al que iba ganando
                indice_mayor = j #actualiza el indice del genero mas vendido
        print(f"Genero con mas unidades vendidas: {generos[indice_mayor]} ({unidades[indice_mayor]} unidades)")

        print(f"Valor total del inventario: ${calcular_valor_inventario(juegos):.2f}")
        print(f"Porcentaje de videojuegos sin stock: {calcular_porcentaje_sin_stock(juegos):.2f}%")

        print("Promedio de precios por genero:") #encabezado 
        promedios = calcular_promedio_precios_por_genero(juegos, generos)
        for j in range(len(generos)): #genero disponible
            if promedios[j] == None:
                print(f"  - {generos[j]}: sin juegos") 
            else:
                print(f"  - {generos[j]}: ${promedios[j]:.2f}")#precio promedio


# ============================ OPCION 4: ORDENAMIENTO ============================

def intercambiar_elementos(lista: list, indice_i: int, indice_j: int) -> None:
    """
    Realiza un intercambio de posiciones (swap) entre dos elementos de una lista usando una variable temporal auxiliar.

    Parametros:
    - lista (list): lista a modificar.
    - indice_i (int): primer indice.
    - indice_j (int): segundo indice.

    Retorno:
    - None.
    """
    auxiliar = lista[indice_i]
    lista[indice_i] = lista[indice_j]
    lista[indice_j] = auxiliar


def obtener_valor_orden(juego: dict, criterio: str) -> str | float:
    """
    Extrae el campo que se usará para ordenar (nombre, género o precio) de un diccionario de videojuego. 
    Los textos se pasan a minusculas para que el orden no dependa de mayusculas.
    Facilita que la comparación al ordenar no distinga entre mayúsculas y minúsculas (evitando que la "Z" mayúscula vaya antes que la "a" minúscula).

    Parametros:
    - juego (dict): videojuego.
    - criterio (str): "nombre", "genero" o "precio".

    Retorno:
    - str | float: el valor a comparar.
    """
    if criterio == "precio": #ordenar segun el precio
        retorno = juego["precio"] #el valor del precio
    else:
        retorno = juego[criterio].lower()#obtiene el texto lo convierte a minúsculas con .lower() para evitar que las mayúsculas alteren el orden del abecedario.

    return retorno


def ordenar_juegos(juegos: list[dict], criterio: str, ascendente: bool) -> list[dict]:
    """
    Ordena (burbujeo) una COPIA de la lista de videojuegos segun un criterio.
    La lista original no se modifica.
    Organizar de manera lógica el catálogo bajo distintas prioridades visuales.

    Parametros:
    - juegos (list[dict]): lista de videojuegos.
    - criterio (str): "nombre", "genero" o "precio".
    - ascendente (bool): True para orden ascendente, False para descendente.

    Retorno:
    - list[dict]: nueva lista ordenada.
    """
    copia = juegos.copy() #copia de la lista para poder reordenarla libremente sin modificar la lista original del sistema.

    for i in range(len(copia) - 1): #bubble sort(desde el primer elemento)
        for j in range(i + 1, len(copia)): #compara el elemento actual i con todos los elementos siguientes j.
            valor_i = obtener_valor_orden(copia[i], criterio) #extrae el valor de ordenamiento del elemento de la posicion i 
            valor_j = obtener_valor_orden(copia[j], criterio)
            if (ascendente == True and valor_i > valor_j) or (ascendente == False and valor_i < valor_j):
                intercambiar_elementos(copia, i, j)

    return copia #Devuelve la nueva lista completamente ordenada.

def solicitar_criterios_orden() -> tuple:
    """
    Pide por consola el criterio de ordenamiento (nombre, genero o precio) y el sentido (asc o desc).
    Ambos datos se normalizan, por lo que "DeSc" o "GÉNERO" son entradas validas.
    Configurar los parámetros de ordenamiento preferidos por el usuario.

    Parametros:
    - Ninguno.

    Retorno:
    - tuple: (criterio (str), ascendente (bool)).
    """
    criterio = pedir_opcion("Ordenar por (nombre / genero / precio): ", ["nombre", "genero", "género", "precio"])
    if criterio == "género":
        criterio = "genero" #Lo unifica a "genero" sin tilde para que coincida exactamente con las claves del diccionario.

    sentido = pedir_opcion("Sentido (asc / desc): ", ["asc", "desc"])

    return criterio, sentido == "asc"#(True si eligió "asc", o False si eligió "desc").


def mostrar_catalogo(juegos: list[dict]) -> None:
    """
    Muestra por consola todas las caracteristicas de cada videojuego (tenga stock o no), en forma de tabla.
    Mostrar el estado general e íntegro de la base de datos de videojuegos.

    Parametros:
    - juegos (list[dict]): lista de videojuegos.

    Retorno:
    - None.
    """
    if len(juegos) == 0:
        print("El catalogo esta vacio.")
    else:
        ancho = obtener_ancho_nombre(juegos) + 2 #la columna de nombres se alinee correctamente.
        encabezado = f"{'Codigo':<12}{'Nombre':<{ancho}}{'Genero':<14}{'Precio':>14}{'Stock':>8}{'Vendidas':>10}"
        print(encabezado)
        print("-" * len(encabezado))
        for i in range(len(juegos)):
            juego = juegos[i] #Obtiene el diccionario del juego actual.
            print(f"{juego['codigo_identificador']:<12}{juego['nombre']:<{ancho}}{juego['genero']:<14}{juego['precio']:>14.2f}{juego['stock']:>8}{juego['unidades_vendidas']:>10}")