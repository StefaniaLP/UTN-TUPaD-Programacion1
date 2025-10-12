# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
from collections import Counter

frase = input("Ingresa una frase: ")
lista= frase.lower().split()
#print(lista)

print(Counter(lista))
