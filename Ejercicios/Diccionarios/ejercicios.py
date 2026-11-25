# Desarrolle un programa con un menú que contenga los siguientes ítems y una opción para salir:

# =====================================================================
# PROGRAMA DE GESTIÓN DE ALUMNOS (DICCIONARIOS Y LISTAS)
# =====================================================================

def mostrar_menu():
    print("\n================ MENÚ DE GESTIÓN DE ALUMNOS ================")
    print("1) Alta de alumno")
    print("2) Mostrar lista de alumnos")
    print("3) Calcular y agregar promedio")
    print("4) Informar estado académico de cada alumno")
    print("5) Buscar alumno por nombre (notas y promedio)")
    print("6) Baja física de un alumno")
    print("7) Baja lógica de un alumno")
    print("8) Alumno con mejor / peor promedio")
    print("9) Ordenar alumnos por promedio (ASC / DESC)")
    print("10) Contar alumnos según estado académico")
    print("11) Salir")

# 1)Alta: Desarrolle una función que permita cargar un diccionario a partir de los datos que ingresa el
# usuario por consola, los datos se componen por un nombre de alumno y 2 calificaciones (primer y segundo examen parcial).

def alta_alumno() -> dict:
    nombre = input("Ingrese el nombre del alumno: ")
    nota_1 = float(input("Ingrese la nota del primer parcial: "))
    nota_2 = float(input("Ingrese la nota del segundo parcial: "))
    
    alumno = {
        "nombre": nombre,
        "nota_1": nota_1,
        "nota_2": nota_2,
        "activo": True
    }
    return alumno

# 2) Desarrolle una función que muestre una lista de alumnos y sus respectivos datos en filas y columnas,
# donde cada fila representa un alumno y cada columna representa uno de sus datos.

def mostrar_alumnos(lista_alumnos: list) -> None:
    if len(lista_alumnos) == 0:
        print("La lista de alumnos está vacía.")
    else:
        print("\n--- LISTA DE ALUMNOS ---")
        print("Nombre          | Parcial 1  | Parcial 2  | Promedio  ")
        print("-" * 52)
        
        for i in range(len(lista_alumnos)):
            alumno = lista_alumnos[i]
            
            # Verificamos si el alumno está activo
            if alumno["activo"] == True:
                nombre = alumno["nombre"]
                n1 = alumno["nota_1"]
                n2 = alumno["nota_2"]
                
                # Verificamos si existe la clave "promedio" usando .keys() (según apuntes)
                tiene_promedio = False
                for clave in alumno.keys():
                    if clave == "promedio":
                        tiene_promedio = True
                
                if tiene_promedio == True:
                    prom = alumno["promedio"]
                    print(nombre, "          | ", n1, "       | ", n2, "       | ", prom)
                else:
                    print(nombre, "          | ", n1, "       | ", n2, "       | Sin calcular")

# 3) Modificación: Desarrolle una función que permita calcular el promedio de calificaciones a partir de
# una lista de alumnos. Recibe una lista de diccionarios por parámetro, calcula el promedio y lo agrega
# como unítem másal diccionario.

def calcular_promedios(lista_alumnos: list) -> None:
    for i in range(len(lista_alumnos)):
        alumno = lista_alumnos[i]
        if alumno["activo"] == True:
            promedio = (alumno["nota_1"] + alumno["nota_2"]) / 2
            # Usamos update como vimos en los apuntes
            alumno.update({"promedio": promedio})
    print("¡Promedios calculados y agregados exitosamente!")

# 4) Desarrolle una función que informe por cada alumno de la lista su estado académico (promedio de 1 al
# 4: desaprobado, 4 o 5: aprobado, y 6 o más: promocionado).

