from pokedex_equipos import *
from pokedex_pokemones import *
from logica_gamelib import *


class Pokedex:
    def __init__(self):
        self.equipos = PokedexEquipos()
        self.pokemones = PokedexPokemones()
        self.actual = 1
    
    def devolver_actual(self):
        return self.actual

    def siguiente(self):
        if self.actual is 1:
            self.pokemones.avanzar()
        else:
            self.equipos.avanzar()

    def anterior(self):
        if self.actual is 1:
            self.pokemones.retroceder()
        else:
            self.equipos.retroceder()

    def cambiar_actual(self):
        if self.actual is 1:
            self.actual += 1 
        else:
            self.actual -= 1

    def borrar_o_buscar(self):
        if self.actual is 1:
            pokemon = gamelib.input("Ingrese un pokemon por numero o nombre") 
            self.pokemones.buscar(pokemon)
        else:
            index_pokemon = gamelib.input(f"Ingrese la posicion del pokemon en el equipo")
            self.equipos.borrar_pokemon(index_pokemon)
    
    def agregar(self):
        if self.actual is 2:
            equipos = self.devolver_equipos()
            equipo_actual = self.equipos.devolver_equipo_actual()
            gamelib.title(f'{equipos[equipo_actual].nombre}')
            pokemon = gamelib.input("Ingrese un pokemon por numero o nombre") 
            self.equipos.agregar_pokemon(pokemon)

    def crear(self):
        if self.actual is 2:
            nombre = gamelib.input("Indique el nombre del equipo: ")
            self.equipos.agregar(nombre)


    def dibujar(self):
        if self.actual == 1:
            dibujar_pokemon(self.pokemones.pokemones_id, self.pokemones.pokemon_actual)
        else:
            if not self.equipos.equipos:
                gamelib.draw_text('Hay que agregar equipos', 600, 120,None, 20, True, 'white')
            else:
                dibujar_pokemon_movimientos(self.equipos.equipos[self.equipos.equipo_actual])
        
    def devolver_equipos(self):
        return self.equipos.devolver()

        