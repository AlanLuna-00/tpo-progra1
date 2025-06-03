import json
import os

BASE_PATH = os.path.dirname(__file__)


def _load_json(filename):
    path = os.path.join(BASE_PATH, filename)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"[ERROR] El archivo '{filename}' no existe.")
    except json.JSONDecodeError:
        raise ValueError(f"[ERROR] El archivo '{filename}' tiene formato JSON inválido o está vacío.")
    except Exception as e:
        raise RuntimeError(f"[ERROR] No se pudo leer el archivo '{filename}': {e}")


def _save_json(filename, data):
    path = os.path.join(BASE_PATH, filename)
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        raise RuntimeError(f"[ERROR] No se pudo guardar el archivo '{filename}': {e}")

def add_estacionados(patente):
    estacionados = get_estacionados()
    if patente not in estacionados:
        estacionados.append(patente)
        _save_json('../data/estacionados.json', estacionados)

def delete_estacionado(patente):
    estacionados = get_estacionados()
    if patente in estacionados:
        estacionados.remove(patente)
        _save_json('../data/estacionados.json', estacionados)

def add_registros(registro):
    registros = get_registros()
    registros.append(registro)
    _save_json('../data/registros.json', registros)

def get_estacionados():
    return _load_json('../data/estacionados.json')

def get_registros():
    return _load_json('../data/registros.json')

def get_estacionamiento():
    return _load_json('../data/estacionamiento.json')

def add_estacionamiento(i, j, patente):
    estacionamiento = get_estacionamiento()
    try:
        estacionamiento[i][j] = patente
        _save_json('../data/estacionamiento.json', estacionamiento)
    except IndexError:
        print(f"[ERROR] Índices fuera de rango al ubicar en ({i},{j})")

def get_finanzas():
    return _load_json('../data/finanzas.json')

def add_finanza(registro):
    finanzas = get_finanzas()
    finanzas.append(registro)
    _save_json('../data/finanzas.json', finanzas)