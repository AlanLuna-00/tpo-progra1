from utils.file_manager_mock import get_registros, get_estacionamiento
from modules.ordenamientos import selection_sort


def mostrar_registro_por_patente():
    """
    Esta funcion busca registros de vehículos por número de patente.

        1) Solicita al usuario la patente del vehículo que quiere buscar.
        2) Recupera todos los registros desde get_registros().
        3) Compara las patentes con lo ingresado y guarda coincidencias en encontrados[].
        4) Si hay registros, imprime los datos, sino, avisa que no hay información disponible.
    """
    
    patente = input("Ingrese la patente del vehiculo a buscar: ")

    try:
        registros = get_registros()
    except Exception as e:
        print(f"Error al obtener los registros: {e}")
        return
    encontrados = []

    for registro in registros:
        if registro['patente'].lower() == patente.lower():
            encontrados.append(registro)

    if len(encontrados) == 0:
        print()
        print("No se encontraron registros para la patente ingresada.")
        return
    print()
    for registro in encontrados:
        for campo, valor in registro.items():
            print(f"{campo.capitalize()}: {valor}")
        print("------")


def mostrar_ranking_tipos_vehiculo():
    """
    Cuenta cuántos vehículos de cada tipo han ingresado al estacionamiento y los ordena.

        1)Obtiene registros de estacionamiento.
        2) Agrupa vehículos por tipo en conteo_por_tipo (ejemplo: "Camioneta", "Moto").
        3) Ordena los resultados con selection_sort(), de mayor a menor.
        4) Muestra el ranking de tipos de vehículos según su cantidad de ingresos.
    """

    try:
        registros = get_registros()
    except Exception as e:
        print(f"Error al obtener los registros: {e}")
        return

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

    if len(ranking) == 0:
        print("No hay registros disponibles.")
        return

    ranking = selection_sort(ranking, ascendente=False)

    for cantidad, tipo in ranking:
        print(f"{tipo}: {cantidad} ingresos")


def mostrarTodosLosRegistros():
    """
    Imprime todos los registros disponibles

        1) Carga todos los registros desde la base de datos.
        2) Recorre los registros y los imprime en pantalla.
    """

    print()
    try:
        db = get_registros()
    except Exception as e:
        print(f"Error al obtener los registros: {e}")
        return
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
    """
    Permite buscar vehículos según su tipo (auto, moto, camioneta, etc.)

        1) Lista los tipos de vehículos disponibles según los registros.
        2) Solicita al usuario que ingrese el tipo de vehículo que quiere filtrar.
        3) Busca coincidencias y las imprime.
    """

    try:
        registros = get_registros()
    except Exception as e:
        print(f"Error al obtener los registros: {e}")
        return
    
    tipos_disponibles = set(registro["tipo_vehiculo"] for registro in registros)
    if not tipos_disponibles:
        print("No hay vehiculos cargados aun.")
        return

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
    """
    Muestra todos los registros asociados a un número de DNI.

        1) Recupera la lista de registros almacenados.
        2) Solicita al usuario un DNI para filtrar.
        3) Busca coincidencias y muestra los datos del cliente.
    """
    try:
        registros = get_registros()
    except Exception as e:
        print(f"Error al obtener los registros: {e}")
    encontrados = []
    dniBuscado = (input("Ingresa el dni para filtrar: "))

    for registro in registros:
        if registro['cliente_dni'] == dniBuscado:
            encontrados.append(registro)

    if len(encontrados) == 0:
        print()
        print("No se encontraron registros para el DNI ingresado.")
        return

    for j in range(len(encontrados)):
        print()
        for k in encontrados[j]:
            print(f"{k.capitalize()}: {encontrados[0][k]}")

def ver_estacionamiento():

    try:
        estacionamiento = get_estacionamiento()
    except Exception as e:
        print(f"Error al obtener los datos del estacionamiento: {e}")
        return
    
    print("\nDisposición actual del estacionamiento:")
    for i, fila in enumerate(estacionamiento):
        for j, lugar in enumerate(fila):
            print(f"[{lugar}]", end=" ")
        print()

def mostrar_estadisticas():
    try:
        estacionamiento = get_estacionamiento()
    except Exception as e:
        print(f"Error al obtener los registros: {e}")

    total_vehiculos = sum(1 for fila in estacionamiento for lugar in fila if lugar != "Vacio")
    total_lugares = len(estacionamiento) * len(estacionamiento[0])

    porcentaje_ocupacion = (total_vehiculos / total_lugares) * 100 if total_lugares > 0 else 0
    print(f"\nTotal de vehículos estacionados: {total_vehiculos}")
    print(f"Porcentaje de ocupación: {porcentaje_ocupacion:.2f}%")
