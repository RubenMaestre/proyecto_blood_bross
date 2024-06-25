# enemigos/enemigo.py

import pygame
from src.enemigos.animaciones import AnimacionesEnemigo
from src.enemigos.ia import IAEnemigo

class Enemigo:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.animaciones = AnimacionesEnemigo(self)
        self.ia = IAEnemigo(self)
        self.salud = 100  # Salud base del enemigo

    def manejar_eventos(self, eventos):
        pass  # Los enemigos no suelen manejar eventos directos

    def actualizar(self):
        self.ia.actualizar()
        self.animaciones.actualizar()

    def dibujar(self, pantalla):
        self.animaciones.dibujar(pantalla)
