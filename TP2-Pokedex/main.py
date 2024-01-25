from pokedex_pokemones import *
from pokedex_equipos import *
from archivos import *
import gamelib
from logica_gamelib import * 
from pokedex_activo import * 
ANCHO_VENTANA = 1200
ALTO_VENTANA = 800


def main():
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    activo = Pokedex()
    actual = activo.devolver_actual()

    try:
        activo.equipos.equipos = traer_equipos()  
    except:
        pass

    while gamelib.is_alive(): 

        gamelib.title('Pokedex')
        gamelib.draw_begin()
        mostrar_pokedex(actual)

        activo.dibujar()

        gamelib.draw_end()

        ev = gamelib.wait()

        if not ev:
            guardar_equipos(activo.devolver_equipos())
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Right': 
            activo.siguiente()
        
        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Left':
            activo.anterior()
        
        if ev.type == gamelib.EventType.KeyPress and ev.key in 'bB':
            activo.borrar_o_buscar()
        
        if ev.type == gamelib.EventType.KeyPress and ev.key in 'aA':
            activo.agregar()
        
        if ev.type == gamelib.EventType.KeyPress and ev.key in 'vV':
            activo.cambiar_actual()
            actual = activo.devolver_actual()
        
        if ev.type == gamelib.EventType.KeyPress and ev.key in 'cC':
            activo.crear()

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            guardar_equipos(activo.devolver_equipos())
            break
       
gamelib.init(main)