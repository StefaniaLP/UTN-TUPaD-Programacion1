# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

productos = {
    'Leche': 10,
    'Manteca': 6,
    'Yogurt': 13
}


def agregar_producto():
    nombre = input("\nIngresa nombre del producto: ")
    stock= input("Ingresa stock del producto: ")

    if nombre in productos: #para evitar que me reasigne un valor en caso de que  exista
        print("El producto ya esta ingresado")
    else:
        if stock.isdigit():
            stock_int= int(stock)
            productos[nombre] = stock_int
            print(f"Producto '{nombre}' agregado correctamente!!")


def consultar_stock():
    consulta = input("\nCONSULTA STOCK. Ingresa el nombre del producto: ")

    if consulta in productos:
        print(f"'{consulta}': stock {productos[consulta]}")
    else:
        print("Ese producto no está en la lista.")

def actualizar_stock():
    nombre = input("\nIngresa nombre del producto a actualizar: ")
    stock= input("Ingresa stock a sumar: ")
    
    if stock.isdigit():
        stock_sumar=int(stock)
        if nombre in productos:
            productos[nombre] = productos[nombre] + stock_sumar
        else: print("El producto ingresado no se encuentra")


while True:
    opcion = ""
    while opcion not in ("1", "2", "3", "4"):
        print("\n// CATALOGO DE PRODUCTOS //")
        print (productos) # ocultar 
        print("\nOpcion 1- Consultar el stock de un producto ")
        print("Opcion 2- Agregar un producto")
        print("Opcion 3- Agregar unidades a un producto")
        print("Opcion 4- Salir")

        opcion = input("Elegí opcion (1, 2, 3, 4): ").strip()
      
    match opcion:
        case '1': consultar_stock()
        case '2': agregar_producto()
        case '3': actualizar_stock()
        case '4': break
        case _:
            print("Opción inválida. Intenta de nuevo.")
