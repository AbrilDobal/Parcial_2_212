import funciones as f

ruta_csv = "juegos.csv" # Define una variable con el nombre del archivo de texto (CSV) donde se almacenarán y leerán los datos de los videojuegos.
generos = ["RPG", "Deportes", "Carreras", "Aventura", "Estrategia"] #Crea una lista con los géneros de videojuegos que están permitidos en tu sistema.

menu = """
============ TIENDA DE VIDEOJUEGOS ============
1) Alta de videojuego
2) Registrar una venta
3) Consultar estadisticas
4) Mostrar catalogo ordenado
5) Salir

Seleccione una opcion: """

juegos = f.cargar_juegos(ruta_csv)
if juegos == None:
    print("No se encontro el archivo juegos.csv, se inicia con un catalogo vacio.")
    juegos = []
else:
    print(f"Se cargaron {len(juegos)} juegos desde {ruta_csv}.") # Muestra un mensaje indicando cuántos videojuegos se cargaron exitosamente a la memoria.

while True:
    opcion = input(menu).strip() # elimina cualquier espacio en blanco innecesario que el usuario haya escrito por error.

    match opcion:
        case "1":
            nuevo = f.alta_videojuego(juegos, generos, ruta_csv) #Llama a la función para registrar un nuevo videojuego pidiendo los datos requeridos y lo guarda en el archivo.
            print(f"Juego '{nuevo['nombre']}' dado de alta con el codigo {nuevo['codigo_identificador']}.")
        case "2":
            if f.registrar_venta(juegos, ruta_csv) == True:
                print("Venta registrada con exito.")
        case "3":
            f.mostrar_estadisticas(juegos, generos)
        case "4":
            criterio, ascendente = f.solicitar_criterios_orden()
            ordenados = f.ordenar_juegos(juegos, criterio, ascendente)
            f.mostrar_catalogo(ordenados)
        case "5":
            print("Programa terminado.")
            break
        case _:
            print("ERROR, opcion invalida.")