# src/jugador/disparo.py

import pygame

class Disparo:
    def __init__(self, x, y, objetivo_x, objetivo_y):
        self.x = x
        self.y = y
        self.velocidad = 10
        self.imagen = pygame.image.load("recursos/disparadores/disparo.png")
        self.rect = self.imagen.get_rect(center=(self.x, self.y))

        # Calcular la dirección del disparo
        delta_x = objetivo_x - x
        delta_y = objetivo_y - y
        distancia = (delta_x ** 2 + delta_y ** 2) ** 0.5
        self.velocidad_x = self.velocidad * (delta_x / distancia)
        self.velocidad_y = self.velocidad * (delta_y / distancia)

    def actualizar(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect.topleft)

    def fuera_de_pantalla(self, ancho_pantalla, alto_pantalla):
        return (self.rect.x < 0 or self.rect.x > ancho_pantalla or
                self.rect.y < 0 or self.rect.y > alto_pantalla)


