# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
        
    
     
#PROGRAMA PRINCIPAL
num= input("Ingresa el numero para conocer su TABLA DE MULTIPLICAR: ")
print("-" * 50)

if num.isdigit():
    numero = int(num)
    tabla_multiplicar(numero)
else:
    print("Error: ingresá solo números enteros, sin letras ni comas.")