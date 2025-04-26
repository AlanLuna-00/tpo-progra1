import random
from utils.file_manager_mock import get_estacionamiento, get_registros, add_estacionados, add_estacionamiento, add_registros
from datetime import datetime
from data.data import estacionados

def agregrarEstacionado():

    estacionamiento = get_estacionamiento()
    registros = get_registros()

    
    patente = (input("Ingrese patente: ")).upper()
    if patente in estacionados:
        print("Ya ingresado.")
    else:
        fecha = datetime.now().strftime("%d/%m/%Y")
        hora = datetime.now().strftime("%H:%M")
        tipo = (input("Ingrese tipo: ")).capitalize()
        dni = (input("Ingrese dni: "))
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

    estacionamiento = get_estacionamiento()
    registros = get_registros()

    patenteEgresada = input("Ingrese la patente del vehiculo a egresar: ").upper()
    if patenteEgresada not in estacionados:
        print("El vehiculo no esta estacionado.")
    else:
        fecha = datetime.now().strftime("%d/%m/%Y")
        hora = datetime.now().strftime("%H:%M")
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
                        print("Exitoso.")
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

