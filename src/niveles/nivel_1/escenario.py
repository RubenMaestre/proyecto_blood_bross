# niveles/nivel_1/escenario.py

import pygame

class Escenario:
    def __init__(self):
        self.fondo = pygame.image.load("src/niveles/nivel_1/fondos/nivel_1_fondo.jpg")
        self.elementos_interactivos = [
            ElementoInteractivo("src/niveles/nivel_1/elementos_interactivos/obstaculo1.png", 300, 400),
            ElementoInteractivo("src/niveles/nivel_1/elementos_interactivos/obstaculo2.png", 500, 300)
        ]

    def dibujar(self, pantalla):
        pantalla.blit(self.fondo, (0, 0))
        for elemento in self.elementos_interactivos:
            elemento.dibujar(pantalla)

class ElementoInteractivo:
    def __init__(self, ruta_imagen, x, y):
        self.imagen = pygame.image.load(ruta_imagen)
        self.rect = self.imagen.get_rect(topleft=(x, y))
        self.destructible = True

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect.topleft)

    def interactuar(self):
        # Lógica para interactuar con el elemento (destruir, cubrir, etc.)
        pass
