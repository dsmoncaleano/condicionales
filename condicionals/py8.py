monto_cuenta = float(input("Ingrese el monto de la cuenta: "))

if monto_cuenta < 150000:
    tipo_pago = "Efectivo"
elif monto_cuenta >= 150000 and monto_cuenta <= 300000:
    tipo_pago = "Celular (dinero electrónico)"
elif monto_cuenta > 300000 and monto_cuenta <= 600000:
    tipo_pago = "Tarjeta de débito"
else:
    tipo_pago = "Tarjeta de crédito"

print("El tipo de pago a utilizar es:", tipo_pago)
