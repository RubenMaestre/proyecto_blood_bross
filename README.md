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

## Pantalla de introducción y menú principal

El juego comienza con una pantalla de presentación que muestra el logo y el título del juego. Esta introducción utiliza varias imágenes que se alternan para crear una experiencia visual atractiva mientras se reproduce música de fondo. 

### Detalles del menú

Desde el menú principal, puedes seleccionar entre varias opciones:

- **Nueva Partida**: Inicia una nueva partida desde el comienzo. Al seleccionar esta opción, se reproduce un video introductorio antes de comenzar la primera misión.
- **Cargar Partida**: (Funcionalidad futura) Permitirá cargar una partida guardada.
- **Opciones**: Aquí puedes ajustar varias configuraciones del juego, como controles, volumen de la música y efectos de sonido.
- **Salir**: Cierra el juego de manera segura.

### Navegación del menú

La navegación por el menú está diseñada para ser fluida y fácil de usar. Puedes usar tanto el teclado como el ratón para interactuar con las opciones disponibles:

- **Teclado**: Usa las flechas arriba y abajo para moverte entre las opciones del menú, y presiona Enter para seleccionar una opción.
- **Ratón**: Haz clic en las opciones del menú para seleccionarlas directamente.

### Transiciones y música

Para una experiencia de usuario más inmersiva, las transiciones entre las pantallas del menú y el juego son suaves. La música del menú se reproduce aleatoriamente entre varios archivos, creando una atmósfera dinámica cada vez que accedes al menú.

Al seleccionar "Nueva Partida", además de reproducirse un video introductorio, la música del menú se desvanece gradualmente, y se inicia la música del juego. Esto proporciona una transición auditiva suave entre las distintas fases del juego.


## Desarrollo del jugador

El jugador en **Rogue Hunter** tiene una variedad de habilidades que lo hacen dinámico y entretenido de controlar. Puede moverse horizontalmente y tiene la capacidad de rodar para evitar ataques enemigos. Además, el jugador puede apuntar y disparar moviendo el visor por la pantalla, lo que añade un elemento estratégico al juego.

### Habilidades del jugador

- **Movimiento**: El jugador puede moverse hacia la izquierda y derecha utilizando las flechas del teclado.
- **Rodar**: Presionando la barra espaciadora, el jugador puede rodar, lo que le permite esquivar ataques enemigos.
- **Disparo**: Usando la tecla `Z`, el jugador puede disparar. El visor, controlado con las teclas `WASD`, permite apuntar y disparar con precisión.

### Disparador

El jugador no solo puede moverse horizontalmente, sino que también puede mover el disparador por toda la pantalla para atacar a los enemigos de manera efectiva. Esto se logra mediante el control del disparador con las teclas `WASD`, permitiendo al jugador una mayor flexibilidad y precisión en el combate.

### Animaciones del jugador

El jugador cuenta con varias animaciones que hacen que sus movimientos sean más realistas y atractivos:
- **Correr**: Animación para cuando el jugador se desplaza horizontalmente.
- **Disparar**: Animación que se activa al presionar la tecla de disparo.
- **Rodar**: Animación especial que se activa cuando el jugador realiza una voltereta.

### Salud y puntuación

El jugador tiene una barra de salud que se reduce cuando recibe daño de los enemigos. Además, hay un sistema de puntuación que incrementa al derrotar enemigos, añadiendo un desafío adicional para el jugador.

## Desarrollo de enemigos

Los enemigos en **Rogue Hunter** están diseñados para ofrecer una experiencia de juego desafiante y variada. Cada enemigo tiene diferentes velocidades de disparo y puntería, lo que requiere que el jugador adapte su estrategia constantemente.

### Inteligencia Artificial

Los enemigos utilizan una IA básica que les permite:
- **Patrullar**: Moverse por el nivel de manera predefinida.
- **Atacar**: Detectar y atacar al jugador cuando está en rango.
- **Reaccionar**: Cambiar su comportamiento basado en las acciones del jugador, evitando patrones predecibles.

### Animaciones de los enemigos

Los enemigos cuentan con animaciones para:
- **Movimiento**: Caminan o corren hacia el jugador.
- **Disparo**: Animación que se activa al atacar al jugador.

### Jefe final

En el nivel 10 de cada misión, el jugador se enfrentará a un líder de la mafia, un enemigo especial con habilidades únicas que hacen cada enfrentamiento final más emocionante y desafiante.

## Diseño de niveles y escenarios

Cada nivel en **Rogue Hunter** tiene mapas y fondos diseñados específicamente para representar diferentes países. Estos escenarios incluyen:

