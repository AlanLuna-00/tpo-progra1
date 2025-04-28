import data.data as db


def get_registros():
    """
    :return: Devuelve una copia de registros, evitando que los datos originales sean modificados directamente.
    """

    return db.registros.copy()


def get_cocheras():
    """
    :return: Obtiene la lista de cocheras disponibles, con información sobre su estado (ocupada o vacía).
    """

    return db.cocheras.copy()


def set_registros(nuevos_registros):
    """
    Elimina los registros existentes y los reemplaza con la nueva lista proporcionada.

    :param nuevos_registros: Este parametro representa una nueva lista de registros cargados.
    :return: Retorna la nueva lista de registros que se le proporciono, reemplazando la existente.
    """

    db.registros.clear()
    db.registros.extend(nuevos_registros)


def set_cocheras(nuevas_cocheras):
    """
    Vacía la lista de cocheras y carga una nueva configuración.

    :param nuevas_cocheras: Se le envía una nueva configuracion de la lista de las cocheras.
    :return: Retorna la nueva configuracion de las cocheras, reemplazando la anterior.
    """

    db.cocheras.clear()
    db.cocheras.extend(nuevas_cocheras)


def get_estacionamiento():
    """
    :return: Devuelve la matriz del estacionamiento, reflejando qué espacios están ocupados y qué lugares siguen libres.
    """

    return db.estacionamiento.copy()


def get_estacionados():
    """
    :return: Devuelve la lista de patentes de vehículos actualmente estacionados.
    """

    return db.estacionados.copy()


def add_estacionamiento(fila, columna, patente):
    """
    Ubica un vehículo en una cochera específica, cambiando su estado de "Vacío" a la patente del auto.

    :param fila: Recibe la fila de la cochera (int)
    :param columna: Recibe la columna de la cochera (int)
    :param patente: Recibe la patente del auto (string)
    :return: La patente del vehículo que se le envió, en el lugar en donde se asigna, que antes estaba vacio.
    """

    db.estacionamiento[fila][columna] = patente


def add_estacionados(patente):
    """
    Registra la patente del vehículo en la lista de autos actualmente estacionados. Funciona conmo una db mini

    :param patente: Recibe la patente del vehiculo (string)
    :return: Aniade la patente del vehículo a la lista de de los estacionados
    """

    db.estacionados.append(patente)


def add_registros(nuevos_registros):
    """
    Añade un nuevo registro con la información del vehículo, incluyendo fecha, hora, tipo y estado.

    :param nuevos_registros:
    :return: Crea un nuevo diccionario con ciertos datos del vehículo que brindan informacion del mismo
    """

    db.registros.append(nuevos_registros)