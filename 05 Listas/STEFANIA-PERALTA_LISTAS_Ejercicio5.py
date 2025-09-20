#  NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.
# 5)Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ["Ainara", "Veronica", "Daniel", "Stefania", "Sharon", "Adrian", "Ruben", "Emanuel"]
estudianteEliminado = ""
estudianteAgregado = ""

print("Los estudiantes de la clase son: ", estudiantes)
print("--------------------------------------------------------------------------------------------")
print("¿Desea agregar un nuevo estudiante o eliminar algun estudiante existente?")
print(".................... MENU .......................")
print("`A´ : si queres agregar")
print("`E´ : si queres eliminar")
print("Cualquier otra letra para salir del menu")

opcion= input(f"Ingresa tu opcion...")

if(opcion == "E" or opcion == "e"):
    estudianteEliminado=input(f"Que estudiante desea eliminar?:")
    if estudianteEliminado in estudiantes:
        estudiantes.remove(estudianteEliminado)
    else:
        print("El estudiante ingresado no esta en la lista")
elif (opcion == "A" or opcion == "a"):
    estudianteAgregado=input(f"Que estudiante desea agregar?:")
    estudiantes.append(estudianteAgregado)

print("--------------------------------------------------------------------------------------------")
print("Los estudiantes finales son: ", estudiantes)
