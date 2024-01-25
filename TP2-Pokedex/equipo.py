import archivos 
from logica_gamelib import *

class Equipo:

    def __init__(self,nombre):
        self.nombre = nombre
        self.pokemones = []
       

    def agregar_pokemon(self, pokemon):
        if len(self.pokemones) == 6:
            return
        if pokemon.movimientos:
            self.pokemones.append(pokemon)
    

    def borrar_pokemon(self, indice):
        self.pokemones.pop(indice-1) 
