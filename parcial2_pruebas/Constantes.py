import pygame
pygame.init()

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
ANCHO = 500
ALTO = 500
PANTALLA = (ANCHO,ALTO)
FPS = 30

BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_PUNTUACIONES = 2
BOTON_SALIR = 3

ANCHO_PREGUNTA = 450
ALTO_PREGUNTA = 220
TAMANO_PREGUNTA = (ANCHO_PREGUNTA, ALTO_PREGUNTA)
ANCHO_BOTON = 250
ALTO_BOTON = 80
ANCHO_BOTON_MENU = 350
ALTO_BOTON_MENU = 90

ANCHO_CUADRO = 400
ALTO_CUADRO = 90

TAMAÑO_BOTON_VOLUMEN = (60,60)
TAMAÑO_BOTON_VOLVER = (100,40)
CLICK_SONIDO = pygame.mixer.Sound("click.mp3")
CORRECTO_SONITO = pygame.mixer.Sound("correcto.mp3")
ERROR_SONIDO = pygame.mixer.Sound("error.mp3")
GAME_OVER_SOUND = pygame.mixer.Sound("fail_sound.mp3")
FUENTE_PREGUNTA = pygame.font.SysFont("comicsansms",25,True)
FUENTE_RESPUESTA = pygame.font.SysFont("comicsansms",20,True)
FUENTE_TEXTO = pygame.font.SysFont("Arial",19,True)
FUENTE_VOLUMEN = pygame.font.SysFont("Arial",30,True)
FUENTE_CUADRO_TEXTO = pygame.font.SysFont("Arial",40,True)
FUENTE_TEXTO_MENU = pygame.font.SysFont("comicsansms",30,True)
FUENTE_MUTE = pygame.font.SysFont("Arial",20,True)
FUENTE_RANKING = pygame.font.SysFont("comicsansms",50,True)
FUENTE_LISTA_TOP_10 = pygame.font.SysFont("comicsansms",15,True)

BOTON_JUGAR = 0

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25
CANTIDAD_TIEMPO = 30

