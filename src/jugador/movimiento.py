# jugador/movimiento.py

import pygame

class Movimiento:
    def __init__(self, jugador):
        self.jugador = jugador
        self.velocidad = 5

    def manejar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    self.jugador.x -= self.velocidad
                elif evento.key == pygame.K_RIGHT:
                    self.jugador.x += self.velocidad
                elif evento.key == pygame.K_DOWN:
                    self.rular()

    def rular(self):
        # Lógica para el movimiento de "rular"
        pass

    def actualizar(self):
        pass
