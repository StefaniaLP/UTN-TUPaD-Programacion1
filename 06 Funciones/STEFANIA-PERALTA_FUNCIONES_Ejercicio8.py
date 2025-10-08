# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc= peso/(altura*altura)
    return imc

#PROGRAMA PRINCIPAL
peso= float(input("Ingresa el PESO en KG: "))
altura = float(input("Ingresa ALTURA en Metros: "))

print(f"El Indice de masa corporal(IMC) es {round(calcular_imc(peso, altura), 2)}")


