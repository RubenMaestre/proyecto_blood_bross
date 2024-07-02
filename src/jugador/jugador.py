# src/jugador/jugador.py

import pygame
from src.jugador.animaciones import AnimacionesJugador
from src.jugador.disparo import Disparo
from src.jugador.disparador import Disparador
import time
from src.configuracion import ANCHO, ALTO

class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y - 60  # Ajuste para elevar al jugador en la pantalla
        self.animaciones = AnimacionesJugador()
        self.accion = "idle"
        self.direccion = "espalda"
        self.frame = 0
        self.disparando = False
        self.voltereta_en_progreso = False
        self.disparos = []
        self.velocidad = 5

        self.salud = 100
        self.max_salud = 100
        self.ultimo_disparo = time.time()  # Para manejar la cadencia de disparo

        self.image = self.animaciones.obtener_imagen(self.accion, self.direccion, self.frame)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.disparador = Disparador(self.rect.centerx, self.rect.centery)

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
                    self.iniciar_voltereta()
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

        self.disparador.manejar_eventos(eventos)

    def iniciar_voltereta(self):
        self.voltereta_en_progreso = True
        self.accion = "voltereta"
        self.frame = 0

    def disparar(self):
        if time.time() - self.ultimo_disparo >= 1:  # Permitir disparar una bala por segundo
            objetivo_x, objetivo_y = self.disparador.rect.center
            nuevo_disparo = Disparo(self.rect.centerx, self.rect.centery, objetivo_x, objetivo_y)
            self.disparos.append(nuevo_disparo)
            self.ultimo_disparo = time.time()

    def actualizar(self):
        self.frame += 1

        if self.accion == "correr":
            if self.direccion == "izquierda":
                self.rect.x -= self.velocidad
                if self.rect.x < 0:
                    self.rect.x = 0
            elif self.direccion == "derecha":
                self.rect.x += self.velocidad
                if self.rect.x > ANCHO - self.rect.width:
                    self.rect.x = ANCHO - self.rect.width
        elif self.accion == "voltereta" and self.voltereta_en_progreso:
            self.realizar_voltereta()

        for disparo in self.disparos:
            disparo.actualizar()

        self.disparos = [disparo for disparo in self.disparos if not disparo.fuera_de_pantalla(ANCHO, ALTO)]

        if self.salud <= 0:
            self.morir()

    def realizar_voltereta(self):
        if self.frame == 1:
            if self.direccion == "izquierda":
                self.rect.x -= self.rect.width
            elif self.direccion == "derecha":
                self.rect.x += self.rect.width
        elif self.frame == 2:
            if self.direccion == "izquierda":
                self.rect.x -= self.rect.width
            elif self.direccion == "derecha":
                self.rect.x += self.rect.width
            self.voltereta_en_progreso = False
            self.accion = "idle"
            self.direccion = "espalda"

        # Asegurar que el jugador no salga de los límites de la pantalla
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > ANCHO - self.rect.width:
            self.rect.x = ANCHO - self.rect.width

    def dibujar(self, pantalla):
        imagen = self.animaciones.obtener_imagen(self.accion, self.direccion, self.frame)
        pantalla.blit(imagen, self.rect.topleft)
        self.disparador.dibujar(pantalla)
        for disparo in self.disparos:
            disparo.dibujar(pantalla)
        self.dibujar_barra_salud(pantalla)

    def dibujar_barra_salud(self, pantalla):
        largo_barra = 100
        alto_barra = 10
        x_barra = self.rect.centerx - largo_barra // 2
        y_barra = self.rect.top - 20
        proporcion_salud = self.salud / self.max_salud
        largo_barra_salud = int(largo_barra * proporcion_salud)

        pygame.draw.rect(pantalla, (255, 0, 0), (x_barra, y_barra, largo_barra, alto_barra))  # Fondo rojo
        pygame.draw.rect(pantalla, (0, 255, 0), (x_barra, y_barra, largo_barra_salud, alto_barra))  # Salud verde

    def recibir_dano(self, cantidad):
        self.salud -= cantidad
        if self.salud < 0:
            self.salud = 0

    def morir(self):
        self.corriendo = False
        print("¡El jugador ha muerto!")
        # Aquí podrías añadir lógica adicional para el fin del juego, como mostrar un mensaje de fin de juego o volver al menú principal
