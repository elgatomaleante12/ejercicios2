def verificar_cancion(duracion, genero, anio):
 
    if not (2.5 <= duracion <= 4.5):
        return False, "La duración de la canción no está entre 2.5 y 4.5 minutos."
    
   
    genero = genero.lower() 
    if genero not in ["rock", "pop", "indie"]:
        return False, "El género de la canción no es 'rock', 'pop' o 'indie'."
    
    if anio <= 2010:
        return False, "La canción no es posterior a 2010."
    
    return True, "¡La canción cumple con todos los criterios!"

print("hola ¿que cancion te gustaria tener en tu playlist?.")

try:
    duracion = float(input("¿Cuánto dura la canción en minutos? (Ejemplo: 3.5): "))
    genero = input("¿Cuál es el género de la canción? (rock, pop, indie): ").strip()
    anio = int(input("¿En qué año se lanzó la canción? (Ejemplo: 2015): "))
    
    cumple, mensaje = verificar_cancion(duracion, genero,anio)
    
    if cumple:
        print(f"\n¡Genial! La canción SE INCLUYE en tu playlist porque:")
    else:
        print(f"\n La canción NO SE INCLUYE en tu playlist porque:")
    
    print(mensaje)

except ValueError:
    print("\nParece que hubo un problema con los datos que ingresaste. Por favor, asegúrate de usar números en duración y año.")
