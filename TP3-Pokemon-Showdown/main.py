from pelea import *
import gamelib
from archivos import *
from logica_gamelib import *
ANCHO_VENTANA = 1200
ALTO_VENTANA = 1200


def main():
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)
    jugador1, jugador2 = pedir_jugadores()
    equipo1 = elegir_equipo(jugador1)
    equipo2 = elegir_equipo(jugador2)
    elegir_pokemon_activo(equipo1)
    elegir_pokemon_activo(equipo2)
    pelea = Pelea(equipo1.pokemon_activo, equipo2.pokemon_activo)
    
    while gamelib.is_alive(): 

        gamelib.title('Batalla Pokemon')
        gamelib.draw_begin()
        
        if not validar_turno(equipo1) or not validar_turno(equipo2):
            break
        
        mostrar_campo_batalla(equipo1, equipo2)
        pedir_accion(equipo1)
        pedir_accion(equipo2)
        manejar_acciones(equipo1, equipo2, pelea)
        gamelib.draw_end()

        ev = gamelib.wait()

        if not ev:
            break
        
        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            break
       
gamelib.init(main)