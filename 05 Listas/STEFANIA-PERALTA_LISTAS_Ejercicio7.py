# 7)Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# •Calcular el promedio de las mínimas y el de las máximas.
# •Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [ 
    [4,12], #8
    [8,24], #16
    [12,26], #14 
    [11,19], #8
    [15,28], #13
    [14,40], #26
    [15,20] #5
]

sumaMin = 0
sumaMax = 0
diaMayorAmplitud = 0
mayorAmplitud = 0
amplitud = 0

for temp in temperaturas:
    sumaMin = sumaMin + temp[0] #aca entraria a la temp 4 en la primer vuelta
    sumaMax = sumaMax + temp[1] #aca entraria a la temp 12 en la primer vuelta
    
    amplitud = temp[1] -temp[0]
    if amplitud > mayorAmplitud:
        mayorAmplitud = amplitud
        diaMayorAmplitud = temperaturas.index(temp)+1
    
print (f"El promedio de las temperaturas minimas es: ", sumaMin / len(temperaturas))
print (f"El promedio de las temperaturas maximas es: ", sumaMax / len(temperaturas))
print (f"El dia con mayor amplitud es el dia: ", diaMayorAmplitud)
print (f"La mayor amplitud registrada fue: ", mayorAmplitud)