### Elementos interactivos

- **Obstáculos**: Elementos del entorno que el jugador debe esquivar o superar.
- **Coberturas**: Objetos detrás de los cuales el jugador puede esconderse para evitar disparos enemigos.
- **Elementos destructibles**: Objetos que pueden ser destruidos durante el combate, añadiendo una capa extra de estrategia.

### Lógica de progresión

La progresión de niveles asegura que el jugador avance al siguiente nivel al derrotar a todos los enemigos presentes en el nivel actual. Esto proporciona una estructura clara y un objetivo para cada nivel, manteniendo al jugador motivado y comprometido.

## Sistema de combate y puntuación

El sistema de combate en **Rogue Hunter** es esencial para la jugabilidad y ofrece varias características:

### Tipos de armas

- **Disparos básicos**: Disponibles desde el inicio del juego.
- **Armas especiales**: Desbloqueables a medida que el jugador avanza en el juego.

### Interacciones de combate

Las interacciones de combate entre el jugador y los enemigos son fundamentales para el juego. El jugador debe esquivar, atacar y utilizar el entorno a su favor para vencer.

### Sistema de puntuación

El sistema de puntuación estará basado en (aún no está implementado):
- **Enemigos derrotados**: Cada enemigo derrotado añade puntos.
- **Objetivos cumplidos**: Completar niveles y misiones otorga bonificaciones adicionales.

## Interfaz de usuario (UI)

La interfaz de usuario en **Rogue Hunter** está diseñada para proporcionar al jugador toda la información necesaria de manera clara y accesible.

### HUD (Head-Up Display)

El HUD muestra información esencial para el jugador:
- **Salud**: Una barra de salud que indica cuánta vida le queda al jugador.
- **Munición**: Información sobre el tipo de munición disponible.
- **Puntuación**: La puntuación actual del jugador, basada en los enemigos derrotados y los objetivos cumplidos.

### Menús de pausa y opciones

Durante el juego, puedes acceder a menús de pausa y opciones que te permiten:
- **Ajustar controles**: Cambiar las configuraciones de los controles según tus preferencias.
- **Ajustar volumen**: Modificar el volumen de la música y los efectos de sonido.

### Pantalla de fin de nivel

Al final de cada nivel, se muestra una pantalla con los resultados:
- **Puntuación final**: La puntuación total obtenida en el nivel.
- **Objetivos cumplidos**: Información sobre los objetivos completados durante el nivel.
- **Opciones de continuar o salir**: Puedes elegir avanzar al siguiente nivel o salir al menú principal.

## Sonido y música

El sonido y la música en **Rogue Hunter** están diseñados para mejorar la inmersión del jugador en el juego.

### Efectos de sonido

- **Disparos**: Efectos sonoros cada vez que el jugador o los enemigos disparan.
- **Explosiones**: Sonidos que acompañan las explosiones en el juego.
- **Saltos**: Efectos de sonido para cuando el jugador realiza saltos o volteretas.

### Música de fondo

Cada nivel y menú tiene su propia música de fondo para establecer el ambiente adecuado. Hay opciones para ajustar el volumen de la música según tus preferencias.

## Cómo jugar

Para jugar a **Rogue Hunter**, simplemente ejecuta el archivo `principal.py` que se encuentra en el directorio `src`.

## Controles del juego
- **Movimiento**: Usa las teclas de flecha izquierda y derecha para moverte.
- **Disparador**: Se mueve con las teclas A, S, D, W.
- **Disparo**: Presiona la tecla Z para disparar.
- **Rodar**: La barra espaciadora te permite rodar para esquivar ataques.
- **Pausa**: Puedes pausar el juego con la tecla ESC.
- **Reiniciar**: En la pantalla de fin de partida, presiona R para reiniciar.
- **Salir**: En la pantalla de fin de partida, presiona Q para salir.

## Estado actual del proyecto

Hasta ahora, he logrado arrancar el juego perfectamente y definir al jugador, los enemigos y la misión 1, pantalla 1. Aunque aún queda mucho por hacer, ya tengo una base sólida sobre la cual seguir construyendo. El juego cuenta con una estructura funcional y una jugabilidad básica que sienta las bases para futuras expansiones y mejoras.

## Futuro del proyecto

El objetivo que me he marcado es llevar **Rogue Hunter** a plataformas móviles. Aunque esta parte aún está en desarrollo y requiere más trabajo, mi idea es crear un producto de alta calidad. Estoy trabajando para optimizar el rendimiento y adaptar la jugabilidad a dispositivos móviles, con la esperanza de ofrecer una experiencia fluida y atractiva en el futuro.