def informar_estado_academico(lista_alumnos: list) -> None:
    print("\n--- ESTADOS ACADÉMICOS ---")
    hay_alumnos = False
    
    for i in range(len(lista_alumnos)):
        alumno = lista_alumnos[i]
        if alumno["activo"] == True:
            hay_alumnos = True
            
            # Verificamos si tiene promedio con .keys()
            tiene_promedio = False
            for clave in alumno.keys():
                if clave == "promedio":
                    tiene_promedio = True
            
            if tiene_promedio == True:
                prom = alumno["promedio"]
                estado = ""
                
                if prom >= 1:
                    if prom < 4:
                        estado = "Desaprobado"
                
                if prom >= 4:
                    if prom < 6:
                        estado = "Aprobado"
                
                if prom >= 6:
                    estado = "Promocionado"
                
                print("Alumno:", alumno["nombre"], "- Promedio:", prom, "- Estado:", estado)
            else:
                print("El alumno", alumno["nombre"], "no tiene el promedio calculado.")
                
    if hay_alumnos == False:
        print("No hay alumnos activos para evaluar.")

# 5) Desarrolle una función que informe las notas y el promedio del alumno cuyo nombre recibe por
# parámetro, en caso de no encontrarlo deberá imprimir un mensaje de error.

def buscar_alumno_por_nombre(lista_alumnos: list, nombre_buscado: str) -> None:
    encontrado = False
    for i in range(len(lista_alumnos)):
        alumno = lista_alumnos[i]
        if alumno["nombre"] == nombre_buscado:
            if alumno["activo"] == True:
                encontrado = True
                print("\n--- Datos del Alumno:", alumno["nombre"], "---")
                print("Parcial 1:", alumno["nota_1"])
                print("Parcial 2:", alumno["nota_2"])
                
                tiene_promedio = False
                for clave in alumno.keys():
                    if clave == "promedio":
                        tiene_promedio = True
                
                if tiene_promedio == True:
                    print("Promedio:", alumno["promedio"])
                else:
                    print("Promedio: No calculado aún.")
                break
            
    if encontrado == False:
        print("Error: El alumno no se encuentra registrado o está inactivo.")

# 6) Baja Física: Desarrolle una función que pueda eliminar a un alumno de la lista de alumnos. El alumno
# a eliminar deberá seleccionarlo el usuario por terminal, validar que exista antes de eliminarlo, y en
# caso de que no exista mostrar un mensaje de error.

def baja_fisica(lista_alumnos: list) -> None:
    nombre_a_borrar = input("Ingrese el nombre del alumno a eliminar físicamente: ")
    indice_encontrado = -1
    
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]["nombre"] == nombre_a_borrar:
            indice_encontrado = i
            break
            
    if indice_encontrado != -1:
        lista_alumnos.pop(indice_encontrado)
        print("El alumno fue eliminado físicamente con éxito.")
    else:
        print("Error: El alumno no existe en la lista.")

# 7) Baja Lógica: Desarrolle una función que pueda dar de baja lógicamente a un alumno de la lista.
# Deberá recibir por parámetro el nombre del alumno a eliminar y agregarle un estado (bool) activo o
# inactivo. Modificar la función que muestra los alumnos haciendo que ignore a todos los alumnos
# inactivos.

def baja_logica(lista_alumnos: list, nombre_a_dar_de_baja: str) -> None:
    encontrado = False
    for i in range(len(lista_alumnos)):
        alumno = lista_alumnos[i]
        if alumno["nombre"] == nombre_a_dar_de_baja:
            alumno.update({"activo": False})
            encontrado = True
            print("El alumno fue dado de baja lógica correctamente.")
            break
            
    if encontrado == False:
        print("Error: No se encontró al alumno.")

# 8) Desarrolle una función que busque al alumno con el mejor o con el peor promedio. Informar sus
# nombres y sus respectivos promedios.

def alumno_mejor_peor_promedio(lista_alumnos: list) -> None:
    activos_con_promedio = []
    
    for i in range(len(lista_alumnos)):
        alumno = lista_alumnos[i]
        if alumno["activo"] == True:
            tiene_promedio = False
            for clave in alumno.keys():
                if clave == "promedio":
                    tiene_promedio = True
            if tiene_promedio == True:
                activos_con_promedio += [alumno]
            
    if len(activos_con_promedio) == 0:
        print("No hay alumnos activos con promedio calculado.")
    else:
        mejor = activos_con_promedio[0]
        peor = activos_con_promedio[0]
        
        for i in range(1, len(activos_con_promedio)):
            if activos_con_promedio[i]["promedio"] > mejor["promedio"]:
                mejor = activos_con_promedio[i]
            if activos_con_promedio[i]["promedio"] < peor["promedio"]:
                peor = activos_con_promedio[i]
                
        print("\n--- MEJOR PROMEDIO ---")
        print("Nombre:", mejor["nombre"], "- Promedio:", mejor["promedio"])
        
        print("\n--- PEOR PROMEDIO ---")
        print("Nombre:", peor["nombre"], "- Promedio:", peor["promedio"])

