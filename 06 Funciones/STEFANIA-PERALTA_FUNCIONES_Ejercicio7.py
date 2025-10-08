# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
        
    if b != 0:
        division = a / b 
    else: 
        division="ERROR, no se puede dividir por cero"
    
    return (suma, resta, multiplicacion, division)


#PROGRAMA PRINCIPAL
a = input("Ingresa el primer numero: ")
b = input("Ingresa el segundo numero: ")

if a.isdigit() and b.isdigit():
    a_ok = int(a)
    b_ok = int(b)
    
    resultado = operaciones_basicas(a_ok, b_ok)

    print(f"Suma: {resultado[0]}")
    print(f"Resta: {resultado[1]}")
    print(f"Multiplicación: {resultado[2]}")
    print(f"División: {resultado[3]}")
    
else:
    print("Error: ingresá solo números enteros, sin letras ni comas.")

