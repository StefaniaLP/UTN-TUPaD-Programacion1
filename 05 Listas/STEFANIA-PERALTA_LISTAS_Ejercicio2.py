# # NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.
# 2) Pedir al usuario que cargue 5 productos en una lista. 
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
from functools import partial
from unicodedata import normalize

cantProd = 5
print(f"Se le va a solicitar que ingrese {cantProd} productos.")
lista = []

for i in range (0,cantProd):
   lista.append(input (f"Ingrese nombre del producto:"))
   
#https://docs.python.org/3/howto/sorting.html  para resolver ej. ['aro', 'áro', 'ñoño', 'vela', 'zeta']
lista_ord = sorted(lista, key = partial(normalize, 'NFD'))
print (f"Los productos son: ", lista_ord)

elimina= input(f"Desea eliminar algun producto? S/N :")
if(elimina == "S" or elimina == "s"):
    prod_eliminar=input(f"Que prodcuto desea eliminar?:")
    if prod_eliminar in lista_ord:
        lista_ord.remove(prod_eliminar)
    else:
        print("El producto no esta en la lista")

print (f"Los productos restantes son: ", lista_ord)