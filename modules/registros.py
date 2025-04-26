import random
from utils.file_manager_mock import get_estacionados, get_estacionamiento, get_registros, add_estacionados, add_estacionamiento, add_registros

def agregrarEstacionado():

    estacionados = get_estacionados()
    estacionamiento = get_estacionamiento()
    registros = get_registros()

    fecha = int(input("Ingrese fecha: "))
    hora = int(input("Ingrese hora: "))
    patente = (input("Ingrese patente: "))
    tipo = (input("Ingrese tipo: "))
    dni = int(input("Ingrese dni: "))
    salio = False

    if patente in estacionados:
        print("Ya ingresado.")
    else:
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
                        print(f"Vehículo {patente} ingresado en la cochera ({i},{j})")
                        return
        print("Estacionamiento lleno.")

    for i in estacionamiento:
        print(i)

    



