# 8)Crear una matriz con las notas de 5 estudiantes en 3 materias.
# •Mostrar el promedio de cada estudiante.
# •Mostrar el promedio de cada materia.

notasEstudiantes = [   # [NombreEstudiante , notaProgramacion, notaMatematica , notaArquitectura ]
    ["Jose", 10, 7, 5],
    ["Mariela", 6, 8, 6],
    ["Daniel", 9, 7.5 , 8.5], 
    ["Eduardo", 8.5, 4.5, 5], 
    ["Stefania", 10, 10, 10]
]

suma=0
sumaProgra = 0
sumaMate = 0
sumaArqui = 0
sumaEstudiante = 0

for est in notasEstudiantes:
    sumaProgra = sumaProgra + est[1]
    sumaMate = sumaMate + est[2]
    sumaArqui = sumaArqui + est[3]
    sumaEstudiante = 0
    for e in est[1:]:
       sumaEstudiante= sumaEstudiante + e
    
    print (f"El promedio del estudiante ", est[0], " es:", sumaEstudiante/(len(est) - 1))
       

print (f"El promedio de la materia Programacion es:", sumaProgra/ len(notasEstudiantes))
print (f"El promedio de la materia Matematica es:", sumaMate/ len(notasEstudiantes))
print (f"El promedio de la materia Arquitectura es:", sumaArqui/ len(notasEstudiantes))