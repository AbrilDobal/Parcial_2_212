import random

caracteres = ["A", "B", "C", "D", "E", "0", "7"]

puntaje = 100
apuesta_actual = 10

menu = """
 == TRAGAMONEDAS ==
1) Jugar
2) Cambiar apuesta
3) Salir

Seleccione una opcion: """

while True:
    opcion = input(menu)

    match opcion:
        case "1":
            # Si la apuesta actual supera el puntaje disponible, la ajustamos
            if apuesta_actual > puntaje:
                apuesta_actual = puntaje
                print(f"La apuesta se ajusto al puntaje disponible: {apuesta_actual}")

            # Genero la fila de 3 caracteres aleatorios
            indice_uno = random.randint(0, len(caracteres) - 1)
            indice_dos = random.randint(0, len(caracteres) - 1)
            indice_tres = random.randint(0, len(caracteres) - 1)

            char_uno = caracteres[indice_uno]
            char_dos = caracteres[indice_dos]
            char_tres = caracteres[indice_tres]

            print(f"Resultado: {char_uno} {char_dos} {char_tres}")

            # Aca se evalua el resultado
            if char_uno == "0" and char_dos == "0" and char_tres == "0":
                puntaje = 0
                print("Perdiste todos los puntos! Fin del juego.")
                break
            elif char_uno == char_dos and char_dos == char_tres and char_uno == "7":
                puntaje += apuesta_actual * 10
                print(f"Tres 7! Ganaste {apuesta_actual * 10} puntos.")
            elif char_uno == char_dos and char_dos == char_tres:
                puntaje += apuesta_actual * 5
                print(f"Tres iguales! Ganaste {apuesta_actual * 5} puntos.")
            elif char_uno == char_dos or char_dos == char_tres or char_uno == char_tres:
                puntaje += apuesta_actual * 2
                print(f"Dos iguales! Ganaste {apuesta_actual * 2} puntos.")
            else:
                puntaje -= apuesta_actual
                print(f"Todos distintos. Perdiste {apuesta_actual} puntos.")

            print(f"Puntaje actual: {puntaje}")

            if puntaje <= 0:
                puntaje = 0
                print("Te quedaste sin puntos! Fin del juego.")
                break

        case "2":
            nueva_apuesta = int(input("Ingrese el nuevo valor de apuesta: "))

            while nueva_apuesta < 1 or nueva_apuesta > puntaje:
                nueva_apuesta = int(input(f"ERROR, la apuesta debe ser entre 1 y {puntaje}. Reingrese: "))

            apuesta_actual = nueva_apuesta
            print(f"Apuesta actualizada a: {apuesta_actual}")

        case "3":
            print(f"Programa terminado. Puntaje final: {puntaje}")
            break
        case _:
            print("Opcion Incorrecta")