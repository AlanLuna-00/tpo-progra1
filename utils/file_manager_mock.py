import data.data as db


def get_registros():
    """
    :return: Devuelve una copia de registros, evitando que los datos originales sean modificados directamente.
    """

    try:
        return db.registros.copy()
    except Exception as e:
        print(f"Error al obtener los registros: {e}")
        return []

def get_estacionamiento():
    """
    :return: Devuelve la matriz del estacionamiento, reflejando qué espacios están ocupados y qué lugares siguen libres.
    """

    try:
        return db.estacionamiento.copy()
    except Exception as e:
        print(f"Error al obtener el estacionamiento: {e}")
        return []


def get_estacionados():
    """
    :return: Devuelve la lista de patentes de vehículos actualmente estacionados.
    """

    try:
        return db.estacionados.copy()
    except Exception as e:
        print(f"Error al obtener los estacionados: {e}")
        return []


def add_estacionamiento(fila, columna, patente):
    """
    Ubica un vehículo en una cochera específica, cambiando su estado de "Vacío" a la patente del auto.

    :param fila: Recibe la fila de la cochera (int)
    :param columna: Recibe la columna de la cochera (int)
    :param patente: Recibe la patente del auto (string)
    :return: La patente del vehículo que se le envió, en el lugar en donde se asigna, que antes estaba vacio.
    """

    try:
        db.estacionamiento[fila][columna] = patente
    except IndexError:
        print(f"Error: La cochera ({fila}, {columna}) no existe.")
    except Exception as e:
        print(f"Error al agregar el vehículo a la cochera: {e}")


def add_estacionados(patente):
    """
    Registra la patente del vehículo en la lista de autos actualmente estacionados. Funciona conmo una db mini

    :param patente: Recibe la patente del vehiculo (string)
    :return: Aniade la patente del vehículo a la lista de de los estacionados
    """

    try:
        db.estacionados.append(patente)
    except Exception as e:
        print(f"Error al agregar la patente a los estacionados: {e}")


def add_registros(nuevos_registros):
    """
    Añade un nuevo registro con la información del vehículo, incluyendo fecha, hora, tipo y estado.

    :param nuevos_registros:
    :return: Crea un nuevo diccionario con ciertos datos del vehículo que brindan informacion del mismo
    """

    try:
        db.registros.append(nuevos_registros)
    except Exception as e:
        print(f"Error al agregar el registro: {e}")

def delete_estacionado(patente):
    try:
        db.estacionados.remove(patente)
    except ValueError:
        print(f"Error: La patente {patente} no está en la lista de estacionados.")
    except Exception as e:
        print(f"Error al eliminar la patente de los estacionados: {e}")