while True:
    print("Seleccione la conversión que desea realizar:")
    print("1. Fahrenheit a Celsius")
    print("2. Fahrenheit a Kelvin")
    print("3. Fahrenheit a Rankine")
    print("4. Fahrenheit a Réaumur")
    print("5. Celsius a Fahrenheit")
    print("6. Celsius a Kelvin")
    print("7. Celsius a Rankine")
    print("8. Celsius a Réaumur")
    print("9. Kelvin a Celsius")
    print("10. Kelvin a Fahrenheit")
    print("11. Kelvin a Rankine")
    print("12. Kelvin a Réaumur")
    print("13. Rankine a Celsius")
    print("14. Rankine a Fahrenheit")
    print("15. Rankine a Kelvin")
    print("16. Rankine a Réaumur")
    print("17. Réaumur a Celsius")
    print("18. Réaumur a Fahrenheit")
    print("19. Réaumur a Kelvin")
    print("20. Réaumur a Rankine")
    print("21. Salir")
    
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
        celsius = (fahrenheit - 32) / 1.8
        print("Temperatura en Celsius:", celsius)
    elif opcion == 2:
        fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
        kelvin = (fahrenheit + 459.67) / 1.8
        print("Temperatura en Kelvin:", kelvin)
    elif opcion == 3:
        fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
        rankine = fahrenheit + 459.67
        print("Temperatura en Rankine:", rankine)
    elif opcion == 4:
        fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
        reaumur = (fahrenheit - 32) / 2.25
        print("Temperatura en Réaumur:", reaumur)
    elif opcion == 5:
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        fahrenheit = celsius * 1.8 + 32
        print("Temperatura en Fahrenheit:", fahrenheit)
    elif opcion == 6:
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        kelvin = celsius + 273.15
        print("Temperatura en Kelvin:", kelvin)
    elif opcion == 7:
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        rankine = (celsius * 1.8) + 32 + 459.67
        print("Temperatura en Rankine:", rankine)
    elif opcion == 8:
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        reaumur = celsius * 0.8
        print("Temperatura en Réaumur:", reaumur)
    elif opcion == 9:
        kelvin = float(input("Ingrese la temperatura en Kelvin: "))
        celsius = kelvin - 273.15
        print("Temperatura en Celsius:", celsius)
    elif opcion == 10:
        kelvin = float(input("Ingrese la temperatura en Kelvin: "))
        fahrenheit = kelvin * 1.8 - 459.67
        print("Temperatura en Fahrenheit:", fahrenheit)
    elif opcion == 11:
        kelvin = float(input("Ingrese la temperatura en Kelvin: "))
        rankine = kelvin * 1.8
        print("Temperatura en Rankine:", rankine)
    elif opcion == 12:
        kelvin = float(input("Ingrese la temperatura en Kelvin: "))
        reaumur = (kelvin - 273.15) * 0.8
        print("Temperatura en Réaumur:", reaumur)
    elif opcion == 13:
        rankine = float(input("Ingrese la temperatura en Rankine: "))
        celsius = (rankine - 32 - 459.67) / 1.8
        print("Temperatura en Celsius:", celsius)
    elif opcion == 14:
        rankine = float(input("Ingrese la temperatura en Rankine: "))
        fahrenheit = rankine - 459.67
        print("Temperatura en Fahrenheit:", fahrenheit)
    elif opcion == 15:
        rankine = float(input("Ingrese la temperatura en Rankine: "))
        kelvin = rankine / 1.8
        print("Temperatura en Kelvin:", kelvin)
    elif opcion == 16:
        rankine = float(input("Ingrese la temperatura en Rankine: "))
        reaumur = (rankine - 32 - 459.67) / 2.25
        print("Temperatura en Réaumur:", reaumur)
    elif opcion == 17:
        reaumur = float(input("Ingrese la temperatura en Réaumur: "))
        celsius = reaumur * 1.25
        print("Temperatura en Celsius:", celsius)
    elif opcion == 18:
        reaumur = float(input("Ingrese la temperatura en Réaumur: "))
        fahrenheit = reaumur * 2.25 + 32
        print("Temperatura en Fahrenheit:", fahrenheit)
    elif opcion == 19:
        reaumur = float(input("Ingrese la temperatura en Réaumur: "))
        kelvin = reaumur * 1.25 + 273.15
        print("Temperatura en Kelvin:", kelvin)
    elif opcion == 20:
        reaumur = float(input("Ingrese la temperatura en Réaumur: "))
        rankine = reaumur * 2.25 + 32 + 459.67
        print("Temperatura en Rankine:", rankine)
    elif opcion == 21:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
