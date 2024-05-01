numero_llantas = int(input("Ingrese el número de llantas compradas: "))
p
if numero_llantas < 6:
    precio_unitario = 240000
elif numero_llantas >= 6 and numero_llantas <= 7:
    precio_unitario = 221000
else:
    precio_unitario = 180000

total_a_pagar = numero_llantas * precio_unitario

print("El total a pagar es: $", total_a_pagar)
