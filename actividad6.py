producto = {}
catidad = int(input("Ingrese la cantidad de productos que desea agregar"))
for i in range(catidad):
    codigo = input("Ingrese el codigo del producto: ")
    nombre_producto = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoria del producto: ")
    talla = input("Ingrese la talla del producto: ")
    precio = int(input("Ingrese el precio del producto: "))
    if precio  <= 0 :
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
