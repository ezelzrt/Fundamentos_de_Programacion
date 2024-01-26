from csv import *
from equipo import *
from pokemon import *
import os.path

def traer_equipos():       
        equipos = {}
        pokemones_id = traer_pokemones_archivo()
        
        path = obtener_path_absoluto('recursos/equipos_guardados.csv')
        with open(path) as entrada:
            datos = reader(entrada, delimiter=';')
            for fila in datos:
                nombre_equipo = fila[0]
                equipo = Equipo(nombre_equipo)
                pokemones = fila[1:]
                for pokemon_datos in pokemones:
                    id_pokemon, movimientos = pokemon_datos.split('-')
                    id_pokemon = int(id_pokemon)
                    nombre_pokemon = pokemones_id[id_pokemon]['nombre']
                    imagen = pokemones_id[id_pokemon]['imagen']
                    tipos = pokemones_id[id_pokemon]['tipos']
                    hp = pokemones_id[id_pokemon]['hp']
                    atk = pokemones_id[id_pokemon]['atk']
                    _def = pokemones_id[id_pokemon]['def']
                    spa = pokemones_id[id_pokemon]['spa']
                    spd = pokemones_id[id_pokemon]['spd']
                    spe = pokemones_id[id_pokemon]['spe']
                    pokemon = Pokemon(id_pokemon, nombre_pokemon, imagen, tipos, hp, atk, _def, spa, spd, spe)
                    pokemon.movimientos = movimientos.split(',')
                    equipo.pokemones[nombre_pokemon] = pokemon
                 
                equipos[nombre_equipo] = equipo
        
        return equipos


def traer_pokemones_archivo():
    '''
    Devuelve:
     Un diccionario que tiene; clave: 'id de pokemon', valor: diccionario de la forma "{ 'estadistica' : 'valor' }"
    '''
    dicc_pokemones_id = {}
    path = obtener_path_absoluto('recursos/pokemons.csv')
    with open(path) as entrada:
        datos = DictReader(entrada, delimiter = ';')

        for fila in datos:
            numero = int(fila['numero'])
            dicc_pokemones_id[numero] = {}
            dicc_pokemones_id[numero]['nombre'] = fila['nombre']
            parth_img = obtener_path_absoluto(fila['imagen'])
            dicc_pokemones_id[numero]['imagen'] = parth_img
            dicc_pokemones_id[numero]['tipos'] = fila['tipos']
            dicc_pokemones_id[numero]['hp'] = int(fila['hp'])
            dicc_pokemones_id[numero]['atk'] = int(fila['atk'])
            dicc_pokemones_id[numero]['def'] = int(fila['def'])
            dicc_pokemones_id[numero]['spa'] = int(fila['spa'])
            dicc_pokemones_id[numero]['spd'] = int(fila['spd'])
            dicc_pokemones_id[numero]['spe'] = int(fila['spe'])

    return dicc_pokemones_id
    

def traer_modificadores():

    modificadores = {}
    path = obtener_path_absoluto('recursos/tabla_tipos.csv')
    with open(path) as entrada:
        datos = DictReader(entrada, delimiter = ';')

        for fila in datos:
            modificadores[fila['Types']] = {}
            modificadores[fila['Types']]['Bug'] = float((fila['Bug']))
            modificadores[fila['Types']]['Dark'] = float((fila['Dark']))
            modificadores[fila['Types']]['Dragon'] = float(fila['Dragon'])
            modificadores[fila['Types']]['Electric'] = float(fila['Electric'])
            modificadores[fila['Types']]['Fairy'] = float(fila['Fairy'])
            modificadores[fila['Types']]['Fighting'] = float(fila['Fighting'])
            modificadores[fila['Types']]['Fire'] = float(fila['Fire'])
            modificadores[fila['Types']]['Flying'] = float(fila['Flying'])
            modificadores[fila['Types']]['Ghost'] = float(fila['Ghost'])
            modificadores[fila['Types']]['Grass'] = float(fila['Grass'])
            modificadores[fila['Types']]['Ground'] = float(fila['Ground'])
            modificadores[fila['Types']]['Ice'] = float(fila['Ice'])
            modificadores[fila['Types']]['Normal'] = float(fila['Normal'])
            modificadores[fila['Types']]['Poison'] = float(fila['Poison'])
            modificadores[fila['Types']]['Psychic'] = float(fila['Psychic'])             
            modificadores[fila['Types']]['Rock'] = float(fila['Rock'])
            modificadores[fila['Types']]['Steel'] = float(fila['Steel'])
            modificadores[fila['Types']]['Water'] = float(fila['Water'])

    
    return modificadores


def traer_detalle_movimientos():
    
    detalle_movimientos = {}
    path = obtener_path_absoluto('recursos/detalle_movimientos.csv')
    with open(path) as entrada:
        datos = DictReader(entrada, delimiter = ',')

        for fila in datos:
            detalle_movimientos[fila['nombre']] = {}
            detalle_movimientos[fila['nombre']]['categoria'] = fila['categoria']
            detalle_movimientos[fila['nombre']]['objetivo'] = fila['objetivo']
            detalle_movimientos[fila['nombre']]['pp'] = int(fila['pp'])
            detalle_movimientos[fila['nombre']]['poder'] = int(fila['poder'])
            detalle_movimientos[fila['nombre']]['tipo'] = fila['tipo']
            if 'def' in fila['stats']:
                fila['stats'] = fila['stats'].replace('def', '_def')
            detalle_movimientos[fila['nombre']]['stats'] = fila['stats'].split(';')   
            
    return detalle_movimientos


def obtener_path_absoluto(archivo):
    '''
    Obtiene el path absoluto del archivo pasado por parametro
    '''
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(BASE_DIR, archivo)

    return path
