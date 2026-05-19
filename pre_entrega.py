productos = []


def validacion_producto(nombre, categoria, precio):
    if nombre == "" or categoria == "" or precio == "":
        print("Error: Todos los campos son obligatorios.")  # return False
    return True


while True:
    print("\n" + "-" * 50)
    print("Menú de gestión:")
    print("-" * 50)
    print("1- Agregar")
    print("2- Mostrar")
    print("3- Buscar")
    print("4- Eliminar")
    print("5- Salir")

    opcion = input("Seleccione una opción (1-5): ")
    if opcion == "1":
        nombre = input("Ingrese nombre de producto: ").strip()
        if nombre == "":
            print("Error: El nombre del producto no puede estar vacío.")
            continue
        categoria = input("Ingrese categoria de producto: ").strip()
        if categoria == "":
            print("Error: La categoría del producto no puede estar vacía.")
            continue
        precio = input("Ingrese precio de producto: ").strip()
        if precio == "" or int(precio) < 0:
            print("Error: El precio del producto no puede estar vacío ni ser menor que cero.")
            continue
        if nombre != "" and categoria != "" and precio != "":
            productos.append([nombre, categoria, precio])
    elif opcion == "2":
        print("\n" + "-" * 60)
        print("Productos:")
        print("-" * 60)
        for i in range(len(productos)):
            print(f"Producto {i+1}: {productos[i][0]}, Categoría: {productos[i][1]}, Precio: {productos[i][2]}")
            print("-" * 60)
    elif opcion == "3":
        criterio = input(
            "Ingrese el criterio de búsqueda (nombre o categoría): "
        ).strip()
        if criterio == "":
            print("Error: El criterio de búsqueda no puede estar vacío.")
            continue
        encontrado = False
        for producto in productos:
            if (
                criterio.lower() in producto[0].lower()
                or criterio.lower() in producto[1].lower()
            ):
                print(
                    f"Producto encontrado: {producto[0]}, \nCategoría: {producto[1]}, \nPrecio: {producto[2]}"
                )
                encontrado = True
        if not encontrado:
            print("Producto no encontrado.")
    elif opcion == "4":
        borrar_elemento = input(
            "Ingrese el nombre exacto del producto a eliminar: "
        ).strip()
        encontrado = False
        for producto in productos:
            if borrar_elemento.lower() == producto[0].lower():
                print(
                    f"Producto a eliminar: {producto[0]}, Confirmar borrado (s/n): ",
                    end="",
                )
                confirmacion = input().strip().lower()
                if confirmacion == "n":
                    print("Eliminación cancelada.")
                elif confirmacion == "s":
                    productos.pop(productos.index(producto))
                    print(f"Producto eliminado: {producto[0]}")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
    elif opcion == "5":
        #print(productos)
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
