num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))


ascendente = sorted([num1, num2, num3])

descendente = sorted([num1, num2, num3], reverse=True)

print("Números en orden ascendente:", ascendente)
print("Números en orden descendente:", descendente)