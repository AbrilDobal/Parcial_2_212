from input import *

edad = get_int("Ingrese su edad (18-120): ", "ERROR, edad invalida.", 18, 120, 2)
altura = get_float("Ingrese su altura en metros (0.5-2.5): ", "ERROR, altura invalida.", 0.5, 2.5, 2)
nombre = get_string("Ingrese su nombre (max 10 letras): ", "ERROR, largo invalido.", 10, 2)

print(edad, altura, nombre)