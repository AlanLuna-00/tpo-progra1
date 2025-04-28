from utils.file_manager_mock import get_registros
from modules.ordenamientos import selection_sort

def mostrar_registro_por_patente():
    patente = input("Ingrese la patente del vehiculo a buscar: ")

    registros = get_registros()
    encontrados = []

    for registro in registros:
        if registro['patente'].lower() == patente.lower():
            encontrados.append(registro)

    if (len(encontrados) == 0):
        print()
        print("No se encontraron registros para la patente ingresada.")
        return
    print()
    for e in encontrados[0]:
        print(f"{e.capitalize()}: {encontrados[0][e]}")

def mostrar_ranking_tipos_vehiculo():
    registros = get_registros()

    conteo_por_tipo = {}

    for registro in registros:
        tipo = registro.get("tipo_vehiculo")
        if tipo in conteo_por_tipo:
            conteo_por_tipo[tipo] += 1
        else:
            conteo_por_tipo[tipo] = 1

    ranking = []
    for tipo, cantidad in conteo_por_tipo.items():
        ranking.append((cantidad, tipo))

    ranking = selection_sort(ranking, ascendente=False)

    for cantidad, tipo in ranking:
        print(f"{tipo}: {cantidad} ingresos")


def mostrarTodosLosRegistros():
    print()
    db = get_registros()
    encontrados = []
    contador = 0

    for i in db:
        encontrados.append(i)
    
    while contador < len(encontrados):
        for j in encontrados[contador]:
            if j.lower() == "patente":
                patente = encontrados[contador][j]
                if len(patente) == 6:
                    patente_formateada = patente[:3] + "-" + patente[3:]
                    print(f"{j.capitalize()}: {patente_formateada}")
                elif len(patente) == 7:
                    patente_formateada = patente[:2] + "-" + patente[2:5] + "-" + patente[5:]
                    print(f"{j.capitalize()}: {patente_formateada}")
                else:
                    print(f"{j.capitalize()}: {patente}")
            else:
                print(f"{j.capitalize()}: {encontrados[contador][j]}")
        contador = contador + 1
        print()


def filtrar_por_tipo_vehiculo():
    registros = get_registros()
    tipos_disponibles = set(registro["tipo_vehiculo"] for registro in registros)
    
    print("\nTipos de vehículos disponibles:", ", ".join(tipos_disponibles))
    tipo_buscado = input("Ingrese el tipo de vehículo a filtrar: ").strip().lower()
    
    encontrados = [
        registro for registro in registros 
        if registro["tipo_vehiculo"].lower() == tipo_buscado
    ]
    
    if not encontrados:
        print(f"No hay registros para el tipo '{tipo_buscado}'.")
        return
    
    print(f"\n→ Registros de tipo '{tipo_buscado}':")
    for registro in encontrados:
        for campo, valor in registro.items():
            print(f"{campo.capitalize()}: {valor}")
        print("------")


def mostrarPorDni():
    registros = get_registros()
    encontrados = []
    dniBuscado = (input("Ingresa el dni para filtrar: "))

    for registro in registros:
        if registro['cliente_dni'] == dniBuscado:
            encontrados.append(registro)

    for j in range(len(encontrados)):
        print()
        for k in encontrados[j]:
            print(f"{k.capitalize()}: {encontrados[0][k]}")





