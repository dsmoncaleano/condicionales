cantidad_articulos = int(input("Ingrese la cantidad de artículos comprados: "))
precio_unitario_original = float(input("Ingrese el precio unitario original: "))

if cantidad_articulos <= 5:
    descuento = 0
elif cantidad_articulos < 10:
    descuento = 0.05  # 5% de descuento
else:
    descuento = 0.08  # 8% de descuento

precio_unitario_descuento = precio_unitario_original * (1 - descuento)

precio_total = cantidad_articulos * precio_unitario_descuento

print("El precio total a pagar es: $", precio_total)
