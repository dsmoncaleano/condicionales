precios = {
    1: 15000,
    2: 24000,
    3: 36000
}

tamaño_pizza = int(input("Ingrese el tamaño de la pizza (1, 2 o 3): "))
ingredientes_adicionales = int(input("Ingrese el número de ingredientes adicionales: "))

precio_base = precios.get(tamaño_pizza)
precio_total = precio_base + (ingredientes_adicionales * 4000)


print("El precio a pagar por la pizza es: $", precio_total)
