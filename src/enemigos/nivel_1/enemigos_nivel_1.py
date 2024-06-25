# enemigos/nivel_1/enemigos_nivel_1.py

from src.enemigos.enemigo import Enemigo

class EnemigoBasico(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y, "basico")
        self.salud = 50  # Menos salud para un enemigo básico
        self.velocidad = 2  # Velocidad de movimiento
        self.punteria = 0.5  # Precisión del disparo

class EnemigoRapido(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y, "rapido")
        self.salud = 30  # Menos salud para un enemigo rápido
        self.velocidad = 5  # Mayor velocidad de movimiento
        self.punteria = 0.3  # Menor precisión del disparo

class LiderMafia(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y, "lider")
        self.salud = 200  # Más salud para el líder
        self.velocidad = 3  # Velocidad moderada
        self.punteria = 0.8  # Alta precisión del disparo
        self.habilidades_unicas = True  # Indicador de habilidades únicas
