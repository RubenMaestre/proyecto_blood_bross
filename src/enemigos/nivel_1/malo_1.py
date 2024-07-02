# src/enemigos/nivel_1/malo_1.py

import pygame
import random
from src.configuracion import ANCHO, ALTO

class Malo1:
    def __init__(self, x, y):
        self.image = pygame.image.load("recursos/imagenes/enemigos/malo_1.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.vida = 20
        self.dano = 10
        self.velocidad = random.randint(1, 3)  # Velocidad horizontal aleatoria
        self.direccion = random.choice(["izquierda", "derecha"])  # Dirección aleatoria
        self.tiempo_ataque = random.randint(3000, 10000)  # en milisegundos
        self.ultimo_ataque = pygame.time.get_ticks()

        self.disparo_imagen = pygame.image.load("recursos/disparadores/disparo_malo.png")
        self.disparos = []

    def actualizar(self, jugador):
        ahora = pygame.time.get_ticks()
        if ahora - self.ultimo_ataque > self.tiempo_ataque:
            self.atacar()
            self.ultimo_ataque = ahora
            self.tiempo_ataque = random.randint(3000, 10000)

        if self.direccion == "izquierda":
            self.rect.x -= self.velocidad
            if self.rect.x < 0:
                self.direccion = "derecha"
        else:
            self.rect.x += self.velocidad
            if self.rect.x > ANCHO - self.rect.width:
                self.direccion = "izquierda"

        for disparo in self.disparos:
            disparo.actualizar()
            if disparo.rect.colliderect(jugador.rect):
                jugador.recibir_dano(self.dano)
                self.disparos.remove(disparo)

        self.disparos = [disparo for disparo in self.disparos if not disparo.fuera_de_pantalla()]

    def atacar(self):
        disparo = DisparoMalo(self.rect.centerx, self.rect.bottom, self.disparo_imagen)
        self.disparos.append(disparo)

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.morir()

    def morir(self):
        self.rect.x = -100  # Movemos el enemigo fuera de la pantalla

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect.topleft)
        for disparo in self.disparos:
            disparo.dibujar(pantalla)

class DisparoMalo:
    def __init__(self, x, y, imagen):
        self.imagen = imagen
        self.rect = self.imagen.get_rect(center=(x, y))
        self.velocidad = 3

    def actualizar(self):
        self.rect.y += self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect.topleft)

    def fuera_de_pantalla(self):
        return self.rect.y > ALTO
