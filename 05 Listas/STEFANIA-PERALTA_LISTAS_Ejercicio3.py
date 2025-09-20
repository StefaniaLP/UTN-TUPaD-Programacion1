# # NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.
# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

#https://www.google.com/search?q=python+metodos+de+listas+random&sca_esv=c86351f7882d4df3&rlz=1C1CHBF_esAR1175AR1175&sxsrf=AE3TifPc4rt-EvGM0_m_vVIo2t0JPFRhaQ%3A1758145942491&ei=li3LaI7eHZGc1sQP19rUiAc&ved=0ahUKEwiOgfaC5OCPAxURjpUCHVctFXEQ4dUDCBA&uact=5&oq=python+metodos+de+listas+random&gs_lp=Egxnd3Mtd2l6LXNlcnAiH3B5dGhvbiBtZXRvZG9zIGRlIGxpc3RhcyByYW5kb20yBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEdIjgpQwghYwghwAngCkAEAmAEAoAEAqgEAuAEDyAEA-AEBmAIDoAIzwgIKEAAYsAMY1gQYR5gDAOIDBRIBMSBAiAYBkAYIkgcBM6AHALIHALgHAMIHBTMtMi4xyAcn&sclient=gws-wiz-serp
import random
lista_random = [random.randint(1, 100) for x in range(15)]
pares = []
impares = []

print(f"La lista generada es", lista_random)

for i in lista_random:
    if i % 2 ==0:
        pares.append(i)
    else: impares.append(i)
    
print(f"La lista de numeros pares es: ", pares, " Y contiene ", len(pares), " elementos.")
print(f"La lista de numeros impares es: ", impares, " Y contiene ", len(impares), " elementos.")
