# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores

paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Brasil": "Brasilia"
}

capitales_a_paises ={}
for pais, capital in paises_a_capitales.items():
    capitales_a_paises[capital] = pais


print("Diccionario original (país : capital):")
print(paises_a_capitales)

print("\nDiccionario invertido (capital : país):")
print(capitales_a_paises)