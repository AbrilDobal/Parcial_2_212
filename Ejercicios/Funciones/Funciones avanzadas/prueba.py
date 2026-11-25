from ejercicios import *

# 1) Edad
print("1)", calcular_edad("30/09/2026", "15/05/2000"))   # 26 (ya cumplio)
print("1)", calcular_edad("30/09/2026", "30/09/2000"))   # 26 (cumple hoy)
print("1)", calcular_edad("29/09/2026", "30/09/2000"))   # 25 (cumple manana)
print("1)", calcular_edad("30/09/2026", "01/10/2000"))   # 25 (cumple el mes que viene)
print("1)", calcular_edad("30/09/2026", "01/01/2030"))   # None (nacimiento futuro)

# 2) Patente
print("2)", identificar_tipo_vehiculo("ABC123"))   # auto
print("2)", identificar_tipo_vehiculo("123ABC"))   # moto
print("2)", identificar_tipo_vehiculo("abc123"))   # auto
print("2)", identificar_tipo_vehiculo("AB1234"))   # None
print("2)", identificar_tipo_vehiculo("ABC12"))    # None
print("2)", identificar_tipo_vehiculo("A1B2C3"))   # None

# 3) CUIL / CUIT
print("3)", generar_cuil_cuit("12345678", "MASCULINO"))   # 20-12345678-6 (ejemplo de la consigna)
print("3)", generar_cuil_cuit("12345678", "FEMENINO"))
print("3)", generar_cuil_cuit("12345678", "EMPRESA"))
print("3)", generar_cuil_cuit("1234567", "MASCULINO"))    # DNI de 7 digitos, se completa a 01234567
print("3)", generar_cuil_cuit("1234", "MASCULINO"))       # None (DNI muy corto)
print("3)", generar_cuil_cuit("12a45678", "MASCULINO"))   # None (DNI no numerico)
print("3)", generar_cuil_cuit("12345678", "OTRO"))        # None (tipo invalido)