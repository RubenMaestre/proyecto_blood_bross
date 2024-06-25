# enemigos/ia.py

import pygame

class IAEnemigo:
    def __init__(self, enemigo):
        self.enemigo = enemigo

    def actualizar(self):
        # Lógica de patrullaje
        self.patrullar()
        # Lógica de ataque
        self.atacar()

    def patrullar(self):
        # Lógica de patrullaje del enemigo
        pass

    def atacar(self):
        # Lógica de ataque del enemigo
        pass
