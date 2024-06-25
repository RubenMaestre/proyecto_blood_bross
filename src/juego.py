# juego.py

import pygame
import sys
from src.configuracion import ANCHO, ALTO, FPS, NEGRO, BLANCO
from src.niveles.nivel import Nivel
from src.datos.progreso import guardar_progreso, cargar_progreso
from src.jugador.jugador import Jugador
from src.enemigos.nivel_1.enemigos_nivel_1 import EnemigoBasico, EnemigoRapido, LiderMafia

class Juego:
    def __init__(self, pantalla, musica_menu):
        self.pantalla = pantalla
        self.musica_menu = musica_menu
        self.reloj = pygame.time.Clock()
        self.corriendo = True
        self.fuente_mision = pygame.font.Font("recursos/fuentes/Orbitron-Bold.ttf", 50)
        self.nivel_actual = cargar_progreso()
        self.nivel = Nivel(self.nivel_actual)
        self.jugador = Jugador(ANCHO // 2, ALTO - 100)
        self.enemigos = [
            EnemigoBasico(100, 100),
            EnemigoRapido(300, 100),
            LiderMafia(500, 100)
        ]
        self.en_mision = False  # Estado para verificar si estamos en la misión

    def bucle_principal(self):
        while self.corriendo:
            eventos = pygame.event.get()
            self.manejar_eventos(eventos)
            self.actualizar()
            self.dibujar()
            self.reloj.tick(FPS)
    
    def manejar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.corriendo = False
            elif evento.type == pygame.MOUSEBUTTONDOWN and not self.en_mision:
                self.iniciar_mision()

        self.jugador.manejar_eventos(eventos)

    def actualizar(self):
        if self.en_mision:
            self.jugador.actualizar()
            for enemigo in self.enemigos:
                enemigo.actualizar()

    def dibujar(self):
        if not self.en_mision:
            self.pantalla.fill(NEGRO)
            texto_mision = self.fuente_mision.render("Iniciar Misión 1", True, BLANCO)
            self.pantalla.blit(texto_mision, (ANCHO // 2 - texto_mision.get_width() // 2, ALTO // 2 - texto_mision.get_height() // 2))
        else:
            self.pantalla.fill(NEGRO)
            self.nivel.pantallas[0].dibujar(self.pantalla)  # Dibujar el escenario del nivel actual
            self.jugador.dibujar(self.pantalla)
            for enemigo in self.enemigos:
                enemigo.dibujar(self.pantalla)
        pygame.display.flip()

    def iniciar_mision(self):
        self.en_mision = True
        print(f"Iniciando misión del nivel {self.nivel_actual}")
        self.nivel.pantallas[0].cargar()  # Cargar la primera pantalla del nivel actual

    def guardar_progreso(self):
        guardar_progreso(self.nivel_actual)
