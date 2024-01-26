from archivos import *
import gamelib
POKE_WIDTH = 210


def pedir_jugadores():
    jugador1 = gamelib.input("Indique el nombre del primer jugador")
    jugador2 = gamelib.input("Indique el nombre del segundo jugador")
    if not jugador1:
        jugador1 = 'jugador 1'
    if not jugador2:
        jugador2 = 'jugador 2'
    return jugador1, jugador2


def elegir_equipo(jugador):
    equipos = traer_equipos()
    while True:
        gamelib.say(f"EQUIPOS: {list(equipos.keys())}")
        nombre_equipo = gamelib.input(f"Ingrese el nombre del equipo a usar por {jugador}")    
        if nombre_equipo in equipos:
            equipo = equipos[nombre_equipo]
            equipo.asignar_jugador(jugador)
            break
        else:
            gamelib.say("debe elegir un equipo válido")

    return equipo


def validar_muertos(equipo):
    pokemones = equipo.devolver_pokemones()
    lista = [not pokemon.esta_vivo() for pokemon in pokemones.values()]
    return all(lista)


def validar_turno(equipo):
    pokemon = equipo.devolver_pokemon_activo()
    jugador = equipo.devolver_jugador()

    if equipo.devolver_accion() == 'r':
        gamelib.say(f"El jugador '{jugador}' se ha retirado")
        return False

    if not validar_muertos(equipo):
        if not pokemon.esta_vivo():
            gamelib.say(f"el pokemon {pokemon.devolver_nombre()} ha muerto, debes seleccionar otro pokemon dentro del equipo")
            elegir_pokemon_activo(equipo)
            
    else:
        gamelib.say(f"has perdido la batalla '{jugador}'")
        return False
    
    return True

def pedir_accion(equipo):
    jugador = equipo.devolver_jugador()
    while True:
        
        accion = gamelib.input(f"Ingrese una acción jugador '{jugador}': 'M' para movimiento / 'C' para cambiar de pokemon / 'R' retirarse")
        if not accion:
            pass
        elif accion.lower() == 'c' or accion.lower() == 'm' or accion.lower() == 'r':
            equipo.asignar_accion(accion.lower())
            return
        
        gamelib.say("Debe ingresar una acción válida")

def manejar_acciones(equipo1, equipo2, pelea):
    atacante, defensor = pelea.elegir_atacante(equipo1, equipo2)
    pokemon_atacante = atacante.devolver_pokemon_activo()
    pokemon_defensor = defensor.devolver_pokemon_activo()

    accion_atacante = atacante.devolver_accion()
    accion_defensor = defensor.devolver_accion()

    if accion_atacante == 'r' or accion_defensor == 'r':
        return

    if accion_atacante == 'c':
        pelea.restaurar_Stats(pokemon_atacante)
        if accion_defensor == 'm':
            elegir_pokemon_activo(atacante)
            mostrar_campo_batalla(equipo1, equipo2)
            elegir_movimiento(pokemon_defensor)
            pokemon_atacante = atacante.devolver_pokemon_activo()
            pelea.manejar_movimiento(pokemon_defensor, pokemon_atacante)
    
        else:
            pelea.restaurar_Stats(pokemon_defensor)
            elegir_pokemon_activo(atacante)
            elegir_pokemon_activo(defensor)
            mostrar_campo_batalla(equipo1, equipo2)
            

    if accion_atacante == 'm':
        if accion_defensor == 'm':
            elegir_movimiento(pokemon_atacante)
            elegir_movimiento(pokemon_defensor)
            pelea.manejar_movimiento(pokemon_atacante, pokemon_defensor)
            pelea.manejar_movimiento(pokemon_defensor, pokemon_atacante)
        
        else:
            pelea.restaurar_Stats(pokemon_defensor)
            elegir_movimiento(pokemon_atacante)
            pelea.manejar_movimiento(pokemon_atacante, pokemon_defensor)
            elegir_pokemon_activo(defensor)
            mostrar_campo_batalla(equipo1, equipo2)

  

