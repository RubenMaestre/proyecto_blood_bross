# principal.py

import sys
import os
import random
import pygame

# Añadir el directorio 'src' al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.configuracion import ANCHO, ALTO, TITULO, FPS, NEGRO
from src.menu import Menu

def cargar_musica(ruta):
    archivos_musica = []
    for archivo in os.listdir(ruta):
        if archivo.endswith('.mp3'):
            archivos_musica.append(os.path.join(ruta, archivo))
    return archivos_musica

def reproducir_musica(musica_menu):
    if musica_menu:
        archivo_musica = random.choice(musica_menu)
        pygame.mixer.music.load(archivo_musica)
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)

def manejar_eventos_musica(musica_menu):
    for evento in pygame.event.get():
        if evento.type == pygame.USEREVENT:
            reproducir_musica(musica_menu)

def mostrar_intro(pantalla, musica_menu):
    frames = [
        pygame.image.load("recursos/imagenes/intro/frame1.jpg"),
        pygame.image.load("recursos/imagenes/intro/frame2.jpg"),
        pygame.image.load("recursos/imagenes/intro/frame3.jpg")
    ]
    reloj = pygame.time.Clock()
    
    reproducir_musica(musica_menu)
    
    for frame in frames:
        pantalla.blit(frame, (0, 0))
        pygame.display.flip()
        pygame.time.wait(4000)  # Espera 4 segundos (4000 milisegundos)
        reloj.tick(FPS)
        manejar_eventos_musica(musica_menu)

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(TITULO)
    
    pygame.mixer.init()
    musica_menu = cargar_musica("recursos/sonidos/menu/")
    
    mostrar_intro(pantalla, musica_menu)
    
    menu = Menu(pantalla, musica_menu)
    menu.bucle_principal()

if __name__ == "__main__":
    main()
