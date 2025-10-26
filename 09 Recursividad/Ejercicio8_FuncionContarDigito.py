# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    # Si el número tiene un solo dígito
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        ultimo = numero % 10
        # Si el ultimo digito es igual al buscado sumo 1, sino sumo 0
        contador = 1 if ultimo == digito else 0
        return contador + contar_digito(numero // 10, digito)