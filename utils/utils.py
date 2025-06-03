import re

from utils.constants import PRECIO_POR_MEDIA_HORA, PRECIO_POR_HORA


def get_user_input(prompt, transform=None, valid_options=None, validator=None):

    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("La entrada no puede estar vacía. Inténtelo nuevamente.")
            continue

        if transform:
            user_input = transform(user_input)

        if valid_options and user_input not in valid_options:
            print(f"Opción no válida. Las opciones válidas son: {', '.join(valid_options)}")
            continue

        if validator and not validator(user_input):
            print("Entrada no válida según la condición requerida.")
            continue

        return user_input


def formatear_patente(patente):
    patente = patente.strip().upper()

    if re.fullmatch(r"[A-Z]{3}[0-9]{3}", patente):
        return f"{patente[:3]}-{patente[3:]}"

    if re.fullmatch(r"[A-Z]{2}[0-9]{3}[A-Z]{2}", patente):
        return f"{patente[:2]}-{patente[2:5]}-{patente[5:]}"

    raise TypeError("Formato de patente invalido.")

def pedir_patente_formateada():
    while True:
        try:
            entrada = get_user_input("Ingrese la patente del vehículo a buscar: ", str.upper)
            return formatear_patente(entrada)
        except TypeError as e:
            print(str(e))

def mostrar_estacionamiento(estacionamiento, mostrar_indices=True):
    filas = len(estacionamiento)
    columnas = len(estacionamiento[0]) if filas > 0 else 0
    ancho_celda = 12

    print("\nEstado actual del estacionamiento\n")

    if mostrar_indices:
        header = "   " + "".join([f"{j + 1:^{ancho_celda}}" for j in range(columnas)])
        print(header)
        print("  " + "-" * (len(header) - 2))

    for i, fila in enumerate(estacionamiento):
        if mostrar_indices:
            print(f"{i + 1:<2} |", end="")

        for lugar in fila:
            print(f"{lugar:<{ancho_celda}}", end="")
        print()

    print()

def buscar_cochera_por_patente(estacionamiento, patente):
    for i, fila in enumerate(estacionamiento):
        for j, cochera in enumerate(fila):
            if cochera == patente:
                return i, j
    return None, None

def buscar_cochera_vacia(estacionamiento):
    for i, fila in enumerate(estacionamiento):
        for j, cochera in enumerate(fila):
            if cochera == "Vacio":
                return i, j
    return None, None


def obtener_registro_activo_por_patente(registros, patente):
    for registro in registros:
        if registro["patente"] == patente and not registro["salio"]:
            return registro
    return None

def calcular_precio(minutos):
    if minutos <= 30:
        return PRECIO_POR_MEDIA_HORA
    elif minutos <= 60:
        return PRECIO_POR_HORA
    else:
        horas_completas = int(minutos // 60)
        minutos_restantes = int(minutos % 60)

        total = horas_completas * PRECIO_POR_HORA
        if minutos_restantes > 30:
            total += PRECIO_POR_HORA
        elif minutos_restantes > 0:
            total += PRECIO_POR_MEDIA_HORA

        return total


def formatear_registro_estacionamiento(r):
    print("\n------\n")
    hora_salida = 'No salio aun' if r['salio'] else r.get('hora_salida', '-')
    lugar = r.get("lugar")
    lugar_str = f"Fila {lugar[0]} - Columna {lugar[1]}" if isinstance(lugar, (list, tuple)) else "-"

    return "\n".join([
        f"Fecha: {r['fecha']}",
        f"Hora entrada: {r.get('hora_entrada', '-')}",
        f"Hora salida: {hora_salida}",
        f"Patente: {r['patente']}",
        f"Tipo vehiculo: {r['tipo_vehiculo']}",
        f"Cliente DNI: {r['cliente_dni']}",
        f"Estacionado: {'NO' if r['salio'] else 'SI'}",
        f"Lugar: {lugar_str}"
    ])

def validate_dni(dni):
    """
    Valida que el DNI sea un número de 8 dígitos.
    """
    return isinstance(dni, str) and dni.isdigit() and (len(dni) == 8 or len(dni) == 7)