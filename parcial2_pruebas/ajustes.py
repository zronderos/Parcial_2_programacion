import pygame
from Constantes import *
from funciones import *

pygame.init()

datos_juego = {"puntuacion":0,"vidas":CANTIDAD_VIDAS,"nombre":"","tiempo_restante":CANTIDAD_TIEMPO,"indice":0,"volumen_musica":5, "racha":0, "volumen_sonidos":10, "musica_activada": True,"comodin_bomba":False, "comodin_puntos_X2":False, "comodin_doble_chance": False, "comodin_pasar_pregunta":False}

boton_suma_musica = crear_elemento_juego("mas.webp",60,60,420,100)
boton_suma_sonidos = crear_elemento_juego("mas.webp",60,60,420,200)
boton_resta_musica = crear_elemento_juego("menos.webp",60,60,20,100)
boton_resta_sonidos = crear_elemento_juego("menos.webp",60,60,20,200)
boton_volver = crear_elemento_juego("textura_boton_menu.png",100,40,10,10)

if datos_juego["musica_activada"]:
    boton_mute = crear_elemento_juego("ON_SPEAKER.png", 80, 80, 400, 400)
else:
    boton_mute = crear_elemento_juego("OFF_SPEAKER.png", 80, 80, 400, 400)



fondo_ajustes = pygame.transform.scale(pygame.image.load("fondo.jpg"),PANTALLA)

def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "ajustes"
    bandera_OFF = False
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_suma_musica["rectangulo"].collidepoint(evento.pos):
                    if datos_juego["volumen_musica"] <= 95:
                        datos_juego["volumen_musica"] += 5
                        CLICK_SONIDO.play()
                    else:
                        ERROR_SONIDO.play()
                elif boton_resta_musica["rectangulo"].collidepoint(evento.pos):
                    if datos_juego["volumen_musica"] > 0:
                        datos_juego["volumen_musica"] -= 5
                        CLICK_SONIDO.play()
                    else: 
                        ERROR_SONIDO.play()
                elif boton_suma_sonidos["rectangulo"].collidepoint(evento.pos):
                    if datos_juego["volumen_sonidos"] <= 95:
                        datos_juego["volumen_sonidos"] += 5
                        porcentaje_volumen_sonidos = datos_juego["volumen_sonidos"] / 100
                        aplicar_volumen_sonidos(porcentaje_volumen_sonidos)
                        CLICK_SONIDO.play()
                    else:
                        ERROR_SONIDO.play()
                elif boton_resta_sonidos["rectangulo"].collidepoint(evento.pos):
                    if datos_juego["volumen_sonidos"] > 0:
                        datos_juego["volumen_sonidos"] -= 5
                        porcentaje_volumen_sonidos = datos_juego["volumen_sonidos"] / 100
                        aplicar_volumen_sonidos(porcentaje_volumen_sonidos)
                        CLICK_SONIDO.play()
                    else:
                        ERROR_SONIDO.play()
                elif boton_mute["rectangulo"].collidepoint(evento.pos):
                    if datos_juego["musica_activada"]:
                        pygame.mixer.music.stop()
                        datos_juego["musica_activada"] = False
                        boton_mute["superficie"] = pygame.transform.scale(pygame.image.load("OFF_SPEAKER.png"), (80, 80))
                    else:
                        datos_juego["musica_activada"] = True
                        boton_mute["superficie"] = pygame.transform.scale(pygame.image.load("ON_SPEAKER.png"), (80, 80))
                    

                elif boton_volver["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "menu"
    
    pantalla.blit(fondo_ajustes,(0,0))
    
    pantalla.blit(boton_suma_musica["superficie"],boton_suma_musica["rectangulo"])
    pantalla.blit(boton_resta_musica["superficie"],boton_resta_musica["rectangulo"])
    pantalla.blit(boton_suma_sonidos["superficie"],boton_suma_sonidos["rectangulo"])
    pantalla.blit(boton_resta_sonidos["superficie"],boton_resta_sonidos["rectangulo"])
    pantalla.blit(boton_mute["superficie"], boton_mute["rectangulo"])
    pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])

    
    mostrar_texto(pantalla,f"volumen musica:{datos_juego['volumen_musica']} %",(120,110),FUENTE_VOLUMEN,COLOR_NEGRO)
    mostrar_texto(pantalla,f"volumen sonidos:{datos_juego['volumen_sonidos']} %",(120,210),FUENTE_VOLUMEN,COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_RESPUESTA,COLOR_NEGRO)
    mostrar_texto(pantalla,"Mutear-Desmutear",(350,470),FUENTE_MUTE,COLOR_NEGRO)

    return retorno