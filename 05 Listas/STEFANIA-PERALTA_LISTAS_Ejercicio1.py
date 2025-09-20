# NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.
# 1) Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa. 
# • Calcular y mostrar el promedio. 
# • Indicar la nota más alta y la más baja.

notas = [5,7,8,2,5.6,8.9,9.5,10,6,7]

suma=0
nota_max = notas[0]
nota_min = notas[0]

for nota in notas:
    suma=suma+nota
    
    if nota > nota_max:
        nota_max = nota
    if nota < nota_min:
        nota_min = nota
    
    # No se si cuando pide mostrar la lista completa debo mostrarla asi o si debo mostrarla 
    # con formato de lista es decir:  print (f"Las notas son: ", notas), pero fuera del for. 
    # Dejo la aclaracion hasta consultar. 
    print (f"Las notas son: ", nota) 
     

promedio = suma/len(notas)
print(f"El promedio de las notas es ", promedio )
print(f"La nota mas alta es ", nota_max )
print(f"La nota mas baja es ", nota_min )