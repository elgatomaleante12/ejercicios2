print("Conversor de Unidades")
print("1. Kilómetros a Millas")
print("2. Millas a Kilómetros")
print("3. Celsius a Fahrenheit")
print("4. Fahrenheit a Celsius")

opcion = int(input("\nSeleccione una opción (1-4): "))


if opcion == 1:
    valor = float(input("Ingrese la distancia en kilómetros: "))
    if valor < 0:
        print("Error: La distancia no puede ser negativa.")
    else:
        resultado = valor * 0.621371
        print(f"{valor} kilómetros equivalen a {resultado:.2f} millas.")


elif opcion == 2:
    valor = float(input("Ingrese la distancia en millas: "))
    if valor < 0:
        print("Error: La distancia no puede ser negativa.")
    else:
        resultado = valor / 0.621371
        print(f"{valor} millas equivalen a {resultado:.2f} kilómetros.")


elif opcion == 3:
    valor = float(input("Ingrese la temperatura en grados Celsius: "))
    resultado = valor * 9/5 + 32
    print(f"{valor}°C equivalen a {resultado:.1f}°F.")


    if valor < 0:
        print("Está bajo cero, ¡qué frío!")
    elif 15 <= valor <= 25:
        print("Está a temperatura ambiente, muy agradable.")
    else:
        print("Hace calor.")


elif opcion == 4:
    valor = float
