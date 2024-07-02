# src/jugador/disparador.py

import pygame
from src.configuracion import ANCHO, ALTO

class Disparador:
    def __init__(self, x, y):
        self.imagen = pygame.image.load("recursos/disparadores/disparador_1.png")
        self.rect = self.imagen.get_rect(center=(x, y))
        self.velocidad = 5

    def manejar_eventos(self, eventos):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_s] and self.rect.bottom < ALTO:
            self.rect.y += self.velocidad
        if teclas[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_d] and self.rect.right < ANCHO:
            self.rect.x += self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect.topleft)
