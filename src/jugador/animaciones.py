# src/jugador/animaciones.py

import pygame

class AnimacionesJugador:
    def __init__(self):
        self.idle_espalda = pygame.image.load("src/jugador/animaciones/idle/espalda.png")
        self.idle_izquierda = pygame.image.load("src/jugador/animaciones/idle/izquierda.png")
        self.idle_derecha = pygame.image.load("src/jugador/animaciones/idle/derecha.png")
        """"
        self.correr_izquierda = [
            pygame.image.load("src/jugador/animaciones/correr/izquierda.png"),
            pygame.image.load("src/jugador/animaciones/correr/izquierda.png"),
        ]
        
        self.correr_derecha = [
            pygame.image.load("src/jugador/animaciones/correr/derecha.png"),
            pygame.image.load("src/jugador/animaciones/correr/derecha.png"),
        ]
        
        self.disparar_espalda = pygame.image.load("src/jugador/animaciones/disparar/espalda.png")
        self.disparar_izquierda = pygame.image.load("src/jugador/animaciones/disparar/izquierda.png")
        self.disparar_derecha = pygame.image.load("src/jugador/animaciones/disparar/dderecha.png")
        
        self.voltereta_izquierda = [
            pygame.image.load("src/jugador/animaciones/voltereta/voltereta_izquierda_1.png"),
            pygame.image.load("src/jugador/animaciones/voltereta/voltereta_izquierda_2.png"),
        ]
        
        self.voltereta_derecha = [
            pygame.image.load("src/jugador/animaciones/voltereta/voltereta_derecha_1.png"),
            pygame.image.load("src/jugador/animaciones/voltereta/voltereta_derecha_2.png"),
        ]"""

    def obtener_imagen(self, accion, direccion, frame):
        if accion == "idle":
            if direccion == "espalda":
                return self.idle_espalda
            elif direccion == "izquierda":
                return self.idle_izquierda
            elif direccion == "derecha":
                return self.idle_derecha
        elif accion == "correr":
            if direccion == "izquierda":
                return self.correr_izquierda[frame % len(self.correr_izquierda)]
            elif direccion == "derecha":
                return self.correr_derecha[frame % len(self.correr_derecha)]
        elif accion == "disparar":
            if direccion == "espalda":
                return self.disparar_espalda
            elif direccion == "izquierda":
                return self.disparar_izquierda
            elif direccion == "derecha":
                return self.disparar_derecha
        elif accion == "voltereta":
            if direccion == "izquierda":
                return self.voltereta_izquierda[frame % len(self.voltereta_izquierda)]
            elif direccion == "derecha":
                return self.voltereta_derecha[frame % len(self.voltereta_derecha)]
