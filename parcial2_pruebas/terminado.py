import pygame
from Constantes import *
from funciones import *
import json
import os
from datetime import datetime


pygame.init()

cuadro_texto = crear_elemento_juego("textura_terminado.png",ANCHO_CUADRO,ALTO_CUADRO,60,200)
fondo_terminado = pygame.transform.scale(pygame.image.load("fondo_game_over.png"),PANTALLA)
boton_guardar = crear_elemento_juego("textura_boton_menu.png",150,50,175,300)
boton_reintentar = crear_elemento_juego("textura_boton_menu.png",150,50,175,350)
boton_ranking = crear_elemento_juego("textura_boton_menu.png",150,50,175,400)
boton_volver = crear_elemento_juego("textura_boton_menu.png",150,50,175,450)


def mostrar_fin_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict,lista_rankings:list) -> str:
    retorno = "terminado"
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_volver["rectangulo"].collidepoint(evento.pos):
                    limpiar_superficie(cuadro_texto,"textura_terminado.png",ANCHO_CUADRO,ALTO_CUADRO)
                    retorno = "menu"
                    CLICK_SONIDO.play()
                elif boton_reintentar["rectangulo"].collidepoint(evento.pos):
                    limpiar_superficie(cuadro_texto,"textura_terminado.png",ANCHO_CUADRO,ALTO_CUADRO)
                    retorno = "juego" 
                    CLICK_SONIDO.play()
            
                elif boton_guardar["rectangulo"].collidepoint(evento.pos):
                    if validar_letras_y_espacios(datos_juego["nombre"]) == True and datos_juego["datos_guardados"] == False:
                        fecha_actual = obtener_fecha_actual()
                        if guardar_partida(datos_juego,"partidas.json",fecha_actual):
                            datos_juego["datos_guardados"] = True
                            CORRECTO_SONITO.play()
                            print("guardado exitoso")
                        else:
                            ERROR_SONIDO.play()
                            print("error de guardado")
                        
                    else:
                        print("error")
                        ERROR_SONIDO.play()
                elif boton_ranking["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "rankings"

        elif evento.type == pygame.KEYDOWN:
            tecla_presionada = pygame.key.name(evento.key)    
            bloc_mayus = pygame.key.get_mods()
            
            manejar_texto(cuadro_texto,tecla_presionada,bloc_mayus,datos_juego)  

    


    if datos_juego["nombre"] != "":
        limpiar_superficie(cuadro_texto,"textura_terminado.png",ANCHO_CUADRO,ALTO_CUADRO)
        mostrar_texto(cuadro_texto["superficie"],f"{datos_juego['nombre']}",(50,10),FUENTE_CUADRO_TEXTO,COLOR_NEGRO)
        
        if random.randint(1,2) == 1:
            mostrar_texto(cuadro_texto["superficie"],f"{datos_juego['nombre']}|",(50,10),FUENTE_CUADRO_TEXTO,COLOR_AZUL)
        
    else:
        mostrar_texto(cuadro_texto["superficie"],"INGRESE SU NOMBRE",(50,20),FUENTE_RESPUESTA,"#736767")
    
    pantalla.blit(fondo_terminado,(0,0))
    pantalla.blit(cuadro_texto["superficie"],cuadro_texto["rectangulo"])
    pantalla.blit(boton_guardar["superficie"], boton_guardar["rectangulo"])
    pantalla.blit(boton_volver["superficie"], boton_volver["rectangulo"])
    pantalla.blit(boton_reintentar["superficie"], boton_reintentar["rectangulo"])
    pantalla.blit(boton_ranking["superficie"], boton_ranking["rectangulo"])

    mostrar_texto(pantalla,f"Usted obtuvo: {datos_juego['puntuacion']} puntos",(220,20),FUENTE_PREGUNTA,COLOR_NEGRO)
    mostrar_texto(boton_guardar["superficie"],"Guardar",(25,10),FUENTE_RESPUESTA,COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"],"Volver menu",(10,10),FUENTE_RESPUESTA,COLOR_NEGRO)
    mostrar_texto(boton_reintentar["superficie"],"Volver jugar",(10,10),FUENTE_RESPUESTA,COLOR_NEGRO)
    mostrar_texto(boton_ranking["superficie"],"Rankings",(25,10),FUENTE_RESPUESTA,COLOR_NEGRO)




    
    
    return retorno 
