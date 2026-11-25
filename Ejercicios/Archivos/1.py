import json

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
    print("11) Guardar alumnos en archivo JSON")
    print("12) Salir")


# Función para cargar automáticamente desde JSON al iniciar el programa
def cargar_alumnos_json() -> list:
    lista = []
    try:
        with open("alumnos.json", "r") as archivo:
            lista = json.load(archivo)
        print("¡Datos cargados automáticamente desde 'alumnos.json'!")
    except:
        print("No se encontró archivo previo, se inicia con lista vacía.")
    return lista


# Función para guardar la lista de diccionarios en formato JSON (Opción 11)
def guardar_alumnos_json(lista_alumnos: list) -> None:
    with open("alumnos.json", "w") as archivo:
        json.dump(lista_alumnos, archivo, indent=4)
    print("¡Datos guardados exitosamente en 'alumnos.json'!")


# (Las funciones 1 a 10 se mantienen exactamente igual que en el script anterior...)
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

def mostrar_alumnos(lista_alumnos: list) -> None:
    if len(lista_alumnos) == 0:
        print("La lista de alumnos está vacía.")
    else:
        print("\n--- LISTA DE ALUMNOS ---")
        print("Nombre          | Parcial 1  | Parcial 2  | Promedio  ")
        print("-" * 52)
        
        for i in range(len(lista_alumnos)):
            alumno = lista_alumnos[i]
            if alumno["activo"] == True:
                nombre = alumno["nombre"]
                n1 = alumno["nota_1"]
                n2 = alumno["nota_2"]
                
                tiene_promedio = False
                for clave in alumno.keys():
                    if clave == "promedio":
                        tiene_promedio = True
                
                if tiene_promedio == True:
                    prom = alumno["promedio"]
                    print(nombre, "          | ", n1, "       | ", n2, "       | ", prom)
                else:
                    print(nombre, "          | ", n1, "       | ", n2, "       | Sin calcular")

def calcular_promedios(lista_alumnos: list) -> None:
    for i in range(len(lista_alumnos)):
        alumno = lista_alumnos[i]
        if alumno["activo"] == True:
            promedio = (alumno["nota_1"] + alumno["nota_2"]) / 2
            alumno.update({"promedio": promedio})
    print("¡Promedios calculados y agregados exitosamente!")

def informar_estado_academico(lista_alumnos: list) -> None:
    print("\n--- ESTADOS ACADÉMICOS ---")
    hay_alumnos = False
    
    for i in range(len(lista_alumnos)):
        alumno = lista_alumnos[i]
        if alumno["activo"] == True:
            hay_alumnos = True
            tiene_promedio = False
            for clave in alumno.keys():
                if clave == "promedio":
                    tiene_promedio = True
            
            if tiene_promedio == True:
                prom = alumno["promedio"]
                estado = ""
                if prom >= 1 and prom < 4:
                    estado = "Desaprobado"
                if prom >= 4 and prom < 6:
                    estado = "Aprobado"
                if prom >= 6:
                    estado = "Promocionado"
                print("Alumno:", alumno["nombre"], "- Promedio:", prom, "- Estado:", estado)
            else:
                print("El alumno", alumno["nombre"], "no tiene el promedio calculado.")
                
    if hay_alumnos == False:
        print("No hay alumnos activos para evaluar.")

def buscar_alumno_por_nombre(lista_alumnos: list, nombre_buscado: str) -> None:
    encontrado = False
    for i in range(len(lista_alumnos)):
        alumno = lista_alumnos[i]
        if alumno["nombre"] == nombre_buscado and alumno["activo"] == True:
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

def ordenar_alumnos_por_promedio(lista_alumnos: list, ascendente: bool = True) -> None:
    if len(lista_alumnos) < 2:
        print("No hay suficientes alumnos para ordenar.")
    else:
        for i in range(len(lista_alumnos) - 1):
            for j in range(i + 1, len(lista_alumnos)):
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
                if prom >= 1 and prom < 4:
                    desaprobados += 1
                if prom >= 4 and prom < 6:
                    aprobados += 1
                if prom >= 6:
                    promocionados += 1
    print("\n--- CANTIDAD DE ESTADOS ---")
    print("Desaprobados:", desaprobados)
    print("Aprobados:", aprobados)
    print("Promocionados:", promocionados)


# =====================================================================
# PROGRAMA PRINCIPAL CON CARGA Y SALIDA AUTOMÁTICA
# =====================================================================
def principal():
    # Carga automática al correr el programa
    lista_general = cargar_alumnos_json()
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción (1-12): ")
        
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
            guardar_alumnos_json(lista_general)
        elif opcion == '12':
            # Guardado automático al salir con confirmación por parte del usuario
            respuesta = input("¿Desea guardar los cambios en el archivo JSON antes de salir? (s/n): ").lower()
            if respuesta == 's':
                guardar_alumnos_json(lista_general)
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

principal()