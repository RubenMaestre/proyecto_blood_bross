# menu.py

import sys
import os
import pygame
import time
import cv2
import random
from moviepy.editor import VideoFileClip

# Añadir el directorio 'src' al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.configuracion import ANCHO, ALTO, FPS, NEGRO, BLANCO, ROJO, GRIS
from src.opciones_usuario import OpcionesUsuario
from src.juego import Juego

class Menu:
    def __init__(self, pantalla, musica_menu):
        self.pantalla = pantalla
        self.musica_menu = musica_menu
        self.reloj = pygame.time.Clock()
        self.corriendo = True
        self.fondo_menu = pygame.image.load("recursos/imagenes/menu/background.jpg")
        self.fuente_titulo = pygame.font.Font("recursos/fuentes/Orbitron-Bold.ttf", 120)
        self.fuente_menu = pygame.font.Font("recursos/fuentes/Orbitron-Bold.ttf", 50)
        self.fuente_info = pygame.font.Font("recursos/fuentes/Orbitron-Bold.ttf", 30)  # Nueva fuente para la información
        self.seleccion = 0
        self.opciones = ["Nueva Partida", "Opciones", "Salir"]
        self.posiciones = [
            (ANCHO // 2 - self.fuente_menu.size(self.opciones[0])[0] // 2, ALTO // 4 + 120),
            (ANCHO - self.fuente_menu.size(self.opciones[1])[0] - 50, ALTO - 150),
            (ANCHO - self.fuente_menu.size(self.opciones[2])[0] - 50, ALTO - 80)
        ]
        self.icono_tiempo = pygame.image.load("recursos/imagenes/menu/tiempo.png")
        self.angulo_tiempo = 0

    def bucle_principal(self):
        while self.corriendo:
            self.manejar_eventos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(FPS)
    
    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.USEREVENT:
                reproducir_musica(self.musica_menu)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.corriendo = False
                elif evento.key == pygame.K_UP:
                    self.seleccion = (self.seleccion - 1) % len(self.opciones)
                elif evento.key == pygame.K_DOWN:
                    self.seleccion = (self.seleccion + 1) % len(self.opciones)
                elif evento.key == pygame.K_RETURN:
                    self.ejecutar_opcion()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                self.manejar_click(evento.pos)

    def manejar_click(self, posicion):
        for i, pos in enumerate(self.posiciones):
            ancho, alto = self.fuente_menu.size(self.opciones[i])
            rect = pygame.Rect(pos[0], pos[1], ancho, alto)
            if rect.collidepoint(posicion):
                self.seleccion = i
                self.ejecutar_opcion()
                break

    def ejecutar_opcion(self):
        if self.opciones[self.seleccion] == "Nueva Partida":
            self.transicion_a_nueva_partida()
        elif self.opciones[self.seleccion] == "Opciones":
            opciones_usuario = OpcionesUsuario(self.pantalla, self.musica_menu)
            opciones_usuario.bucle_opciones()
        elif self.opciones[self.seleccion] == "Salir":
            self.corriendo = False

    def transicion_a_nueva_partida(self):
        # Transición en negro con icono giratorio
        tiempo_icono_centro = (ANCHO // 2, ALTO // 2)
        for alpha in range(0, 255, 5):
            self.pantalla.fill(NEGRO)
            s = pygame.Surface((ANCHO, ALTO))
            s.set_alpha(alpha)
            s.fill(NEGRO)
            self.pantalla.blit(s, (0, 0))
            self.angulo_tiempo = (self.angulo_tiempo + 10) % 360
            icono_rotado = pygame.transform.rotate(self.icono_tiempo, self.angulo_tiempo)
            icono_rect = icono_rotado.get_rect(center=tiempo_icono_centro)
            self.pantalla.blit(icono_rotado, icono_rect.topleft)
            pygame.display.flip()
            pygame.time.wait(10)

        # Atenuación de la música
        for volume in range(10, -1, -1):
            pygame.mixer.music.set_volume(volume / 10.0)
            pygame.time.wait(300)

        pygame.mixer.music.stop()

        # Reproducción del video y audio
        self.reproducir_video_y_audio("recursos/videos/video_1.mp4", "recursos/videos/video_1_audio.mp3")

    def reproducir_video_y_audio(self, ruta_video, ruta_audio):
        # Asegurarse de que el volumen esté al máximo
        pygame.mixer.music.set_volume(1.0)

        # Iniciar reproducción de audio
        pygame.mixer.music.load(ruta_audio)
        pygame.mixer.music.play()

        cap = cv2.VideoCapture(ruta_video)
        if not cap.isOpened():
            self.ir_a_juego()
            return

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (ANCHO, ALTO))
            frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
            self.pantalla.blit(frame, (0, 0))
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    cap.release()
                    pygame.mixer.music.stop()
                    self.ir_a_juego()
                    return

        cap.release()
        pygame.mixer.music.stop()
        self.ir_a_juego()

    def ir_a_juego(self):
        juego = Juego(self.pantalla, self.musica_menu)
        juego.bucle_principal()

    def actualizar(self):
        pass

    def dibujar(self):
        self.pantalla.blit(self.fondo_menu, (0, 0))
        self.mostrar_menu()
        self.mostrar_info()  # Llamar a la función para mostrar la información adicional
        pygame.display.flip()

    def mostrar_menu(self):
        texto_titulo = self.fuente_titulo.render("Rogue Hunter", True, ROJO)
        self.pantalla.blit(texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, ALTO // 4))

        for i, opcion in enumerate(self.opciones):
            color = BLANCO if i == self.seleccion else GRIS
            texto = self.fuente_menu.render(opcion, True, color)
            self.pantalla.blit(texto, self.posiciones[i])

    def mostrar_info(self):
        texto_realizado_por = self.fuente_info.render("Realizado por Rubén Maestre", True, BLANCO)
        texto_version = self.fuente_info.render("Versión: 0.1", True, BLANCO)
        self.pantalla.blit(texto_realizado_por, (50, ALTO - 100))
        self.pantalla.blit(texto_version, (50, ALTO - 60))

def reproducir_musica(musica_menu):
    if musica_menu:
        archivo_musica = random.choice(musica_menu)
        pygame.mixer.music.load(archivo_musica)
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
