from utils.file_manager import get_registros, get_estacionamiento, get_finanzas
from modules.ordenamientos import selection_sort
from utils.utils import get_user_input, mostrar_estacionamiento, pedir_patente_formateada, \
    formatear_registro_estacionamiento, validate_dni
from functools import reduce



def mostrar_registro_por_patente():
    """
    Esta funcion busca registros de vehículos por número de patente.

        1) Solicita al usuario la patente del vehículo que quiere buscar.
        2) Recupera todos los registros desde get_registros().
        3) Compara las patentes con lo ingresado y guarda coincidencias en encontrados[].
        4) Si hay registros, imprime los datos, sino, avisa que no hay información disponible.
    """
    try:
        patente = pedir_patente_formateada()
    except TypeError:
        print("Patente incorrecta.")
        return

    registros = get_registros()
    encontrados = list(filter(lambda r: r['patente'].lower() == patente.lower(), registros))

    if not encontrados:
        print("\nNo se encontraron registros para la patente ingresada.")
        return

    for bloque in map(formatear_registro_estacionamiento, registros):
        print(bloque)

def mostrar_ranking_tipos_vehiculo():
    """
    Cuenta cuántos vehículos de cada tipo han ingresado al estacionamiento y los ordena.

        1)Obtiene registros de estacionamiento.
        2) Agrupa vehículos por tipo en conteo_por_tipo (ejemplo: "Camioneta", "Moto").
        3) Ordena los resultados con selection_sort(), de mayor a menor.
        4) Muestra el ranking de tipos de vehículos según su cantidad de ingresos.
    """


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
    registros = get_registros()

    if not registros:
        print("No hay registros disponibles.")
        return

    for bloque in map(formatear_registro_estacionamiento, registros):
        print(bloque)

def filtrar_por_tipo_vehiculo():
    """
    Permite buscar vehículos según su tipo (auto, moto, camioneta, etc.)

        1) Lista los tipos de vehículos disponibles según los registros.
        2) Solicita al usuario que ingrese el tipo de vehículo que quiere filtrar.
        3) Busca coincidencias y las imprime.
    """
    registros = get_registros()

    tipos_disponibles = set(registro["tipo_vehiculo"] for registro in registros)

    if not tipos_disponibles:
        print("No hay vehiculos cargados aun.")
        return

    print("\nTipos de vehículos disponibles:", ", ".join(tipos_disponibles))

    tipo_buscado = get_user_input(
        "Ingrese el tipo de vehículo a filtrar: ", str.upper, tipos_disponibles
    )

    encontrados = list(filter(lambda r: r["tipo_vehiculo"] == tipo_buscado, registros))

    if not encontrados:
        print(f"No hay registros para el tipo '{tipo_buscado}'.")
        return

    print(f"\n→ Registros de tipo '{tipo_buscado}':")
    for registro in encontrados:
        for campo, valor in registro.items():
            print(f"{campo.replace('_', ' ').capitalize()}: {valor}")
        print("-" * 40)


def mostrarPorDni():
    """
    Muestra todos los registros asociados a un número de DNI.

        1) Recupera la lista de registros almacenados.
        2) Solicita al usuario un DNI para filtrar.
        3) Busca coincidencias y muestra los datos del cliente.
    """
    registros = get_registros()
    dni_buscado = get_user_input("Ingrese el DNI del cliente: ", validator=validate_dni)

    encontrados = list(filter(lambda r: r['cliente_dni'] == dni_buscado, registros))

    if not encontrados:
        print("\nNo se encontraron registros para el DNI ingresado.")
        return

    for registro in encontrados:
        print()
        for clave, valor in registro.items():
            print(f"{clave.replace('_', ' ').capitalize()}: {valor}")

def ver_estacionamiento():
    mostrar_estacionamiento(get_estacionamiento())

def mostrar_estadisticas():
    estacionamiento = get_estacionamiento()

    total_vehiculos = sum(1 for fila in estacionamiento for lugar in fila if lugar != "Vacio")
    total_lugares = len(estacionamiento) * len(estacionamiento[0])

    porcentaje_ocupacion = (total_vehiculos / total_lugares) * 100 if total_lugares > 0 else 0
    print(f"\nTotal de vehículos estacionados: {total_vehiculos}")
    print(f"Porcentaje de ocupación: {porcentaje_ocupacion:.2f}%")

def mostrar_estado_caja():
    finanzas = get_finanzas()

    ingresos = list(filter(lambda f: f["tipo"] == "INGRESO", finanzas))
    egresos = list(filter(lambda f: f["tipo"] == "EGRESO", finanzas))

    total_ingresos = reduce(lambda acc, f: acc + f["monto"], ingresos, 0)
    total_egresos = reduce(lambda acc, f: acc + f["monto"], egresos, 0)
    neto = total_ingresos - total_egresos

    print(f"\nTotal Ingresado: ${total_ingresos}")
    print(f"Total Egresado: ${total_egresos}")
    print(f"Estado de caja: ${neto}")

def mostrar_gastos_por_cliente():
    dni = get_user_input("Ingrese el DNI del cliente: ", validator=validate_dni)
    finanzas = get_finanzas()

    gastos_cliente = list(filter(lambda f: f.get("cliente_dni") == dni, finanzas))

    if not gastos_cliente:
        print(f"No hay gastos registrados para el cliente DNI: {dni}")
        return

    total = reduce(lambda acc, f: acc + f["monto"], gastos_cliente, 0)

    print(f"\nGastos del cliente {dni}: ${total}")

    salidas = map(
        lambda f: f"- {f['fecha']} {f['hora']}: ${f['monto']} ({f['motivo']})",
        gastos_cliente
    )

    print("\n".join(salidas))