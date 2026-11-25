from ejercicios import *

print("=== calcular_fibonacci (f0 a f10) ===")
for i in range(11):
    print(f"f{i} =", calcular_fibonacci(i))     # 0 1 1 2 3 5 8 13 21 34 55
print("f(-1) =", calcular_fibonacci(-1))        # None
print("f(50) =", calcular_fibonacci(50))        # 12586269025

print("\n=== mostrar_serie_fibonacci ===")
mostrar_serie_fibonacci(5)
print("---")
mostrar_serie_fibonacci(0)
print("---")
mostrar_serie_fibonacci(1)
print("---")
mostrar_serie_fibonacci(-2)

print("\n=== determinar_suma_consecutiva ===")
for numero in [0, 1, 2, 3, 4, 5, 7, 9, 10, 11, 101]:
    print(numero, "->", determinar_suma_consecutiva(numero))   # True: 3 5 7 9 11 101
print("1 con inicio=0 ->", determinar_suma_consecutiva(1, 0))  # True (0 + 1)