#  NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.
# 4) Dada una lista con valores repetidos: datos =[1,3,5,3,7,1,9,5,3]
# •  Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos = [1,3,5,3,7,1,9,5,3]

datos_sinduplicado= []

for elemento in datos:
    if elemento not in datos_sinduplicado:
        datos_sinduplicado.append(elemento)

print(f"La lista original es ", datos)
print(f"La lista sin numeros repetidos es ", datos_sinduplicado)