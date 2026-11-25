from ejercicios import *

print("1)", verificar_es_par(10), verificar_es_par(7))                         # True False
print("2)", verificar_es_letra("a"), verificar_es_letra("Z"), verificar_es_letra("5"), verificar_es_letra("ñ"))  # True True False False
print("3)", verificar_es_digito("0"), verificar_es_digito("9"), verificar_es_digito("a"))  # True True False
print("4)", validar_numero_entero(5, 1, 10), validar_numero_entero(10, 1, 10), validar_numero_entero(11, 1, 10))  # True True False
print("7)", medir_largo_cadena("hola mundo"), medir_largo_cadena(""))          # 10 0
print("8)", verificar_es_primo(13), verificar_es_primo(15), verificar_es_primo(1))  # True False False
print("9)", calcular_factorial(5), calcular_factorial(0), calcular_factorial(-3))   # 120 1 None
print("10)", verificar_dni("12345"), verificar_dni("123456"), verificar_dni("12345678"), verificar_dni("123456789"))  # False True True False
print("11)", completar_dni("123456"), completar_dni("1234567"), completar_dni("12345678"))  # 00123456 01234567 12345678
for cadena in ["0", "7", "10", "15", "16", "20", "21", "22", "29", "30", "31", "45", "99", "100", "101", "115", "120", "200", "321", "500", "999", "987", "007", "1000", "12a", ""]:
    print("12)", cadena, "->", convertir_numero_a_letras(cadena))

edad = solicitar_entero_validado("Ingrese su edad (18-120): ", 18, 120)
print("5)", edad, "tipo entero sumando 1:", edad + 1)
respuesta = solicitar_opcion("Continuar? (si/no): ", "si", "no")
print("6)", respuesta)