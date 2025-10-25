# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

lineas = [
    "Nombre,Precio,Cantidad\n",
    "Mochilas,145000.0,10\n",
    "Cartucheras,1900.0,15\n",
    "Cuaderno,1300.0,32\n"
]

with open("productos.txt", "w") as archivo:
    archivo.writelines(lineas)
    
# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    cont =0
    
    for linea in lineas:
        nombre, precio, cantidad = linea.strip().split(",")
        if cont == 0:
            print(f"{nombre} | {precio} | {cantidad}")
        else:
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
        cont +=1
        
# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.

with open("productos.txt", "a") as archivo:
    print("Ingresa un nuevo producto: ...")
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")
    archivo.write(f"{nombre},{precio},{cantidad}\n")
    
# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad

productos = []
with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    # print(f"lineas", lineas )
    
    for linea in lineas:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })
        
# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.

buscar = input("Ingrese el nombre del producto a buscar: ")
encontrado = False
for p in productos:
    # print(f"p, {p}")
    if p["nombre"].lower() == buscar.lower():
        print(f"Producto: {p["nombre"]} | Precio: ${p["precio"]} | Cantidad: {p["cantidad"]}")
        encontrado = True
        break
if not encontrado:
    print("Producto no encontrado")
    
# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.

with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p["nombre"]},{p["precio"]},{p["cantidad"]}\n")
        
        
#Solo agrego para ver como quedo finalmente. Comentar antes de entregar

# with open("productos.txt", "r") as archivo:
#     lineas = archivo.readlines()
#     cont =0
    
#     for linea in lineas:
#         nombre, precio, cantidad = linea.strip().split(",")
#         if cont == 0:
#             print("------------------------------------")
#             print(f"{nombre} | {precio} | {cantidad}")
#         else:
#             print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
#         cont +=1