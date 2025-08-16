# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 
print("Hola Mundo")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla.

nombre = input("Ingresa tu nombre")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
# la impresión por pantalla.

nombre = input("Ingresa tu nombre")
apellido = input("Ingresa tu apellido")
edad = int(input("Ingresa tu edad"))
lugarDeResidencia = input("Ingresa tu lugar de residencia")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarDeResidencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro. 

radio = int(input("Ingresa el radio del circulo"))
pi= 3.14
area= pi * (radio ** 2)
perimetro= 2 * pi * radio
print (f"El area del circulo es {area} y el perimetro es {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
# cuántas horas equivale.

segundos = int(input("Ingresa cantidad de segundos"))
minutos = segundos/60
horas = minutos/60
print (f"La cantidad de segundos ingresada corresponde a {horas} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.  

numero = int(input("Ingresa un numero"))
print (f"{numero} x 1 = {numero*1}")
print (f"{numero} x 2 = {numero*2}")
print (f"{numero} x 3 = {numero*3}")
print (f"{numero} x 4 = {numero*4}")
print (f"{numero} x 5 = {numero*5}")
print (f"{numero} x 6 = {numero*6}")
print (f"{numero} x 7 = {numero*7}")
print (f"{numero} x 8 = {numero*8}")
print (f"{numero} x 9 = {numero*9}")
print (f"{numero} x 10 = {numero*10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Ingresa un numero distinto de 0 (cero)"))
numero2 = int(input("Ingresa otro numero distinto de 0 (cero)"))
print (f"{numero1} + {numero2} = {numero1 + numero2}")
print (f"{numero1} / {numero2} = {numero1 / numero2}")
print (f"{numero1} * {numero2} = {numero1 * numero2}")
print (f"{numero1} - {numero2} = {numero1 - numero2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
# modo:  
# I𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)**2

altura = float(input("Ingresa tu altura (en metros)"))
peso = float(input("Ingresa tu peso (en kg)"))
imc= peso / (altura ** 2)
print (f"El indice de masa corporal (IMC) es {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
# Te𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/ 5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠   + 32

gradosCelsius= float(input("Ingresa la temperatura en Cº"))
gradosFar= (9/5)*gradosCelsius+32
print(f"El equivalente de esta temperatura en Fahrenheit es {gradosFar}")

#  10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
# dichos números. 

numero1 = int(input("Ingresa un numero "))
numero2 = int(input("Ingresa otro numero"))
numero3 = int(input("Ingresa el tercer numero"))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de dichos numeros es {promedio}")