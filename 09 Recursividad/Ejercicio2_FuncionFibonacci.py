# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)