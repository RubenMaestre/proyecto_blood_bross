# datos/progreso.py

import json
import os

PROGRESO_ARCHIVO = "progreso.json"

def guardar_progreso(nivel):
    progreso = {"nivel_desbloqueado": nivel}
    with open(PROGRESO_ARCHIVO, "w") as archivo:
        json.dump(progreso, archivo)

def cargar_progreso():
    if os.path.exists(PROGRESO_ARCHIVO):
        with open(PROGRESO_ARCHIVO, "r") as archivo:
            progreso = json.load(archivo)
            return progreso.get("nivel_desbloqueado", 1)
    return 1
