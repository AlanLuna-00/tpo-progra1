import random
from utils.file_manager import get_estacionamiento, get_registros, get_estacionados, add_estacionados, \
    add_estacionamiento, add_registros, delete_estacionado, add_finanza
from datetime import datetime
from utils.utils import get_user_input, formatear_patente, mostrar_estacionamiento, buscar_cochera_por_patente, \
    buscar_cochera_vacia, obtener_registro_activo_por_patente, pedir_patente_formateada, calcular_precio, validate_dni


def agregar_estacionado():
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

    estacionamiento = get_estacionamiento()
    estacionados = get_estacionados()

    patente = pedir_patente_formateada()

    if patente in estacionados:
        print("Ya ingresado.")
        return

    now = datetime.now()
    fecha = now.strftime("%d/%m/%Y")
    hora_actual = now.strftime("%H:%M")
    tipo = get_user_input("Ingrese tipo: ", str.upper)
    dni = get_user_input("Ingrese el DNI del cliente: ", validator=validate_dni)

    i, j = buscar_cochera_vacia(estacionamiento)
    if i is None:
        print("Estacionamiento lleno.")
    else:
        add_estacionados(patente)
        add_registros({
            "fecha": fecha,
            "hora_entrada": hora_actual,
            "hora_salida": None,
            "patente": patente,
            "tipo_vehiculo": tipo,
            "cliente_dni": dni,
            "salio": False,
            "lugar": (i + 1, j + 1)
        })
        add_estacionamiento(i, j, patente)
        estacionamiento = get_estacionamiento()
        print(f"\nVehículo {patente} ingresado en la cochera ({i + 1},{j + 1})")


    mostrar_estacionamiento(estacionamiento)



def egresar_vehiculo():
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
    estacionamiento = get_estacionamiento()
    estacionados = get_estacionados()
    registros = get_registros()

    patente = pedir_patente_formateada()

    if patente not in estacionados:
        print("El vehículo no está estacionado.")
        return

    dni = get_user_input("Ingrese el DNI del cliente: ", validator=validate_dni)
    now = datetime.now()
    fecha = now.strftime("%d/%m/%Y")
    hora_actual = now.strftime("%H:%M")

    registro = obtener_registro_activo_por_patente(registros, patente)
    if not registro:
        print("No se encontró un registro activo para ese vehículo.")
        mostrar_estacionamiento(estacionamiento)
        return

    if registro["cliente_dni"] != dni:
        print("El DNI no coincide.")
        mostrar_estacionamiento(estacionamiento)
        return

    hora_entrada_str = registro.get("hora_entrada")
    if not hora_entrada_str:
        print("No se puede calcular el tiempo: falta hora de entrada.")
        return

    hora_entrada = datetime.strptime(f"{fecha} {hora_entrada_str}", "%d/%m/%Y %H:%M")
    duracion = (now - hora_entrada).total_seconds() / 60

    monto = calcular_precio(duracion)

    add_registros({
        "fecha": fecha,
        "hora_entrada": registro.get("hora_entrada"),
        "hora_salida": hora_actual,
        "patente": patente,
        "tipo_vehiculo": registro["tipo_vehiculo"],
        "cliente_dni": dni,
        "salio": True,
        "lugar": registro["lugar"],
    })

    add_finanza({
        "tipo": "INGRESO",
        "motivo": "Cobro por estacionamiento",
        "monto": monto,
        "cliente_dni": dni,
        "fecha": fecha,
        "hora": hora_actual
    })

    delete_estacionado(patente)

    i, j = registro["lugar"]

    add_estacionamiento(i - 1, j - 1, "Vacio")
    estacionamiento = get_estacionamiento()
    print(f"\nVehículo {patente} salió de la cochera ({i},{j})")

    mostrar_estacionamiento(estacionamiento)

def registrar_movimiento():
    tipo = get_user_input("Tipo de movimiento: (INGRESO, EGRESO): ", str.upper, ["INGRESO", "EGRESO"])
    motivo = get_user_input(f"Motivo del {tipo.lower()}: ")
    monto = get_user_input("Monto: ", float , validator=lambda x: x > 0)

    asociar_cliente = get_user_input("¿Asociar a un cliente? (S/N): ", str.upper, ["S", "N"])

    dni = None
    if asociar_cliente == "S":
        dni = get_user_input("Ingrese el DNI del cliente: ", validator=validate_dni)


    now = datetime.now()
    add_finanza({
        "tipo": tipo,
        "motivo": motivo,
        "monto": monto,
        "fecha": now.strftime("%d/%m/%Y"),
        "hora": now.strftime("%H:%M"),
        "cliente_dni": dni
    })

    print(f"{tipo.capitalize()} registrado por ${monto} - Motivo: {motivo}")