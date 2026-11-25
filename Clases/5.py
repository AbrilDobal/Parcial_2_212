# #esqueleto de un menu de opciones
# menu = """ 
#  == MENU ==
# 1) Jugar
# 2) Informar resultado
# 3) Salir

# Selecciones una opcion: """


# while True:
#     opcion = input(menu)

#     match opcion:
#         case "1":
#             print("JUGANDO.....") #escribir nuestra logica
#         case "2":
#             print("INFORMANDO.....")
#         case "3":
#             print("Programa terminado.")
#             break
#         case _:
#             print("Opcion Incorrecta")

#parametros: se pueden cambiar excepto que no puede valer 0 la apuesta minima
#aprobado o desaprobado
#como genero aleatoriamente caracteres:
import random
caracteres = "ABCDE07"
lista = ["A", "B", "C", "D", "E", "0", "7"]


indice_aleatorio = random.randint(0, len(lista) - 1)

print(indice_aleatorio, caracteres[indice_aleatorio], lista[indice_aleatorio]) #pensar como repetir

