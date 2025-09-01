# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for num in range (101):
    print (num)
    
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene.

num = int(input("Ingrese un numero entero: "))

cant = len(str(num))
print(f"El numero contiene ",cant," digitos")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un numero entero "))
num2 = int(input("Ingrese otro numero entero "))
sumatoria = 0

if num1 < num2:
    menor = num1
    mayor = num2
else:
    menor = num2
    mayor= num1

for x in range (menor+1, mayor):  
    sumatoria = sumatoria + x
print(f"La suma de los números enteros entre", menor, " y ", mayor ," excluyendo ambos, es:", sumatoria)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0.
DETENERSE = 0
sumatoria = 0

while True:
    num = int(input("Ingresa un numero entero para sumar: "))
    if (num >= 0):
        sumatoria += num
        if num == DETENERSE:
            break
    elif num <0:
        print ("Los numeros que debes ingresar son enteros")

print (f"la Sumatoria de los numeros es ", sumatoria)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random
numeroSecreto = random.randint(0, 9)
noAdivina = True
cont= 0

while noAdivina == True:
    numero = int(input("Ingresa el numero a adivinar: "))
    cont += 1
    if numero == numeroSecreto:
        noAdivina = False # Significa que ya lo adivino
        print (f"ADIVINASTE!!! El numero era ", numeroSecreto , "y lo adivinaste en ", cont , " intentos")
    else:
        print("No era el numero secreto, intenta de nuevo")  
        
        
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.

for i in range (100,-1,-2):
    print (i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.

num1 = int(input("Ingrese un numero entero positivo"))
sumatoria = 0

if (num1 >= 0):
    for x in range (num1+1):  
        sumatoria = sumatoria + x
    print(f"La suma de los números enteros entre 0 y ", num1 ," es:", sumatoria)
else:
    print ("El numero ingresado no es un entero positivo")
    
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
negativos = 0
positivos = 0

# Aca se ingresan la cantidad de numeros que se van a evaluar
cantNumeros = 10
print(f"Se le va a solicitar que ingrese {cantNumeros} numeros.")

for i in range (1,cantNumeros+1):
    num = int(input (f"Ingrese un numero: "))
    if (num>=0):
        positivos +=1
    else:
        negativos += 1
    if (num%2==0):
        pares +=1
    else:
        impares += 1
print(f"Se ingresaron {cantNumeros} numeros. De este listado: ")
print(f"{positivos} son positivos ")
print(f"{negativos} son negativos ")
print(f"{pares} son pares ")
print(f"{impares} son impares ")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).

# Aca se ingresan la cantidad de numeros que se van a evaluar
cantNumeros = 10
print(f"Se le va a solicitar que ingrese {cantNumeros} numeros.")

sumatoria = 0
cont = 0
for i in range (1,cantNumeros+1):
    num = int(input (f"Ingrese un numero: "))
    sumatoria = sumatoria + num
    cont += 1
print(f"La media de estos valores es: ", sumatoria / cont)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingresa un número entero: ")
invertido = numero[::-1]
print(f"El numero ingresado es {numero} y su invertido es {invertido}")