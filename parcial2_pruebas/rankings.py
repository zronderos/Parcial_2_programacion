import pygame
from Constantes import *
from funciones import *

pygame.init()

boton_volver = crear_elemento_juego("textura_boton_menu.png",100,40,10,10)
fondo_rankings = pygame.transform.scale(pygame.image.load("fondo.jpg"),PANTALLA)
textura_rankings = crear_elemento_juego("textura_pregunta.png",500,500,0,0)


def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],lista_rankings:list) -> str:

    retorno = "rankings"
    lista_top_10 = obtener_top_10("partidas.json")
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_volver["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "menu"
    
    pantalla.blit(fondo_rankings,(0,0))
    pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])
    pantalla.blit(textura_rankings["superficie"],textura_rankings["rectangulo"])
    #limpiar_superficie(textura_rankings, "textura_pregunta.png", 500, 500)
    mostrar_texto(pantalla,f"***TOP 10***",(80,80),FUENTE_RANKING,COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_RESPUESTA,COLOR_NEGRO)
    mostrar_texto(pantalla,preparar_texto_ranking(lista_top_10),(40,150),FUENTE_LISTA_TOP_10,COLOR_NEGRO)


    return retorno