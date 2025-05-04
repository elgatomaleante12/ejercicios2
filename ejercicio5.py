biblioteca = ["Papelucho", "hit", "El principito", "Harry Potter", "1984"]

print("Biblioteca Digital")
print("1. Ver todos los libros")
print("2. Buscar un libro")
print("3. Agregar un libro")
print("4. Eliminar un libro")

try:
    opcion = int(input("\nSeleccione una opción (1-4): "))

    if opcion == 1:
        if len(biblioteca) == 0:
            print("La biblioteca está vacía.")
        else:
            print("\nLibros disponibles:")
            for i, libro in enumerate(biblioteca, 1):
                print(f"{i}. {libro}")

    elif opcion == 2:
        busqueda = input("Ingrese el nombre del libro a buscar: ")
        encontrado = False
        for libro in biblioteca:
            if busqueda.lower() in libro.lower():
                print(f"Libro encontrado: {libro}")
                encontrado = True
        if not encontrado:
            print("No se encontró ningún libro con ese nombre.")

    elif opcion == 3:
        nuevo_libro = input("Ingrese el nombre del nuevo libro: ")
        if any(libro.lower() == nuevo_libro.lower() for libro in biblioteca):
            print("Este libro ya existe en la biblioteca.")
        else:
            biblioteca.append(nuevo_libro)
            print(f"'{nuevo_libro}' ha sido agregado a la biblioteca.")
        
        if len(biblioteca) > 10:
            print("¡Atención! Has alcanzado el límite de 10 libros de la versión gratuita.")

    elif opcion == 4:
        if len(biblioteca) == 0:
            print("La biblioteca está vacía, no hay libros para eliminar.")
        else:
            print("\nLibros disponibles:")
            for i, libro in enumerate(biblioteca, 1):
                print(f"{i}. {libro}")
            
            try:
                indice = int(input("\nIngrese el número del libro a eliminar: ")) - 1
                if 0 <= indice < len(biblioteca):
                    libro_eliminado = biblioteca.pop(indice)
                    print(f"'{libro_eliminado}' ha sido eliminado de la biblioteca.")
                else:
                    print("Número de libro inválido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    else:
        print("Opción no válida. Por favor seleccione un número del 1 al 4.")

except ValueError:
    print("Por favor, ingrese un número válido para seleccionar la opción.")

