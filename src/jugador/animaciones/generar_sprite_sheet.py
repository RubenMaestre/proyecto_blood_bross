from PIL import Image

# Carga las imágenes individuales
idle_front = Image.open("src/jugador/animaciones/idle/frente.png")
idle_back = Image.open("src/jugador/animaciones/idle/espalda.png")
idle_left = Image.open("src/jugador/animaciones/idle/izquierda.png")
idle_right = Image.open("src/jugador/animaciones/idle/derecha.png")

# Obtén las dimensiones de una de las imágenes individuales (suponiendo que todas tienen el mismo tamaño)
width, height = idle_back.size

# Crea una nueva imagen con suficiente espacio para todas las vistas
sprite_sheet = Image.new("RGBA", (width * 4, height * 1))  # Ajusta el número de filas si es necesario

# Pega las imágenes en el sprite sheet con las posiciones correctas
sprite_sheet.paste(idle_front, (0, 0))
sprite_sheet.paste(idle_back, (width, 0))
sprite_sheet.paste(idle_left, (width * 2, 0))
sprite_sheet.paste(idle_right, (width * 3, 0))  # Ajusta esta posición si agregas más imágenes

# Guarda el sprite sheet
sprite_sheet.save("src/jugador/animaciones/idle/sprite_sheet.png")
