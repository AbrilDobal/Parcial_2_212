# Pruebas de las funciones puras del modulo (sin entrada por consola).
from Funciones_casino import *

print("valor carta:", calcular_valor_carta("A"), calcular_valor_carta("K"), calcular_valor_carta("10"), calcular_valor_carta("7"))  # 11 10 10 7
print("mano A K       =", calcular_valor_mano(["A", "K"]))            # 21
print("mano A A 9     =", calcular_valor_mano(["A", "A", "9"]))       # 21
print("mano A 5 K     =", calcular_valor_mano(["A", "5", "K"]))       # 16
print("mano K Q 5     =", calcular_valor_mano(["K", "Q", "5"]))       # 25
print("mano A A A A   =", calcular_valor_mano(["A", "A", "A", "A"]))  # 14
print("mostrar_mano   =", mostrar_mano(["A", "7", "10"]))             # A 7 10
print("resultados     =", determinar_resultado_blackjack(22, 25), determinar_resultado_blackjack(18, 23),
      determinar_resultado_blackjack(20, 18), determinar_resultado_blackjack(17, 19), determinar_resultado_blackjack(18, 18))
# Banca, Jugador, Jugador, Banca, Push
for fila in [["0", "0", "0"], ["7", "7", "7"], ["A", "A", "A"], ["A", "A", "B"], ["A", "B", "A"], ["A", "B", "C"]]:
    print(fila, "->", evaluar_fila_tragamonedas(fila))
print("ajustar_apuesta:", ajustar_apuesta(10, 100), ajustar_apuesta(50, 30))   # 10 (sin aviso) | 30 (con aviso)