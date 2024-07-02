# src/juego.py

import pygame
import sys
import random
from src.configuracion import ANCHO, ALTO, FPS, NEGRO, BLANCO, ROJO
from src.niveles.nivel import Nivel
from src.datos.progreso import guardar_progreso, cargar_progreso
from src.jugador.jugador import Jugador
from src.enemigos.nivel_1.malo_1 import Malo1

class Juego:
    def __init__(self, pantalla, musica_menu):
        self.pantalla = pantalla
        self.musica_menu = musica_menu
        self.reloj = pygame.time.Clock()
        self.corriendo = True
        self.fuente_mision = pygame.font.Font("recursos/fuentes/Orbitron-Bold.ttf", 50)
        self.fuente_fin = pygame.font.Font("recursos/fuentes/Orbitron-Bold.ttf", 70)
        self.nivel_actual = cargar_progreso()
        self.nivel = Nivel(self.nivel_actual)
        self.jugador = Jugador(ANCHO // 2, ALTO - 140)
        self.en_mision = False  # Estado para verificar si estamos en la misión
        self.enemigos = []
        self.tiempo_ultimo_enemigo = pygame.time.get_ticks()
        self.max_enemigos = 50  # Número máximo de enemigos a generar
        self.enemigos_eliminados = 0
        self.fin_de_partida = False  # Estado para verificar si la partida ha terminado

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
                if self.fin_de_partida and evento.key == pygame.K_r:
                    self.reiniciar_juego()
                elif self.fin_de_partida and evento.key == pygame.K_q:
                    self.corriendo = False
            elif evento.type == pygame.MOUSEBUTTONDOWN and not self.en_mision:
                self.iniciar_mision()

        if not self.fin_de_partida:
            self.jugador.manejar_eventos(eventos)

    def actualizar(self):
        if self.en_mision and not self.fin_de_partida:
            self.jugador.actualizar()
            for enemigo in self.enemigos:
                enemigo.actualizar(self.jugador)
                if enemigo.vida <= 0:
                    self.enemigos.remove(enemigo)
                    self.enemigos_eliminados += 1

            ahora = pygame.time.get_ticks()
            if len(self.enemigos) < 10 and self.enemigos_eliminados < self.max_enemigos and ahora - self.tiempo_ultimo_enemigo > 3000:
                self.generar_enemigo()
                self.tiempo_ultimo_enemigo = ahora

            if self.enemigos_eliminados >= self.max_enemigos:
                self.nivel_completado()

            if self.jugador.salud <= 0:
                self.fin_de_partida = True

            # Verificar colisiones entre disparos del jugador y enemigos
            for disparo in self.jugador.disparos:
                for enemigo in self.enemigos:
                    if disparo.rect.colliderect(enemigo.rect):
                        enemigo.recibir_dano(10)  # El disparo del jugador hace 10 de daño
                        if disparo in self.jugador.disparos:
                            self.jugador.disparos.remove(disparo)  # Eliminar disparo tras impacto

    def generar_enemigo(self):
        # Generar enemigo desde los bordes de la pantalla
        x = random.choice([random.randint(-50, -10), random.randint(ANCHO + 10, ANCHO + 50)])
        y = random.randint(50, ALTO // 3 * 2)  # Aparece en la parte superior de la pantalla, dejando 1/3 inferior libre
        enemigo = Malo1(x, y)
        self.enemigos.append(enemigo)

    def dibujar(self):
        self.pantalla.fill(NEGRO)
        if not self.en_mision:
            texto_mision = self.fuente_mision.render("Iniciar Misión 1", True, BLANCO)
            self.pantalla.blit(texto_mision, (ANCHO // 2 - texto_mision.get_width() // 2, ALTO // 2 - texto_mision.get_height() // 2))
        elif self.fin_de_partida:
            texto_fin = self.fuente_fin.render("Fin de Partida", True, ROJO)
            self.pantalla.blit(texto_fin, (ANCHO // 2 - texto_fin.get_width() // 2, ALTO // 2 - texto_fin.get_height() // 2))
            texto_reiniciar = self.fuente_mision.render("Presiona 'R' para Reiniciar o 'Q' para Salir", True, BLANCO)
            self.pantalla.blit(texto_reiniciar, (ANCHO // 2 - texto_reiniciar.get_width() // 2, ALTO // 2 + 50))
        else:
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

    def nivel_completado(self):
        print("¡Nivel completado!")
        self.corriendo = False
        # Aquí podrías añadir lógica para guardar el progreso y avanzar al siguiente nivel.

    def reiniciar_juego(self):
        self.__init__(self.pantalla, self.musica_menu)  # Reiniciar la instancia del juego
        self.bucle_principal()
