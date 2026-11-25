# Abril Dobal
# ===================== FACTURACIÓN SERVICIO DE AGUA POTABLE =====================

# 1. Pedimos los datos al usuario.
# 2. Calculamos el subtotal de consumo.
# 3. Aplicamos bonificaciones o recargos según tipo de cliente y consumo.
# 4. Aplicamos el descuento especial si corresponde.
# 5. Aplicamos el IVA y calculamos el total final.
# 6. Mostramos el desglose completo.

CARGO_FIJO = 7000
COSTO_M3 = 200
IVA = 0.21

metros_consumidos = float(input("Ingrese la cantidad de metros cúbicos consumidos: "))
tipo_cliente = input("Ingrese el tipo de cliente (Residencial / Comercial / Industrial): ")

subtotal_consumo = metros_consumidos * COSTO_M3

# "Total sin impuestos ni bonificaciones": cargo fijo + consumo, antes de aplicar nada más.
subtotal_sin_bonif = CARGO_FIJO + subtotal_consumo

bonificacion = 0
recargo = 0

match tipo_cliente:
    case "Residencial":
        if metros_consumidos < 30:
            bonificacion = subtotal_consumo * 0.10
        elif metros_consumidos > 80:
            recargo = subtotal_consumo * 0.15
    case "Comercial":
        if metros_consumidos > 300:
            bonificacion = subtotal_consumo * 0.12
        elif metros_consumidos > 150:
            bonificacion = subtotal_consumo * 0.08
        elif metros_consumidos < 50:
            recargo = subtotal_consumo * 0.05
    case "Industrial":
        if metros_consumidos > 1000:
            bonificacion = subtotal_consumo * 0.30
        elif metros_consumidos > 500:
            bonificacion = subtotal_consumo * 0.20
        elif metros_consumidos < 200:
            recargo = subtotal_consumo * 0.10
    case _:  # Caso por defecto (default), debe ir como último caso.
        print("Error, tipo de cliente inválido.")

# Subtotal ya con recargos y bonificaciones aplicadas.
subtotal_con_ajustes = subtotal_sin_bonif + recargo - bonificacion

# Caso especial: descuento adicional del 5% para Residencial si la factura
# sin impuestos ni bonificaciones (cargo fijo + consumo) es menor a $35000.
descuento_especial = 0
if tipo_cliente == "Residencial" and subtotal_sin_bonif < 35000:
    descuento_especial = subtotal_con_ajustes * 0.05

subtotal_final = subtotal_con_ajustes - descuento_especial

monto_iva = subtotal_final * IVA

total_a_pagar = subtotal_final + monto_iva

# ===================== DESGLOSE =====================
print("\n----- DESGLOSE DE FACTURACIÓN -----")
print(f"Cargo fijo: ${CARGO_FIJO}")
print(f"Consumo: {metros_consumidos} x ${COSTO_M3} = ${subtotal_consumo}")
print(f"Subtotal sin impuestos ni bonificaciones: ${subtotal_sin_bonif}")
print(f"Bonificación aplicada: ${bonificacion}")
print(f"Recargo aplicado: ${recargo}")
print(f"Descuento especial (Residencial): ${descuento_especial}")
print(f"Subtotal final (antes de IVA): ${subtotal_final}")
print(f"IVA (21%): ${monto_iva}")
print(f"TOTAL A PAGAR: ${total_a_pagar}")