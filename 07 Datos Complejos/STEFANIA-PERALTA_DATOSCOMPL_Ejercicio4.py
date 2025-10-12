# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

agenda={}

def agregar_contacto(contacto_nombre , contacto_tel, i):
    agenda[contacto_nombre] = contacto_tel
    print(f"Contacto nº {i} agregado correctamente!!")

i=1
while i<6:
    
    nombre= input("\nIngresa nombre del contacto: ")
    tel= input("Ingresa tel del contacto: ")
    
    if tel.isdigit():
        agregar_contacto(nombre, tel, i)
        i +=1
    else: 
        print("Ingresa un telefono valido. No ingreses letras ni numeros negativos")
       

consulta = input("\nIngresa el nombre a buscar en la agenda: ")

if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Ese contacto no está en la agenda.")
