import random
from utils.file_manager_mock import get_estacionamiento, get_registros, add_estacionados, add_estacionamiento, add_registros
from datetime import datetime
from data.data import estacionados

def agregrarEstacionado():
    """
    Registra el ingreso de un vehículo en el estacionamiento.

        1) Obtiene la estructura de estacionamiento y los registros existentes.
        2) Solicita la patente del vehículo y verifica si ya está registrado.
        3) Solicita más datos al usuario, como tipo de vehículo y DNI del cliente.
        4) Guarda la fecha y hora del ingreso usando datetime.now().
        5) Busca una cochera disponible y registra el vehículo en la primera vacía que encuentre.
        6) Actualiza los datos en file_manager_mock.py
        7) Muestra la disposición del estacionamiento tras la asignación.

    Si no hay espacios vacíos, informa que el estacionamiento está lleno.
    """
    try:
        estacionamiento = get_estacionamiento()
    except Exception as e:
        print(f"Error al obtener los datos del estacionamiento: {e}")

    try:
        registros = get_registros()
    except Exception as e:
        print(f"Error al obtener los registros: {e}")


    patente = input("Ingrese la patente: ")
    while not patente:
        print("La patente no puede estar vacía.")
        patente = input("Ingrese la patente: ")

    
    if patente in estacionados:
        print("Ya ingresado.")
    else:
        fecha = datetime.now().strftime("%d/%m/%Y")
        hora = datetime.now().strftime("%H:%M")
        tipo = (input("Ingrese tipo: ")).capitalize()

        while not tipo:
            print("El tipo de vehiculo no puede estar vacío.")
            tipo = input("Ingrese el tipo de vehiculo: ")
        dni = (input("Ingrese dni: "))

        while not dni:
            print("El DNI no puede estar vacío.")
            dni = input("Ingrese el DNI: ")

        salio = False
        while patente not in estacionados:
            add_estacionados(patente)
            add_registros({
                "fecha": fecha,
                "hora": hora,
                "patente": patente,
                "tipo_vehiculo": tipo,
                "cliente_dni": dni,
                "salio": salio,
            })
            for i in range(len(estacionamiento)):
                for j in range(len(estacionamiento[i])):
                    if estacionamiento[i][j] == 'Vacio':
                        add_estacionamiento(i,j,patente)
                        print()
                        print(f"Vehículo {patente} ingresado en la cochera ({i+1},{j+1})")
                        print()
                        for fila in estacionamiento:
                            for lugar in fila:
                                print(lugar, end=" ")
                            print()
                        return
        print("Estacionamiento lleno.")

    for fila in estacionamiento:
        for lugar in fila:
            print(lugar, end=" ")
        print()


def egresarVehiculo():
    """
    Registra la salida de un vehículo del estacionamiento.

        1) Solicita la patente del vehículo a egresar.
        2) Verifica si el vehículo está en el estacionamiento.
        3) Solicita el DNI del cliente y comprueba que coincida con el registro.
        4) Si es válido, actualiza el registro marcando el vehículo como egresado (salio = True).
        5) Libera la cochera cambiando su estado a 'Vacio'.
        6) Muestra la disposición actualizada del estacionamiento.

    Si el DNI no coincide, el egreso no se permite.
    """

    try:
        estacionamiento = get_estacionamiento()
    except Exception as e:
        print(f"Error al obtener los datos del estacionamiento: {e}")

    try:
        registros = get_registros()
    except Exception as e:
        print(f"Error al obtener los registros: {e}")

    patenteEgresada = input("Ingrese la patente del vehiculo a egresar: ").upper()
    while not patenteEgresada:
        print("Ingrese una patente valida: ")
        patenteEgresada = input("Ingrese la patente del vehiculo a egresar: ").upper()
    
    if patenteEgresada not in estacionados:
        print("El vehiculo no esta estacionado.")
    else:
        fecha = datetime.now().strftime("%d/%m/%Y")
        hora = datetime.now().strftime("%H:%M")
        dni = input("Ingrese el dni: ")

        while not dni:
            print("Ingrese un numero de DNI valido.")
            dni = input("Ingrese el dni: ")

        while patenteEgresada in estacionados:
            estacionados.remove(patenteEgresada)
            for registro in registros:
                if registro["patente"] == patenteEgresada and registro["salio"] == False:
                    if registro["cliente_dni"] == dni:
                        nuevo_registro = {
                        "fecha": fecha,
                        "hora": hora,
                        "patente": patenteEgresada,
                        "tipo_vehiculo": registro["tipo_vehiculo"],  
                        "cliente_dni": dni,
                        "salio": True
                        }
                        add_registros(nuevo_registro)
                    else:
                        print("El dni no coincide.")
                        return

            for i in range(len(estacionamiento)):
                for j in range(len(estacionamiento[i])):
                    if estacionamiento[i][j] == patenteEgresada:
                        add_estacionamiento(i,j,"Vacio")
                        print()
                        print(f"Vehículo {patenteEgresada} salio de la cochera ({i+1},{j+1})")
                        print()
                        for fila in estacionamiento:
                            for lugar in fila:
                                print(lugar, end=" ")
                            print()
                        return

    for fila in estacionamiento:
        for lugar in fila:
            print(lugar, end=" ")
        print()
