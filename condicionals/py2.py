nombre = (input(" digite su nombre: "))
edad = int (input("ingrese su edad"))
if edad >= 100:
        print ("edad invalida")
elif edad < 0:
        print ("edad invalida")
 
if edad >= 18 and edad < 100:
    print ("usted es mayor de edad")
elif edad < 18 and edad > 0:
    print ("usted es menor de edad")