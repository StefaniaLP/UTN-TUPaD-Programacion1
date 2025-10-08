# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

def segundos_a_horas(segundos):
    horas= segundos/3600
    return horas
    
     
#PROGRAMA PRINCIPAL
seg= input("Ingresa cantidad de segundos: ")

if seg.isdigit():
    segundos = int(seg)
    print(f"{segundos} segundos son equivalentes a {round(segundos_a_horas(segundos), 2)} horas.")
else:
    print("Error: ingresá solo números enteros, sin letras ni comas.")