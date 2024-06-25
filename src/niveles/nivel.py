# niveles/nivel.py

from src.niveles.pantalla import Pantalla

class Nivel:
    def __init__(self, numero):
        self.numero = numero
        self.pantallas = [Pantalla(i + 1) for i in range(10)]

    def desbloquear(self):
        # Lógica para desbloquear el nivel
        pass

    def esta_desbloqueado(self):
        # Lógica para comprobar si el nivel está desbloqueado
        pass

    def avanzar_pantalla(self):
        # Lógica para avanzar a la siguiente pantalla
        pass
