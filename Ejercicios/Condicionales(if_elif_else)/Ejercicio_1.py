#Abril Dobal
# 1. A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la 
# posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

altura = int(input("Ingrese la altura del jugador en cm: "))

if altura < 160:
    print("Posición: Base")
elif altura < 180:  # 160 a 179
    print("Posición: Escolta")
elif altura < 200:  # 180 a 199
    print("Posición: Alero")
else:  # 200 o más
    print("Posición: Ala-Pívot o Pívot")

# Abril Dobal
# 2.Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota
#  es ...

nota = int(input("Ingrese la nota (1 a 10): "))

if nota >= 6:  # 6, 7, 8, 9, 10
    print(f"Promoción directa, la nota es {nota}")
elif nota >= 4:  # 4 y 5
    print(f"Aprobado, la nota es {nota}")
else:  # 1, 2, 3
    print(f"Desaprobado, la nota es {nota}")