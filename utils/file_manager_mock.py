import data.data as db

def get_registros():
    return db.registros.copy()

def get_cocheras():
    return db.cocheras.copy()

def set_registros(nuevos_registros):
    db.registros.clear()
    db.registros.extend(nuevos_registros)

def set_cocheras(nuevas_cocheras):
    db.cocheras.clear()
    db.cocheras.extend(nuevas_cocheras)
