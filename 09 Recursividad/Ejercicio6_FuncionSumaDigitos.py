# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    
    if n<0:
        print("Ingresa un numero positivo")
    elif n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
    
#ejemplo paso a paso
#  suma_digitos(1234)
#  (1234 % 10) + suma_digitos(1234 // 10)
#  4 + suma_digitos(123)
#  4 + (3 + suma_digitos(12))
#  4 + 3 + (2 + suma_digitos(1))
#  4 + 3 + 2 + 1
#  10