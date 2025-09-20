#  NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.
# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha 
# (el último pasa a ser el primero).

lista = [4,16,27,38,45,51,69]
lista_rot = []

#len(lista) esto es 7
lista_rot.append(lista[len(lista)-1])
#print(lista_rot)  bien aca ya rote el ultimo como primero

for num in lista[0:6]:
    lista_rot.append(num)

print(f"La lista original es: ", lista)
print(f"La lista con rotacion es: ", lista_rot)