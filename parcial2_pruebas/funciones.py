import random
from Constantes import *
import pygame
import json
import os
from datetime import datetime


#GENERAL
def mezclar_lista(lista_preguntas:list) -> None:
    random.shuffle(lista_preguntas)

#GENERAL
def reiniciar_estadisticas(datos_juego:dict) -> None:
    datos_juego["puntuacion"] = 0
    datos_juego["vidas"] = CANTIDAD_VIDAS
    datos_juego["nombre"] = ""
    datos_juego["tiempo_restante"] = 30
    datos_juego["comodin_bomba"] = False
    datos_juego["comodin_puntos_X2"] = False
    datos_juego["comodin_doble_chance"] = False
    datos_juego["comodin_pasar_pregunta"] = False
    datos_juego["comodin_puntos_X2_usado"] = False
    datos_juego["comodin_pasar_pregunta_usado"] =False
    datos_juego["comodin_doble_chance_usado"] = False
    datos_juego["datos_guardados"] = False




#GENERAL
def verificar_respuesta(datos_juego:dict,pregunta:dict,respuesta:int) -> bool:
    if respuesta == pregunta["respuesta_correcta"]:
        datos_juego["racha"] += 1
        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
        retorno = True
        if datos_juego["racha"] == 5:
            datos_juego["vidas"] += 1
            datos_juego["tiempo_restante"] += 5
            datos_juego["racha"] = 0
        
    else:
        datos_juego["vidas"] -= 1
        datos_juego["puntuacion"] -= PUNTUACION_ERROR
        datos_juego["racha"] = 0
        retorno = False    
        
    return retorno


def crear_elemento_juego(textura:str,ancho:int,alto:int,pos_x:int,pos_y:int) -> dict:
    elemento_juego = {}
    elemento_juego["superficie"] = pygame.transform.scale(pygame.image.load(textura),(ancho,alto))
    elemento_juego["rectangulo"] = elemento_juego["superficie"].get_rect()
    elemento_juego["rectangulo"].x = pos_x
    elemento_juego["rectangulo"].y = pos_y
    
    return elemento_juego

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def crear_respuestas(textura:str,ancho:int,alto:int,pos_x:int,pos_y:int,cantidad_respuestas:int) -> list:
    lista_respuestas = []
    
    for i in range(cantidad_respuestas):
        boton_respuesta = crear_elemento_juego(textura,ancho,alto,pos_x,pos_y)
        lista_respuestas.append(boton_respuesta)
        pos_y += 65
    
    return lista_respuestas

def obtener_respuesta_click(lista_respuestas:list,pos_click:tuple):
    respuesta = None
    
    for i in range(len(lista_respuestas)):
        if lista_respuestas[i]["rectangulo"].collidepoint(pos_click):
            respuesta = i + 1
    
    return respuesta

def limpiar_superficie(elemento_juego:dict,textura:str,ancho:int,alto:int) -> None:
    elemento_juego["superficie"] =  pygame.transform.scale(pygame.image.load(textura),(ancho,alto))

def cambiar_pregunta(lista_preguntas:list,indice:int,caja_pregunta:dict,lista_respuestas:list) -> dict:
    pregunta_actual = lista_preguntas[indice]
    limpiar_superficie(caja_pregunta,"textura_pregunta.png",ANCHO_PREGUNTA,ALTO_PREGUNTA)
    for i in range(len(lista_respuestas)):
        limpiar_superficie(lista_respuestas[i],"textura_respuesta.png",ANCHO_BOTON,ALTO_BOTON)
    
    return pregunta_actual

def crear_botones_menu() -> list:
    lista_botones = []
    pos_y = 115

    for i in range(4):
        boton = crear_elemento_juego("textura_boton_menu.png",ANCHO_BOTON_MENU,ALTO_BOTON_MENU,80,pos_y)
        pos_y += 80
        lista_botones.append(boton)
    
    return lista_botones

def aplicar_volumen_sonidos(volumen: float)->None:
    CLICK_SONIDO.set_volume(volumen)
    ERROR_SONIDO.set_volume(volumen)
    CORRECTO_SONITO.set_volume(volumen)
    GAME_OVER_SOUND.set_volume(volumen)

def manejar_texto(cuadro_texto:dict,tecla_presionada:str,bloc_mayus:int,datos_juego:dict) -> None:
    #Cuando se toca un espacio
    if tecla_presionada == "space":
        CLICK_SONIDO.play()
        datos_juego["nombre"] += " "
    
    #Cuando se toca el boton borrar
    if tecla_presionada == "backspace" and len(datos_juego["nombre"]) > 0:
        datos_juego["nombre"] = datos_juego["nombre"][0:len(datos_juego["nombre"]) - 1]
        limpiar_superficie(cuadro_texto,"textura_terminado.png",ANCHO_CUADRO,ALTO_CUADRO)
    
    #Cuando se toca un caracter
    if len(tecla_presionada) == 1: 
        CLICK_SONIDO.play()
        #ESTA ACTIVO EL BLOC MAYUSCULA
        if bloc_mayus == 8192 or bloc_mayus == 1 or bloc_mayus == 2:          
            datos_juego["nombre"] += tecla_presionada.upper()
        else:
            datos_juego["nombre"] += tecla_presionada

