import pygame
from Constantes import *
from funciones import *


pygame.init()
fondo_menu = pygame.transform.scale(pygame.image.load("fondo.jpg"),PANTALLA)
lista_botones = crear_botones_menu()


def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "menu"
    #Gestionar Eventos
    for evento in cola_eventos:
        #Actualizaciones
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                for i in range(len(lista_botones)):
                    if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                        if i == BOTON_JUGAR:
                            CLICK_SONIDO.play()
                            retorno = "juego"
                        elif i == BOTON_PUNTUACIONES:
                            CLICK_SONIDO.play()
                            retorno = "rankings"
                        elif i == BOTON_CONFIG:
                            CLICK_SONIDO.play()
                            retorno = "ajustes"
                        else:
                            CLICK_SONIDO.play()
                            retorno = "salir"



    pantalla.blit(fondo_menu,(0,0))
    for i in range(len(lista_botones)):
        pantalla.blit(lista_botones[i]["superficie"],lista_botones[i]["rectangulo"])
        
    mostrar_texto(lista_botones[BOTON_JUGAR]["superficie"],"JUGAR",(110,20),FUENTE_TEXTO_MENU,COLOR_NEGRO)
    mostrar_texto(lista_botones[BOTON_PUNTUACIONES]["superficie"],"RANKINGS",(110,20),FUENTE_TEXTO_MENU,COLOR_NEGRO)
    mostrar_texto(lista_botones[BOTON_CONFIG]["superficie"],"AJUSTES",(110,20),FUENTE_TEXTO_MENU,COLOR_NEGRO)
    mostrar_texto(lista_botones[BOTON_SALIR]["superficie"],"SALIR",(110,20),FUENTE_TEXTO_MENU,COLOR_NEGRO)

    return retorno
