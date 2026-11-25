from Entrada import *
from Array_Generales import *


lista_numeros = []
datos_cargados = False

menu = """
 == MENU DE NUMEROS ==
1) Ingresar datos
2) Cantidad de positivos y negativos
3) Suma de los numeros pares
4) Mayor numero impar
5) Listar los numeros ingresados
6) Listar los numeros pares
7) Listar los numeros en posiciones impares
8) Salir

Seleccione una opcion: """

while True:
    opcion = input(menu)

    match opcion:
        case "1":
            lista_numeros = ingresar_numeros(10)
            datos_cargados = True
            print("Numeros cargados correctamente.")

        case "2":
            if datos_cargados == False:
                print("ERROR, primero debe ingresar los datos (opcion 1).")
            else:
                conteo = contar_positivos_negativos(lista_numeros)
                print(f"Positivos: {conteo[0]}, Negativos: {conteo[1]}")

        case "3":
            if datos_cargados == False:
                print("ERROR, primero debe ingresar los datos (opcion 1).")
            else:
                print("Suma de los numeros pares:", sumar_pares(lista_numeros))

        case "4":
            if datos_cargados == False:
                print("ERROR, primero debe ingresar los datos (opcion 1).")
            else:
                resultado = mayor_impar(lista_numeros)
                if resultado == None:
                    print("No hay numeros impares en la lista.")
                else:
                    print("El mayor numero impar es:", resultado)

        case "5":
            if datos_cargados == False:
                print("ERROR, primero debe ingresar los datos (opcion 1).")
            else:
                print("Numeros ingresados:", end=" ")
                listar_elementos(lista_numeros)

        case "6":
            if datos_cargados == False:
                print("ERROR, primero debe ingresar los datos (opcion 1).")
            else:
                print("Numeros pares:", end=" ")
                listar_pares(lista_numeros)

        case "7":
            if datos_cargados == False:
                print("ERROR, primero debe ingresar los datos (opcion 1).")
            else:
                print("Numeros en posiciones impares:", end=" ")
                listar_posiciones_impares(lista_numeros)

        case "8":
            print("Programa terminado.")
            break

        case _:
            print("Opcion Incorrecta")