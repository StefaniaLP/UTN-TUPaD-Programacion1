# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.
from datetime import datetime

agenda = {
    ('lunes', '11:00'): "Consulta medica",
    ('jueves', '15:00'): "Reunion"
}

def agregar_evento():
    dia = input("\nIngresa dia del evento (lunes a domingo): ").lower()
    hora= input("Ingresa la hora del evento (formato hh:mm): ")
    evento= input("Ingresa el nombre del evento: ")

    dias_validos = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

    if dia not in dias_validos:
        print("Día inválido. Ingresá un día de la semana válido.")
        return 
    else:
        try:
            datetime.strptime(hora, "%H:%M") 
            clave_tupla= (dia, hora)
    
            if clave_tupla in agenda: 
                print("Agenda cubierta en ese dia y horario")
            else:
                agenda[clave_tupla] = evento
                print(f"Evento cargado correctamente para el dia {dia} a las {hora}")
        except ValueError:
            print("Formato de hora inválido. Usá el formato hh:mm (Por ejemplo, 12:30).")
            return

    
        
def consultar_agenda():
    consulta_dia = input("\nCONSULTA AGENDA. Ingresa el dia a consultar: ").lower()
    consulta_hora = input("CONSULTA AGENDA. Ingresa el horario a consultar (hh:mm): ")

    dias_validos = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

    if  consulta_dia not in dias_validos:
        print("Día inválido. Ingresá un día de la semana válido.")
        return 
    else:
        try:
            datetime.strptime(consulta_hora, "%H:%M") 
            clave_tupla= (consulta_dia, consulta_hora)
            if clave_tupla in agenda :
                print(f"Dia {consulta_dia} {consulta_hora}: evento '{agenda[clave_tupla]}'")
            else:
                print("La agenda esta libre en ese dia y horario")
        except ValueError:
            print("Formato de hora inválido. Usá el formato hh:mm (Por ejemplo, 12:30).")
            return

    
def ver_eventos():
    print("\n EVENTOS REGISTRADOS:")
    if len(agenda) == 0:
        print("No hay eventos cargados.")
    else:
        for (dia, hora), evento in agenda.items():
            print(f"- {dia.title()} {hora}: {evento}")
        
while True:
    
    print("\n===== AGENDA =====")
    print("1. Agregar evento")
    print("2. Consultar agenda")
    print("3. Ver todos los eventos")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    match opcion:
        case '1': agregar_evento()
        case '2': consultar_agenda()
        case '3': ver_eventos()
        case '4': 
            print("Hasta luego!")
            break
        case _:
            print("Opción inválida. Intenta de nuevo.")
