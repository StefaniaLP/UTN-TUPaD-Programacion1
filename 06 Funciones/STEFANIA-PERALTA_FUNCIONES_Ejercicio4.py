# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
from math import pi

def calcular_area_circulo(radio):
    area = pi *(radio**2)
    return round(area,2)

def calcular_perimetro_circulo(radio):
    perimetro= 2 * pi * radio
    return round(perimetro, 2)

#PROGRAMA PRINCIPAL
valido = False

while not valido:
    rad = input("Ingresa el radio del círculo: ")
    tiene_letra = False
    tiene_punto = 0

    # Verificar carácter por carácter
    for c in rad:
        if c.isalpha():
            tiene_letra = True
        elif c == '.':
            tiene_punto += 1
        elif not c.isdigit() and c != '.': # OTROS símbolos 
            tiene_letra = True  

    if tiene_letra or tiene_punto > 1 or len(rad) == 0:
        print("Ingrese solo números (puede ser entero o con decimal).")
    else:
        valido = True  # pasa la validación

radio = float(rad)
print(f"El area del circulo es: {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)}")   
