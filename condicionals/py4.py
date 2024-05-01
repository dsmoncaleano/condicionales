numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))
 

if numero1 > numero2:
    mayor = numero1
    menor = numero2
elif numero2 > numero1:
    mayor = numero2
    menor = numero1
else:
    print("Los dos números son iguales.")
    exit()

print("El número", mayor, "es mayor que", menor)
print("El número", menor, "es menor que", mayor)p