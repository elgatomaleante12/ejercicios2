DESCUENTO_ESTUDIANTE = 0.15 
DESCUENTO_CLIENTE_FRECUENTE = 0.10 
DESCUENTO_PRIMERA_COMPRA = 0.05 
descuento=0.0
precio_original = float(input("ingrese el precio del descuento: $" ))
print("gracias, este es su sueldo")

print("¿que tipo de cliente es usted?")
print("1 -estudiante, -2 cliente, 3-, cliente frecuente")

cliente=input("ingrese su opcion")

if cliente=="1":
    descuento= precio_original* DESCUENTO_ESTUDIANTE
    precio_final= precio_original -descuento
    print(f"el descuento para el estudiante es {descuento} y el precio final es {precio_final}")

elif cliente=="2":
    descuento= precio_original* DESCUENTO_CLIENTE_FRECUENTE
    precio_final= precio_original -descuento
    print(f"el descuento para el estudiante es {descuento} y el precio final es {precio_final}")
else:
    print("No se aplicó descuento. El precio final es el precio original:", precio_original)