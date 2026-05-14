productos = []
def validacion_producto(nombre, categoria,precio):
    if nombre == "" or categoria == "" or precio == "":
        print("Error: Todos los campos son obligatorios.") #return False
    return True

while True:
    print("\n" + "-" * 50 )
    print("Menú de gestión:")
    print("-" * 50 )
    print("1- Agregar")
    print("2- Mostrar")
    print("3- Buscar")
    print("4- Eliminar")
    print("5- Salir")
    
    opcion = input("Seleccione una opción (1-5): ")
    if opcion == "1":
        nombre = input("Ingrese nombre de producto: ").strip()
        categoria = input("Ingrese categoria de producto: ").strip()
        precio = input("Ingrese precio de producto: ").strip()
        if nombre !="":
            productos.append([nombre, categoria, precio])
    elif opcion == "2":
        for i in range(len(productos)):
            print(f"estos son los productos {productos[i][0]}")
    elif opcion == "3":
        ...
    elif opcion == "4":
        ...
    elif opcion == "5":
        print(productos)
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")