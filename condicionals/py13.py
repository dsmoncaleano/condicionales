peso = float(input("Ingrese su peso en Kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

imc = peso / (estatura * estatura)

if imc < 18.5:
    estado = "Desnutrido"
elif 18.5 <= imc < 25:
    estado = "Normal"
elif 25 <= imc < 30:
    estado = "Sobrepeso"
elif 30 <= imc < 35:
    estado = "Obesidad Grado 1"
elif 35 <= imc < 40:
    estado = "Obesidad Grado 2"
elif 40 <= imc < 50:
    estado = "Obesidad Grado 3"
else:
    estado = "Obesidad Grado 4"
print("Su estado de salud según el IMC es:", estado)