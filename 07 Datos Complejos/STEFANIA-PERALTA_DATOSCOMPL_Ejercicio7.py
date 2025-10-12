# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {"Rocio", "Stefania", "Daniel", "Ainara"}
parcial2 = {"Stefania", "Rocio", "Martín", "Pedro"}

ambos_parciales = parcial1 & parcial2   # otra opcion parcial1.intersection(parcial2)

solo_un_parcial = parcial1 ^ parcial2   # otra opcion parcial1.symmetric_difference(parcial2)

al_menos_uno = parcial1 | parcial2   # otra opcion parcial1.union(parcial2)

print("\nAprobados en ambos parciales:", ambos_parciales)
print("Aprobados solo en uno:", solo_un_parcial)
print("Aprobados en al menos uno:", al_menos_uno)