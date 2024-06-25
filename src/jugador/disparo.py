# src/jugador/disparo.py

import pygame

class Disparo:
    def __init__(self, x, y, direccion):
        self.x = x
        self.y = y
        self.direccion = direccion
        self.velocidad = 10
        self.imagen = pygame.image.load("src/jugador/animaciones/disparo/disparo.png")

    def actualizar(self):
        if self.direccion == "izquierda":
            self.x -= self.velocidad
        elif self.direccion == "derecha":
            self.x += self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))
