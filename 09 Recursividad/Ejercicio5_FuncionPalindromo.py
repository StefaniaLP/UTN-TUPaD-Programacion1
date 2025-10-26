# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().
#palindromo: se lee igual al derecho y al revés

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    # Si la primera y la última letra no coinciden, no es palíndromo
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
