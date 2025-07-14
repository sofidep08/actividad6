producto = {}
catidad = int(input("Ingrese la cantidad de productos que desea agregar: "))
for i in range(catidad):
    codigo = input(f"\nIngrese el codigo del producto{i+1}: ")
    if codigo in producto :
        print("Ese producto ya existe")
    nombre_producto = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoria del producto: ")
    talla = input("Ingrese la talla del producto: ")
    precio = int(input("Ingrese el precio del producto: "))
    if precio <= 0:
        print("Ingreso un dato incorrecto")
    else:
        cantidad_productos = int(input("Ingrese la cantidad del producto: "))
        if cantidad_productos <= 0:
            print("Ingreso un dato incorrecto")
        producto[codigo] = {
            "nombre_producto": nombre_producto,
            "categoria": categoria,
            "talla": talla,
            "precio": precio,
            "cantidad_productos": cantidad_productos
        }
opcion = int(input("Desea buscar un producto?: [1]si, [2]no"))
if opcion < 0 or opcion > 2 :
    print("Ingreso un dato incorrecto")
elif opcion == 1 :
    buscar = int(input("Ingrese el codigo del producto: "))
    if buscar in producto :
        print("Producto encontrado")
        for codigo, dato in producto.items():
            if buscar == producto["codigo"]:
                print("El producto es: ", producto["codigo"])
    else:
    print("Ese producto no exixte")
elif opcion == 2 :
    print("Saliendo del programa")