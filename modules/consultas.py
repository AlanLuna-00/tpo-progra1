from utils.file_manager_mock import get_registros
from modules.ordenamientos import selection_sort

def mostrar_registro_por_patente():
    patente = input("Ingrese la patente del vehiculo a buscar: ")

    registros = get_registros()
    encontrados = []

    for registro in registros:
        if registro.get('patente', None).lower() == patente.lower():
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
            print(f"{j.capitalize()}: {encontrados[0][j]}")
        contador = contador + 1
        print()