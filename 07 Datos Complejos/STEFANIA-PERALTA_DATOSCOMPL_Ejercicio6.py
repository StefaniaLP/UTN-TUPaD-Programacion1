# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
alumnos={}

def agregar_alumno(nombre , notas_alumno):
    alumnos[nombre] = notas_alumno
    print(f"Alumno '{nombre}' agregado correctamente!!")

i=1
    
while i<4:
    notas=[]
    nombre= input("\nIngresa nombre del alumno: ")
    nota1= input("Ingresa primera nota del alumno: ")
    nota2= input("Ingresa segunda nota del alumno: ")
    nota3= input("Ingresa tercera nota del alumno: ")

    if nota1.isdigit() and nota2.isdigit() and nota3.isdigit():
        nota1_int = int(nota1)
        nota2_int = int(nota2)
        nota3_int = int(nota3)
        if  11> nota1_int >0 and 11> nota2_int >0 and 11> nota3_int >0:
            notas.append(nota1_int)
            notas.append(nota2_int)
            notas.append(nota3_int)
            notas_tupla = tuple(notas)
            agregar_alumno(nombre, notas_tupla)
            i +=1
        else: print ("Atencion, ingresa notas de 1 al 10")
    else: print("Ingresa una nota valida.")
    
#print (alumnos.items())
       
print("\nPromedio de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {round(promedio,2)}")