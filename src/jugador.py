# jugador.py

import pygame

class Jugador:
    def __init__(self, x, y):
        self.imagen = pygame.image.load("recursos/imagenes/jugador.png")
        self.rect = self.imagen.get_rect(topleft=(x, y))
        self.velocidad = 5

    def manejar_eventos(self, eventos):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidad

    def actualizar(self):
        pass

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect.topleft)
