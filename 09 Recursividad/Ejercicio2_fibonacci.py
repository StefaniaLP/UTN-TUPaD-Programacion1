from Ejercicio2_FuncionFibonacci import fibonacci

posicion = int(input("Ingrese la posición hasta donde mostrar la serie fibonaci: "))

print("----- Serie de Fibonacci -----")
for i in range(posicion+1):
    print(f"Posicion {i}: {fibonacci(i)}")