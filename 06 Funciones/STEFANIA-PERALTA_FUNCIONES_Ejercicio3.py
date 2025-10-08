# Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

#PROGRAMA PRINCIPAL
apellido= input("Ingresa tu apellido: ")
nombre= input("Ingresa tu nombre: ")
edad= input("Ingresa tu edad: ")
residencia= input("Ingresa tu residencia: ")
print(informacion_personal(nombre, apellido, edad, residencia))