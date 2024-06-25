# opciones_usuario.py

import pygame
import random
import os
from src.configuracion import BLANCO, NEGRO, GRIS, ROJO

class OpcionesUsuario:
    def __init__(self, pantalla, musica_menu):
        self.pantalla = pantalla
        self.musica_menu = musica_menu
        self.reloj = pygame.time.Clock()
        self.corriendo = True
        self.fuente_menu = pygame.font.Font("recursos/fuentes/Orbitron-Bold.ttf", 50)
        self.fuente_opcion = pygame.font.Font("recursos/fuentes/Orbitron-Bold.ttf", 40)
        self.fuente_resolucion = pygame.font.Font("recursos/fuentes/Orbitron-Bold.ttf", 30)

        self.resoluciones = [(1920, 1080), (1600, 900), (1280, 720), (1024, 576)]
        self.resolucion_actual = 0

        self.musica_activa = True
        self.volumen_musica = 5
        self.musica_sonando = True

        self.efectos_activos = True
        self.volumen_efectos = 5

        self.opciones = ["Resolución", "Música", "Volumen Música", "Efectos", "Volumen Efectos", "Volver"]
        self.seleccion = 0

        self.sonido_efecto = pygame.mixer.Sound("recursos/sonidos/menu/efectos/efecto_1.mp3")

        self.offset_vertical = -20  # Ajusta este valor para mover todo hacia arriba o abajo

    def reproducir_musica(self):
        if not self.musica_activa:
            pygame.mixer.music.stop()
            self.musica_sonando = False
            return

        if self.musica_sonando:
            return

        if self.musica_menu:
            archivo_musica = random.choice(self.musica_menu)
            pygame.mixer.music.load(archivo_musica)
            pygame.mixer.music.play(-1)
            self.musica_sonando = True

    def reproducir_efecto(self):
        if self.efectos_activos:
            self.sonido_efecto.play()

    def bucle_opciones(self):
        while self.corriendo:
            self.manejar_eventos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(60)
    
    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
        # Check if the resolution buttons are clicked
        menos_resolucion_rect = pygame.Rect(self.pantalla.get_width() // 2 - 180, self.pantalla.get_height() // 4 + self.offset_vertical, 40, 40)
        mas_resolucion_rect = pygame.Rect(self.pantalla.get_width() // 2 + 140, self.pantalla.get_height() // 4 + self.offset_vertical, 40, 40)
        if menos_resolucion_rect.collidepoint(posicion):
            print("Menos resolución clicado")  # Debugging
            self.modificar_opcion(-1)
        elif mas_resolucion_rect.collidepoint(posicion):
            print("Más resolución clicado")  # Debugging
            self.modificar_opcion(1)

        # Check if the music switch is clicked
        musica_switch_rect = pygame.Rect(self.pantalla.get_width() // 2 - 100, self.pantalla.get_height() // 4 + 100 + 80 + self.offset_vertical, 200, 40)
        if musica_switch_rect.collidepoint(posicion):
            if posicion[0] < musica_switch_rect.x + musica_switch_rect.width // 2:
                self.musica_activa = False
            else:
                self.musica_activa = True
            self.reproducir_musica()

        # Check if the effects switch is clicked
        efectos_switch_rect = pygame.Rect(self.pantalla.get_width() // 2 - 100, self.pantalla.get_height() // 4 + 320 + 80 + self.offset_vertical, 200, 40)  # Ajustado para igualar espacio
        if efectos_switch_rect.collidepoint(posicion):
            if posicion[0] < efectos_switch_rect.x + efectos_switch_rect.width // 2:
                self.efectos_activos = False
            else:
                self.efectos_activos = True
            self.reproducir_efecto()

        # Check if volume buttons are clicked
        menos_musica_rect = pygame.Rect(self.pantalla.get_width() // 2 - 120, self.pantalla.get_height() // 4 + 220 + self.offset_vertical, 40, 40)  # Ajustado para igualar espacio
        mas_musica_rect = pygame.Rect(self.pantalla.get_width() // 2 + 80, self.pantalla.get_height() // 4 + 220 + self.offset_vertical, 40, 40)  # Ajustado para igualar espacio
        if menos_musica_rect.collidepoint(posicion):
            self.modificar_opcion_volumen(-1, "musica")
        elif mas_musica_rect.collidepoint(posicion):
            self.modificar_opcion_volumen(1, "musica")

        menos_efectos_rect = pygame.Rect(self.pantalla.get_width() // 2 - 120, self.pantalla.get_height() // 4 + 420 + self.offset_vertical, 40, 40)
        mas_efectos_rect = pygame.Rect(self.pantalla.get_width() // 2 + 80, self.pantalla.get_height() // 4 + 420 + self.offset_vertical, 40, 40)
        if menos_efectos_rect.collidepoint(posicion):
            self.modificar_opcion_volumen(-1, "efectos")
        elif mas_efectos_rect.collidepoint(posicion):
            self.modificar_opcion_volumen(1, "efectos")

        # Check if other menu options are clicked
        for i, opcion in enumerate(self.opciones):
            if opcion == "Volver":
                ancho, alto = self.fuente_opcion.size(opcion)
                rect = pygame.Rect((self.pantalla.get_width() // 2 - ancho // 2, self.pantalla.get_height() - 100 + self.offset_vertical), (ancho, alto))
            else:
                ancho, alto = self.fuente_opcion.size(opcion)
                rect = pygame.Rect((self.pantalla.get_width() // 2 - ancho // 2, self.pantalla.get_height() // 4 + i * 100 + self.offset_vertical), (ancho, alto))
            if rect.collidepoint(posicion):
                self.seleccion = i
                self.ejecutar_opcion()
                break

    def ejecutar_opcion(self):
        if self.opciones[self.seleccion] == "Volver":
            self.corriendo = False
        elif self.opciones[self.seleccion] == "Música":
            self.musica_activa = not self.musica_activa
            self.reproducir_musica()
        elif self.opciones[self.seleccion] == "Efectos":
            self.efectos_activos = not self.efectos_activos
            self.reproducir_efecto()

    def modificar_opcion(self, valor):
        if self.opciones[self.seleccion] == "Resolución":
            self.resolucion_actual = (self.resolucion_actual + valor) % len(self.resoluciones)
            self.cambiar_resolucion()

    def modificar_opcion_volumen(self, valor, tipo):
        if tipo == "musica":
            self.volumen_musica = max(1, min(10, self.volumen_musica + valor))
            pygame.mixer.music.set_volume(self.volumen_musica / 10.0)
        elif tipo == "efectos":
            self.volumen_efectos = max(1, min(10, self.volumen_efectos + valor))
            self.sonido_efecto.set_volume(self.volumen_efectos / 10.0)

    def cambiar_resolucion(self):
        nueva_resolucion = self.resoluciones[self.resolucion_actual]
        self.pantalla = pygame.display.set_mode(nueva_resolucion)

    def actualizar(self):
        pass

    def dibujar(self):
        self.pantalla.fill(NEGRO)
        self.mostrar_menu()
        pygame.display.flip()

    def mostrar_menu(self):
        for i, opcion in enumerate(self.opciones):
            if opcion == "Resolución":
                texto = opcion
                resolucion_texto = f"{self.resoluciones[self.resolucion_actual][0]}x{self.resoluciones[self.resolucion_actual][1]}"
            elif opcion == "Música":
                texto = opcion
            elif opcion == "Volumen Música":
                texto = opcion
                volumen_texto = f"{self.volumen_musica}"
            elif opcion == "Efectos":
                texto = opcion
            elif opcion == "Volumen Efectos":
                texto = opcion
                volumen_texto = f"{self.volumen_efectos}"
            elif opcion == "Volver":
                texto = opcion
            else:
                continue

            color = BLANCO if i == self.seleccion else GRIS
            renderizado = self.fuente_opcion.render(texto, True, color)
            if opcion == "Resolución":
                menos = self.fuente_opcion.render("-", True, ROJO)
                mas = self.fuente_opcion.render("+", True, ROJO)
                resolucion_renderizado = self.fuente_resolucion.render(resolucion_texto, True, color)
                self.pantalla.blit(menos, (self.pantalla.get_width() // 2 - 180, self.pantalla.get_height() // 4 + i * 100 + self.offset_vertical))
                self.pantalla.blit(renderizado, (self.pantalla.get_width() // 2 - renderizado.get_width() // 2, self.pantalla.get_height() // 4 + i * 100 + self.offset_vertical))
                self.pantalla.blit(mas, (self.pantalla.get_width() // 2 + 140, self.pantalla.get_height() // 4 + i * 100 + self.offset_vertical))
                self.pantalla.blit(resolucion_renderizado, (self.pantalla.get_width() // 2 - resolucion_renderizado.get_width() // 2, self.pantalla.get_height() // 4 + i * 100 + 40 + self.offset_vertical))
            elif opcion == "Música":
                self.pantalla.blit(renderizado, (self.pantalla.get_width() // 2 - renderizado.get_width() // 2, self.pantalla.get_height() // 4 + i * 110 + self.offset_vertical))
                switch_color = ROJO if self.musica_activa else GRIS
                switch_rect = pygame.Rect(self.pantalla.get_width() // 2 - 100, self.pantalla.get_height() // 4 + i * 100 + 80 + self.offset_vertical, 200, 40)
                pygame.draw.rect(self.pantalla, GRIS, switch_rect)
                if (self.musica_activa):
                    pygame.draw.rect(self.pantalla, ROJO, (switch_rect.x + switch_rect.width // 2, switch_rect.y, switch_rect.width // 2, switch_rect.height))
                else:
                    pygame.draw.rect(self.pantalla, BLANCO, (switch_rect.x, switch_rect.y, switch_rect.width // 2, switch_rect.height))
            elif opcion == "Volumen Música":
                self.pantalla.blit(renderizado, (self.pantalla.get_width() // 2 - renderizado.get_width() // 2, self.pantalla.get_height() // 4 + i * 100 + 60 + self.offset_vertical))
                menos = self.fuente_opcion.render("-", True, ROJO)
                mas = self.fuente_opcion.render("+", True, ROJO)
                volumen_renderizado = self.fuente_opcion.render(volumen_texto, True, color)
                self.pantalla.blit(menos, (self.pantalla.get_width() // 2 - 120, self.pantalla.get_height() // 4 + i * 100 + 120 + self.offset_vertical))  # Ajustado para igualar espacio
                self.pantalla.blit(volumen_renderizado, (self.pantalla.get_width() // 2 - volumen_renderizado.get_width() // 2, self.pantalla.get_height() // 4 + i * 100 + 120 + self.offset_vertical))  # Ajustado para igualar espacio
                self.pantalla.blit(mas, (self.pantalla.get_width() // 2 + 80, self.pantalla.get_height() // 4 + i * 100 + 120 + self.offset_vertical))  # Ajustado para igualar espacio
            elif opcion == "Efectos":
                self.pantalla.blit(renderizado, (self.pantalla.get_width() // 2 - renderizado.get_width() // 2, self.pantalla.get_height() // 4 + i * 100 + 120 + self.offset_vertical))
                switch_color = ROJO if self.efectos_activos else GRIS
                switch_rect = pygame.Rect(self.pantalla.get_width() // 2 - 100, self.pantalla.get_height() // 4 + i * 100 + 170 + self.offset_vertical, 200, 40)  # Ajustado para igualar espacio
                pygame.draw.rect(self.pantalla, GRIS, switch_rect)
                if (self.efectos_activos):
                    pygame.draw.rect(self.pantalla, ROJO, (switch_rect.x + switch_rect.width // 2, switch_rect.y, switch_rect.width // 2, switch_rect.height))
                else:
                    pygame.draw.rect(self.pantalla, BLANCO, (switch_rect.x, switch_rect.y, switch_rect.width // 2, switch_rect.height))
            elif opcion == "Volumen Efectos":
                self.pantalla.blit(renderizado, (self.pantalla.get_width() // 2 - renderizado.get_width() // 2, self.pantalla.get_height() // 4 + i * 100 + 140 + self.offset_vertical))
                menos = self.fuente_opcion.render("-", True, ROJO)
                mas = self.fuente_opcion.render("+", True, ROJO)
                volumen_renderizado = self.fuente_opcion.render(volumen_texto, True, color)
                self.pantalla.blit(menos, (self.pantalla.get_width() // 2 - 120, self.pantalla.get_height() // 4 + i * 100 + 200 + self.offset_vertical))
                self.pantalla.blit(volumen_renderizado, (self.pantalla.get_width() // 2 - volumen_renderizado.get_width() // 2, self.pantalla.get_height() // 4 + i * 100 + 200 + self.offset_vertical))
                self.pantalla.blit(mas, (self.pantalla.get_width() // 2 + 80, self.pantalla.get_height() // 4 + i * 100 + 200 + self.offset_vertical))
            elif opcion == "Volver":
                self.pantalla.blit(renderizado, (self.pantalla.get_width() // 2 - renderizado.get_width() // 2, self.pantalla.get_height() - 100 + self.offset_vertical))
            else:
                self.pantalla.blit(renderizado, (self.pantalla.get_width() // 2 - renderizado.get_width() // 2, self.pantalla.get_height() // 4 + i * 100 + self.offset_vertical))
