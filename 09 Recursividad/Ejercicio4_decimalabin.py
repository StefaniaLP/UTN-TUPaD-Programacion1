from Ejercicio4_FuncionDecimalaBin import decimal_a_binario

num = int(input("Ingrese un número entero positivo: "))

if num < 0:
    print("Por favor, ingrese un número positivo.")
else:
    binario = decimal_a_binario(num)
    print(f"El número {num} en binario es: {binario}")