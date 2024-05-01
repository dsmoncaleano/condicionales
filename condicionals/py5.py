nota1= float(input("ingresa una nota de 0.0 a 5: "))
nota2= float(input("ingresa una nota de 0.0 a 5: "))
nota3= float(input("ingresa una nota de 0.0 a 5: "))
nota4= float(input("ingresa una nota de 0.0 a 5: "))
nota5= float(input("ingresa una nota de 0.0 a 5: "))

promedio= (nota1+nota2+nota3+nota4+nota5) / 5

if promedio >= 3.0:
    print("el estidiante aprobo con un promedio de:",promedio)
else:
     print("el estidiante no aprobo con un promedio de:",promedio)p