# 9) Desarrolle una función que ordene a los alumnos por promedio ASC/DESC.

def ordenar_alumnos_por_promedio(lista_alumnos: list, ascendente: bool = True) -> None:
    if len(lista_alumnos) < 2:
        print("No hay suficientes alumnos para ordenar.")
    else:
        for i in range(len(lista_alumnos) - 1):
            for j in range(i + 1, len(lista_alumnos)):
                # Verificamos que ambos tengan la clave promedio
                tiene_prom_i = False
                tiene_prom_j = False
                
                for clave in lista_alumnos[i].keys():
                    if clave == "promedio":
                        tiene_prom_i = True
                for clave in lista_alumnos[j].keys():
                    if clave == "promedio":
                        tiene_prom_j = True
                
                if tiene_prom_i == True and tiene_prom_j == True:
                    debe_cambiar = False
                    
                    if ascendente == True:
                        if lista_alumnos[i]["promedio"] > lista_alumnos[j]["promedio"]:
                            debe_cambiar = True
                    else:
                        if lista_alumnos[i]["promedio"] < lista_alumnos[j]["promedio"]:
                            debe_cambiar = True
                            
                    if debe_cambiar == True:
                        aux = lista_alumnos[i]
                        lista_alumnos[i] = lista_alumnos[j]
                        lista_alumnos[j] = aux
                        
        print("¡Alumnos ordenados por promedio con éxito!")

# 10) Desarrolle una función que calcule e informe la cantidad de alumnos según su estado académico
# (desaprobado, aprobado o promocionado).

def contar_por_estado_academico(lista_alumnos: list) -> None:
    desaprobados = 0
    aprobados = 0
    promocionados = 0
    
    for i in range(len(lista_alumnos)):
        alumno = lista_alumnos[i]
        if alumno["activo"] == True:
            tiene_promedio = False
            for clave in alumno.keys():
                if clave == "promedio":
                    tiene_promedio = True
            
            if tiene_promedio == True:
                prom = alumno["promedio"]
                if prom >= 1:
                    if prom < 4:
                        desaprobados += 1
                if prom >= 4:
                    if prom < 6:
                        aprobados += 1
                if prom >= 6:
                    promocionados += 1
                
    print("\n--- CANTIDAD DE ALUMNOS POR ESTADO ---")
    print("Desaprobados:", desaprobados)
    print("Aprobados:", aprobados)
    print("Promocionados:", promocionados)


# =====================================================================
# PROGRAMA PRINCIPAL (EJECUCIÓN DEL MENÚ)
# =====================================================================
def principal():
    lista_general = []
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción (1-11): ")
        
        if opcion == '1':
            nuevo = alta_alumno()
            lista_general += [nuevo]
            print("¡Alumno agregado con éxito!")
            
        elif opcion == '2':
            mostrar_alumnos(lista_general)
            
        elif opcion == '3':
            calcular_promedios(lista_general)
            
        elif opcion == '4':
            informar_estado_academico(lista_general)
            
        elif opcion == '5':
            nombre_busq = input("Ingrese el nombre del alumno a buscar: ")
            buscar_alumno_por_nombre(lista_general, nombre_busq)
            
        elif opcion == '6':
            baja_fisica(lista_general)
            
        elif opcion == '7':
            nombre_baja = input("Ingrese el nombre del alumno para dar de baja lógica: ")
            baja_logica(lista_general, nombre_baja)
            
        elif opcion == '8':
            alumno_mejor_peor_promedio(lista_general)
            
        elif opcion == '9':
            criterio = input("¿Desea ordenar de forma ascendente? (s/n): ")
            if criterio == 's':
                ordenar_alumnos_por_promedio(lista_general, True)
            else:
                ordenar_alumnos_por_promedio(lista_general, False)
                
        elif opcion == '10':
            contar_por_estado_academico(lista_general)
            
        elif opcion == '11':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Para ejecutar el programa:
principal()