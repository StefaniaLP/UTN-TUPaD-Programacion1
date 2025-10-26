from Ejercicio8_FuncionContarDigito import contar_digito

num= int(input("Ingresa un numero: "))
digito= int(input("Ingresa un digito (0-9): "))
print(f"El digito ingresado se repite {contar_digito(num,digito)} veces en el numero {num}")