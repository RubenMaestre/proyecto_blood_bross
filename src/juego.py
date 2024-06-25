# juego.py

import pygame
from src.configuracion import ANCHO, ALTO, FPS, NEGRO, BLANCO

class Juego:
    def __init__(self, pantalla, musica_menu):
        self.pantalla = pantalla
        self.musica_menu = musica_menu
        self.reloj = pygame.time.Clock()
        self.corriendo = True
        self.fuente_mision = pygame.font.Font("recursos/fuentes/Orbitron-Bold.ttf", 50)

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
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.corriendo = False

    def actualizar(self):
        pass

    def dibujar(self):
        self.pantalla.fill(NEGRO)
        texto_mision = self.fuente_mision.render("Iniciar Misión 1", True, BLANCO)
        self.pantalla.blit(texto_mision, (ANCHO // 2 - texto_mision.get_width() // 2, ALTO // 2 - texto_mision.get_height() // 2))
        pygame.display.flip()
