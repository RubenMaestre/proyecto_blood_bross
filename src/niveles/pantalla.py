# niveles/pantalla.py

from src.niveles.nivel_1.escenario import Escenario

class Pantalla:
    def __init__(self, numero):
        self.numero = numero
        self.escenario = Escenario()

    def cargar(self):
        # Lógica para cargar la pantalla
        pass

    def completar(self):
        # Lógica para completar la pantalla
        pass

    def dibujar(self, pantalla):
        self.escenario.dibujar(pantalla)
