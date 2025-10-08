# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
   fahrenheit = (celsius * (9/5)) + 32
   return fahrenheit

#PROGRAMA PRINCIPAL
grados_C = float(input("Ingresa los grados Celcius: "))
print(f"El equivalente de {grados_C} Cº es {round(celsius_a_fahrenheit(grados_C), 2)} fahrenheit")