from archivos import *
from logica_gamelib import *

class PokedexPokemones:
    
    def __init__(self):
        self.pokemon_actual = 1
        self.pokemones_id, self.pokemones_nombre = traer_pokemones_archivo()

    def avanzar(self):
        if self.pokemon_actual == len(self.pokemones_id):
                self.pokemon_actual = 1
        else:
            self.pokemon_actual += 1
    
    def retroceder(self):
        if self.pokemon_actual == 1:
                self.pokemon_actual = len(self.pokemones_id) 
        else:
            self.pokemon_actual -= 1
        
    def buscar(self, pokemon):
        if not pokemon:
            return
        
        if pokemon.isdigit():
            id_pokemon = int(pokemon)
            if id_pokemon in self.pokemones_id:
                self.pokemon_actual = id_pokemon
            
            else:
                gamelib.say("el pokemon solicitado no existe")
            
        elif pokemon.title() in self.pokemones_nombre:
            busqueda_pokemon = pokemon.title()
            id_pokemon = self.pokemones_nombre[busqueda_pokemon]
            self.pokemon_actual = id_pokemon
        
        else:
            gamelib.say("el pokemon solicitado no existe")