def elegir_pokemon_activo(equipo):
    pokemones = equipo.devolver_pokemones()
    jugador = equipo.devolver_jugador()
    
    gamelib.say(f"POKEMONES del jugador '{jugador}': {list(pokemones.keys())}")
    while True:
        nombre_pokemon = gamelib.input(f"Ingrese el nombre del pokemon a utilizar por {jugador}")

        if not nombre_pokemon:
            gamelib.say("debe ingresar el nombre de un pokemón que esté en el equipo")
            continue

        nombre_pokemon = nombre_pokemon.title()
        if nombre_pokemon in pokemones:
            if not pokemones[nombre_pokemon].esta_vivo():
                gamelib.say("No puedes seleccionar a ese pokemon, está muerto")
                continue
            equipo.cambiar_pokemon_activo(pokemones[nombre_pokemon])
            break

        gamelib.say("debe ingresar el nombre de un pokemón que esté en el equipo")


def crear_puntos_movimientos(pokemon):
    detalle_movimientos = traer_detalle_movimientos() 

    for movimiento in pokemon.devolver_movimientos():
        pokemon.asignar_puntos_movimiento(movimiento, detalle_movimientos[movimiento]['pp'])


def validacion_movimiento(movimiento, pokemon):
    if movimiento in pokemon.devolver_movimientos():
        pp_movimiento = pokemon.devolver_puntos_movimiento(movimiento)
        if pp_movimiento > 0:
            pokemon.asignar_movimiento_actual(movimiento)
            pokemon.asignar_puntos_movimiento(movimiento, pp_movimiento-1) 
            return True
        
        else:
            gamelib.say("No puedes utilizar ese movimiento, ya no tiene pp")
        
    else:
        gamelib.say("debe elegir un movimiento válido")

    return False


def elegir_movimiento(pokemon):
    if not pokemon.devolver_puntos_movimientos():
        crear_puntos_movimientos(pokemon)

    while True:
        nombre_pokemon = pokemon.devolver_nombre()
        gamelib.say(f"MOVIMIENTOS {nombre_pokemon}: {list(pokemon.devolver_movimientos())}")
        movimiento = gamelib.input(f"Elige el movimiento para {nombre_pokemon}")
        if validacion_movimiento(movimiento, pokemon):
            break
      

def mostrar_campo_batalla(equipo1, equipo2):
    gamelib.draw_rectangle(50,30,950,670, fill='white')

    gamelib.draw_text(equipo1.jugador, 120, 480, size=18, bold=True, fill='gray')
    path_img = obtener_path_absoluto("imgs/trainer1.gif")
    gamelib.draw_image(path_img, 70, 530)

    gamelib.draw_text(equipo2.jugador, 820, 110, size=18, bold=True, fill='gray')
    path_img = obtener_path_absoluto("imgs/trainer2.gif")
    gamelib.draw_image(path_img, 770, 160)

    mostrar_pokeballs(equipo1, 90, 505)
    mostrar_pokeballs(equipo2, 790, 135)

    mostrar_hp(equipo1.pokemon_activo, 250, 460, POKE_WIDTH)
    gamelib.draw_image(equipo1.pokemon_activo.imagen, 250, 480)
    mostrar_hp(equipo2.pokemon_activo, 550, 120, POKE_WIDTH)
    gamelib.draw_image(equipo2.pokemon_activo.imagen, 550, 140)

def mostrar_hp(poke, x, y, width):
    porcentaje_restante = poke.hp / poke.hp_total
    if porcentaje_restante > 0.7:
        color = "green"
    elif 0.2 < porcentaje_restante <= 0.7:
        color = "yellow"
    else:
        color = "red"
    gamelib.draw_text(f"Hp: {poke.hp}", x, y-15, size=15, bold=True, fill='black')
    gamelib.draw_rectangle(x, y, x + width, y + 10, fill='gray')
    gamelib.draw_rectangle(x, y, x + (width * porcentaje_restante), y + 10, fill=color)

def mostrar_pokeballs(equipo, x_inicial, y):
    for i, poke in enumerate(equipo.pokemones.values()):
        if poke.esta_vivo():
            path_img = obtener_path_absoluto("imgs/pokeball.gif")
            gamelib.draw_image(path_img, x_inicial + i * 20, y)
        if poke.esta_vivo():
            path_img2 = obtener_path_absoluto("imgs/pokeball_gray.gif")
            gamelib.draw_image(path_img2, x_inicial + i * 20, y)
