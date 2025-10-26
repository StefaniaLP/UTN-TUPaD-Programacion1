from Ejercicio5_FuncionPalindromo import es_palindromo

texto = input("Ingrese una palabra (sin espacios ni tildes): ").strip().lower()

if es_palindromo(texto):
    print("Es un palindromo")
else:
    print("No es un palindromo")