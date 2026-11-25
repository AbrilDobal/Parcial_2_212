from funciones import *

menu = """
===== SISTEMA DE PATENTES =====
1. Generar patentes.
2. Buscar patente.
3. Informar estadísticas.
4. Ordenar y mostrar patentes.
5. Salir.
==============================
Seleccione una opción: """

lista_patentes = []
bandera_generadas = False  # Bandera para controlar si se ejecutó el ítem 1

while True:
    opcion = input(menu)

    match opcion:
        case "1":
            cantidad_patentes = int(input("Ingrese la cantidad de patentes a generar: "))
            while cantidad_patentes < 1:
                cantidad_patentes = int(input("ERROR, reingrese la cantidad de patentes a generar (mayor a 0): "))

            cargar_patentes(cantidad_patentes, lista_patentes)
            bandera_generadas = True  # Se activa la bandera
            print(f"Se agregaron {cantidad_patentes} patentes. Total almacenadas: {len(lista_patentes)}.")

        case "2":
            if bandera_generadas:
                patente = transformar_a_mayusculas(input("Ingrese la patente a buscar: "))

                if validar_patente(patente):
                    if buscar_patente(lista_patentes, patente):
                        print(f"La patente {patente} fue encontrada.")
                    else:
                        print(f"La patente {patente} no fue encontrada.")
                else:
                    print("ERROR, formato de patente inválido (debe ser AB123CD).")
            else:
                print("ERROR, primero debe generar patentes (ítem 1).")

        case "3":
            if bandera_generadas:
                print(f"Patente más vieja: {obtener_patente_mas_vieja(lista_patentes)}")
                print(f"Patente más nueva: {obtener_patente_mas_nueva(lista_patentes)}")
                print("Porcentaje según letra inicial:")
                informar_porcentajes_letra_inicial(lista_patentes)
            else:
                print("ERROR, primero debe generar patentes (ítem 1).")

        case "4":
            if bandera_generadas:
                criterio = transformar_a_mayusculas(input("Ingrese el criterio de ordenamiento (ASC / DESC): "))
                while criterio != "ASC" and criterio != "DESC":
                    criterio = transformar_a_mayusculas(input("ERROR, reingrese el criterio de ordenamiento (ASC / DESC): "))

                ordenar_patentes_burbuja(lista_patentes, criterio)

                if criterio == "ASC":
                    print("Patentes ordenadas ASCENDENTEMENTE:")
                else:
                    print("Patentes ordenadas DESCENDENTEMENTE:")
                mostrar_patentes(lista_patentes)
            else:
                print("ERROR, primero debe generar patentes (ítem 1).")

        case "5":
            print("Programa terminado.")
            break

        case _:
            print("ERROR, opción inválida.")