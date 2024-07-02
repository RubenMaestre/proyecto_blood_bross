# Blood Bros Style Game

Este proyecto surge de la idea de construir un juego inspirado en el clásico Blood Bros para poner en práctica mis conocimientos de Python y la librería Pygame. Inicialmente, mi objetivo era seguir practicando con Pygame para un proyecto más grande, PCFutsal, que está actualmente en pausa debido al verano. Pensé que desarrollar un juego arcade sería sencillo, pero pronto descubrí que es una tarea más compleja de lo que imaginaba.

## Planificación y concepto general

Comencé con la planificación y el concepto general del juego. La idea principal es un profesional del ejército harto de las injusticias sociales que decide tomarse la justicia por su cuenta enfrentándose a diversas mafias alrededor del mundo. Cada misión consta de 10 pantallas, empezando por la más fácil y culminando en la décima con un enfrentamiento contra un jefe final. La temática del juego incluye viajar por distintos países y enfrentarse a las mafias locales, como la italiana, la rusa, la yakuza japonesa, entre otras.

Con este concepto en mente, esbocé la estructura básica del juego y empecé a construirlo. La planificación inicial incluyó definir la historia y los personajes, crear un guion gráfico básico de los niveles y la progresión, y listar los recursos necesarios como imágenes, sonidos y música.


### Descripción General de las Carpetas y Archivos

- **recursos**: Contiene todos los archivos multimedia utilizados en el juego.
  - **disparadores**: Imágenes y recursos relacionados con los disparos.
  - **fuentes**: Fuentes utilizadas en el juego.
  - **imagenes**: Todas las imágenes necesarias para el juego, como sprites y fondos.
  - **sonidos**: Efectos de sonido y música de fondo.
  - **videos**: Videos introductorios o de escenas del juego.

- **src**: Contiene todo el código fuente del juego.
  - **datos**: Módulos relacionados con el manejo y almacenamiento de datos del juego.
  - **enemigos**: Definiciones y comportamientos de los diferentes enemigos en el juego.
  - **jugador**: Lógica y animaciones relacionadas con el jugador.
  - **niveles**: Configuración y diseño de los niveles del juego.
  - **configuracion.py**: Archivo de configuración con parámetros globales del juego.
  - **enemigo.py**: Módulo que define las clases y funciones para manejar los enemigos.
  - **interfaz.py**: Maneja la interfaz de usuario del juego.
  - **juego.py**: Lógica principal del juego.
  - **jugador.py**: Módulo que define las clases y funciones para manejar al jugador.
  - **menu.py**: Implementación del menú principal del juego.
  - **nivel.py**: Configuración y lógica para los niveles del juego.
  - **opciones_usuario.py**: Manejo de las opciones configurables por el usuario.
  - **principal.py**: Archivo principal que inicia el juego.
  - **utilidades.py**: Funciones utilitarias y auxiliares utilizadas en todo el proyecto.