def eliminar_dos_incorrectas(pregunta: dict) -> list:
    respuestas_visibles = []
    incorrectas = []

    indice_correcta = pregunta["respuesta_correcta"]
    respuestas_visibles.append(f"respuesta_{indice_correcta}")

    for i in range(1, 5):
        if i != indice_correcta:
            incorrectas.append(i)
    incorrecta_random = random.choice(incorrectas)
    respuestas_visibles.append(f"respuesta_{incorrecta_random}")

    return respuestas_visibles


def saltar_pregunta(datos_juego: dict, lista_preguntas: list, caja_pregunta: dict, lista_respuestas: list) -> dict:
    
    pregunta_nueva = {}

    datos_juego["comodin_pasar_pregunta"] = True
    datos_juego["comodin_pasar_pregunta_usado"] = True

    datos_juego['indice'] += 1
    if datos_juego['indice'] == len(lista_preguntas):
        mezclar_lista(lista_preguntas)
        datos_juego['indice'] = 0

    datos_juego["respuestas_a_mostrar"] = ["respuesta_1", "respuesta_2", "respuesta_3", "respuesta_4"]
    pregunta_nueva = cambiar_pregunta(lista_preguntas, datos_juego['indice'], caja_pregunta, lista_respuestas)
    return pregunta_nueva

def guardar_datos_partida_en_diccionario(datos_juego:dict, fecha_actual:str)->dict:
    
    diccionario_datos_partida = {
        "nombre": datos_juego["nombre"],
        "puntuacion": datos_juego["puntuacion"],
        "fecha": fecha_actual
    }

    return diccionario_datos_partida

def leer_json(nombre_archivo:str) -> list:
    try:
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo,"r") as archivo:
                lista = json.load(archivo)
        else:
            lista = []
    except:
        lista = []
    return lista

def guardar_json(nombre_archivo:str, lista:list) -> bool:
    if type(lista) == list and len(lista) > 0:
        with open(nombre_archivo,"w") as archivo:
            json.dump(lista, archivo, indent=4)
        retorno = True
    else:
        retorno = False
    return retorno

def guardar_partida(datos_juego:dict, nombre_archivo:str, fecha_actual:str):
    partidas = leer_json(nombre_archivo)
    nueva_partida = guardar_datos_partida_en_diccionario(datos_juego,fecha_actual)
    partidas.append(nueva_partida)
    guardar = guardar_json(nombre_archivo,partidas)

    return guardar

def validar_letras_y_espacios(cadena: str) -> bool:

    if type(cadena) == str and len(cadena) > 0:
        retorno = True
        for i in range(len(cadena)):
            codigo_ascii = ord(cadena[i])
            if not ((codigo_ascii == 32) or (65 <= codigo_ascii <= 90) or (97 <= codigo_ascii <= 122)):
                retorno = False
                break
    else:
        retorno = False
    return retorno

def obtener_fecha_actual()->str:
    fecha = datetime.now()
    fecha_actual = fecha.strftime("%d-%m-%Y")

    return fecha_actual

def obtener_puntuacion(partida):
    return partida["puntuacion"]

def obtener_top_10(nombre_archivo:str) -> list| bool:
    lista_top_10 = []
    lista_partidas = leer_json(nombre_archivo)
    if len(lista_partidas) > 0:
        lista_partidas.sort(key=obtener_puntuacion)
        lista_partidas.reverse()
        if len(lista_partidas) > 10:
            lista_top_10 = lista_partidas[0:10]
        else:
            lista_top_10 = lista_partidas

        retorno = lista_top_10
    else:
        retorno = False
    
    return retorno


def preparar_texto_ranking(lista_top_10:list)->str:
    texto = ""
    if type(lista_top_10) == list:
        for i in range(len(lista_top_10)):
            texto += f"{i+1}.Nombre:{lista_top_10[i]['nombre']} - Puntuacion:{lista_top_10[i]['puntuacion']} - Fecha:{lista_top_10[i]['fecha']}\n"
    return texto

def crear_diccionario_preguntas(linea:str,separador:str = ",") -> dict:
    #print(linea,end="")
    linea = linea.replace("\n","")
    lista_datos = linea.split(separador)
    
    pregunta = {}
    pregunta["pregunta"] = lista_datos[0]
    pregunta["respuesta_1"] = lista_datos[1]
    pregunta["respuesta_2"] = lista_datos[2]
    pregunta["respuesta_3"] = lista_datos[3]
    pregunta["respuesta_4"] = lista_datos[4]
    pregunta["respuesta_correcta"]= int(lista_datos[5])
    
    return pregunta

def leer_csv_preguntas(nombre_archivo:str,lista_preguntas:list,separador:str = ",") -> bool:
    if os.path.exists(nombre_archivo) == True: 
        with open(nombre_archivo,"r") as archivo:
            #Falsa lectura
            archivo.readline()

            for linea in archivo:
                pregunta = crear_diccionario_preguntas(linea,separador)
                lista_preguntas.append(pregunta)
        
        retorno = True
    else:
        retorno = False
        
    return retorno







