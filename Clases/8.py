# RECURSIVIDAD: Una funcion recursiva es una funcion que se invoca a si misma.
# * Absolutamente todo, lo que se puede resolver con recursividad, se puede resolver con BUCLES.

# Factorial:
# 0! -> 1

# 5! -> 5 * 4 * 3 * 2 * 1 -> 120
# 5! -> 1 * 2 * 3 * 4 * 5 -> 120

# def calcular_factorial(num:int)->int:
#     """Documentacion"""
#     resultado = 1
#     # v0.5
#     # contador = 1
#     # while contador <= num:
#     #     contador += 1
#     # v1
#     # for numero in range(num, 0, -1):
#     # v2
#     for numero in range(1, num + 1): # [1, 2, 3, 4, 5]
#         resultado *= numero # resultado = resultado * numero
#     return resultado




# 5! -> 5 * 4!                      -> 120
# 5! -> 5 * 4 * 3!                  -> 120
# 5! -> 5 * 4 * 3 * 2!              -> 120
# 5! -> 5 * 4 * 3 * 2 * 1!          -> 120
# 5! -> 5 * 4 * 3 * 2 * 1 * 0!      -> 120


# def calcular_factorial_recursiva(num:int)->int|None:
#     """Documentacion"""
#     if num == 0:
#         resultado = 1
#     elif num < 0:
#         resultado = None
#     else:
#         resultado = num * calcular_factorial_recursiva(num - 1)
#     return resultado


# numero = 5
# print(f"El factorial de {numero} es {calcular_factorial(numero)} con BUCLE.")
# res = calcular_factorial_recursiva(numero)
# if res == None:
#     print("NO se puede calcular el factorial de numeros negativos.")
# else:
#     print(f"El factorial de {numero} es {calcular_factorial_recursiva(numero)} con RECURSIVA.")





# def calc_fact(num:int)->int:
#     if num <= 0:
#         resultado = 1
#     else:
#         resultado = num * calc_fact(num - 1)
#     return resultado

# def calc_fact(num:int)->int:
#     if num <= 0:
#         resultado = 1
#     else:
#         resultado = num * calc_fact(num - 1)
#     return resultado

# def calc_fact(num:int)->int:
#     if num <= 0:
#         resultado = 1
#     else:
#         resultado = num * calc_fact(num - 1)
#     return resultado

# def calc_fact(num:int)->int:
#     if num <= 0:
#         resultado = 1
#     else:
#         resultado = num * calc_fact(num - 1)
#     return resultado


# print(calc_fact(3))






# Fibonacci

# f0 = 0
# f1 = 1
# f2 = 1 + 0 = 1
# f3 = 1 + 1 = 2
# f4 = 2 + 1 = 3
# f5 = 3 + 2 = 5
# f6 = 5 + 3 = 8
# f7 = 8 + 5 = 13
# f8 = 13 + 8 = 21
# f9 = 21 + 13 = 34
# f10 = 34 + 21 = 55
# f11 = 55 + 34 = 89
# f12 = 89 + 55 = 144



# f2 = f1 + f0
# f3 = f2 + f1
# f4 = f3 + f2
# f(n) = f(n-1) + f(n-2)

# f(7) = f(6) + f(5)
#      = f(6-5)




# RECURSIVA
def calcular_fibonacci_r(num:int)->int|None:
    """Documentacion"""
    if num == 0 or num == 1:
        resultado = num
    elif num < 0:
        resultado = None
    else:
        resultado = calcular_fibonacci_r(num - 1) + calcular_fibonacci_r(num - 2)
    return resultado



# f2 = f1 + f0
# f3 = f2 + f1
# f4 = f3 + f2
# f(n) = f(n-1) + f(n-2)


# BUCLE                  7
def calcular_fibonacci(num:int)->int|None:
    """Documentacion"""
    lista = [0, 1]
    if num < 0:
        resultado = None
    elif num == 1 or num == 0:
        resultado = num
    else:
        for _ in range(num - 1): # [0,1,2,3,4,5]
        # proximo = lista[-1] + lista[-2]
            proximo = lista[len(lista)-1] + lista[len(lista)-2]
            lista += [proximo]
        resultado = lista[len(lista)-1]
        # print(lista)
        
    return resultado

numero = 2000
res = calcular_fibonacci(numero)
if res == None:
    print("No se puede calcular fibonacci de numeros negativos.")
else:
    print(f"BUCLE: El resultado de la sucesion {numero}° de fibonacci es {res}.")
    # res_r = calcular_fibonacci_r(numero)
    # print(f"RECURSIVA: El resultado de la sucesion {numero}° de fibonacci es {res_r}.")








# Fibonacci de n = 7


# n0 = 0
# n1 = 1
# Formula: suma de los dos anteriores
# n2 = 1 + 0 | (n1 + n0) -> 1
# n3 = 1 + 1 | (n2 + n1) -> 2
# n4 = 2 + 1 | (n3 + n2) -> 3
# n5 = 3 + 2 | (n4 + n3) -> 5
# n6 = 5 + 3 | (n5 + n4) -> 8
# n7 = 8 + 5 | (n6 + n5) -> 13


# Establecemos un caso base:
# SI N es mayor a la base: aplicamos la formula.
# Sumamos los dos anteriores.

# Solucion con listas:
# lista_fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]

# Sin listas: 
# anteultimo = 0
# ultimo = 1
# proximo = ultimo + anteultimo
# anteultimo = ultimo
# ultimo = proximo

