from data.data import estacionamiento,registros, estacionados
import random

def agregrarEstacionado():

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
            estacionados.append(patente)

            registros. append({
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
                        estacionamiento[i][j] = patente            
                        print(f"Vehículo {patente} ingresado en la cochera ({i},{j})")
                        return
        print("Estacionamiento lleno.")

    for i in estacionamiento:
        print(i)

    



