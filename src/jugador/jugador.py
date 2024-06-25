# src/jugador/jugador.py

import pygame
from src.jugador.animaciones import AnimacionesJugador
from src.jugador.disparo import Disparo

class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.animaciones = AnimacionesJugador()
        self.accion = "idle"
        self.direccion = "espalda"
        self.frame = 0
        self.disparando = False
        self.disparos = []

    def manejar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    self.accion = "correr"
                    self.direccion = "izquierda"
                elif evento.key == pygame.K_RIGHT:
                    self.accion = "correr"
                    self.direccion = "derecha"
                elif evento.key == pygame.K_SPACE:
                    self.accion = "voltereta"
                    self.direccion = "izquierda" if self.direccion == "izquierda" else "derecha"
                elif evento.key == pygame.K_z:
                    self.accion = "disparar"
                    self.disparando = True
                    self.disparar()
            elif evento.type == pygame.KEYUP:
                if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    self.accion = "idle"
                elif evento.key == pygame.K_z:
                    self.disparando = False
                    self.accion = "idle"

    def disparar(self):
        nuevo_disparo = Disparo(self.x, self.y, self.direccion)
        self.disparos.append(nuevo_disparo)

    def actualizar(self):
        self.frame += 1
        for disparo in self.disparos:
            disparo.actualizar()

    def dibujar(self, pantalla):
        imagen = self.animaciones.obtener_imagen(self.accion, self.direccion, self.frame)
        pantalla.blit(imagen, (self.x, self.y))
        for disparo in self.disparos:
            disparo.dibujar(pantalla)
