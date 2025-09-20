# 9)Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# •Inicializarlo con guiones "-" representando casillas vacías.
# •Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# •Mostrar el tablero después de cada jugada.

tateti = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

# tateti = [
#     ["f1c1","f1c2","f1c3"]
#     ["f2c1","f2c2","f2c3"]
#     ["f3c1","f3c2","f3c3"]
# ]

fila =0
columna=0
jugada= "X"

print ("JUGAREMOS AL TA - TE - TI")
#se permitira ingresar hasta 9 elementos
for turno in range(9):
    fila = int(input ("Ingrese numero de fila donde va a seleccionar (1-3):... "))
    columna = int(input ("Ingrese numero de columna donde va a seleccionar (1-3): ..."))
    if tateti[fila-1][columna-1] == "-":
        tateti[fila-1][columna-1] = jugada
         #cambio el jugador
        if jugada == "X":
            jugada = "O"
        else:
            jugada = "X"
    else: print("Casilla ocupada, elija otra.")
    
   
    
    #muestro tateti
    for x in tateti:
        print(" ".join(x))
    print("") 
        