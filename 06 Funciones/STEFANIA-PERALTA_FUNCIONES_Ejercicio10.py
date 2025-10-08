# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    suma = a + b + c
    promedio = suma /3
    return round(promedio,2)

#PROGRAMA PRINCIPAL
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
c = float(input("Ingresa el tercer numero: "))
print(f"El promedio de los 3 numeros es {calcular_promedio(a, b, c)}")