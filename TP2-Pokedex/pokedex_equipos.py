from archivos import *

class PokedexEquipos:

    def __init__(self):
        self.equipo_actual = 0
        self.equipos = []
        self.pokemones_id, self.pokemones_nombre = traer_pokemones_archivo()
        self.movimientos = traer_movimientos()
    
    def agregar_pokemon(self, id_pokemon):
        if len(self.equipos[self.equipo_actual].pokemones) == 6:
               gamelib.say("No se pueden agregar mas pokemones")
               return
        
        gamelib.title(f'{self.equipos[self.equipo_actual].nombre}')

        if not id_pokemon:
            return

        if not id_pokemon.isdigit():
            id_pokemon = id_pokemon.title()
            if not id_pokemon in self.pokemones_nombre:
                gamelib.say('No existe el pokemon solicitado')
                return

            id_pokemon = self.pokemones_nombre[id_pokemon]

        id_pokemon = int(id_pokemon)

        if id_pokemon in self.pokemones_id:
            nombre = self.pokemones_id[id_pokemon]['nombre'] 
            pokemon = Pokemon(id_pokemon, nombre)
            self.agregar_movimientos(nombre, pokemon)
            if pokemon.movimientos:
                self.equipos[self.equipo_actual].agregar_pokemon(pokemon)
            else:
                gamelib.say('Debe tener por lo menos un movimiento')
                    
    def agregar_movimientos(self, nombre, pokemon):
        for movimiento in self.movimientos[nombre]:
            agregar_movimiento = gamelib.input(f"¿Desea agregar el movimiento {movimiento}? s/n")
            if agregar_movimiento == 's':
                pokemon.movimientos.append(movimiento)

            if len(pokemon.movimientos) == 4:
                return

    def borrar_pokemon(self, index_pokemon):
        if len(self.equipos[self.equipo_actual].pokemones) == 0:
            gamelib.say("no hay pokemones disponibles para borrar")
        else:
            if not index_pokemon or not index_pokemon.isdigit():
                gamelib.say("no ingresó un valor valido")
                return 
    
            index_pokemon = int(index_pokemon)
            
            if not index_pokemon or len(self.equipos[self.equipo_actual].pokemones) < index_pokemon:
                gamelib.say("el indice ingresado no existe")
                return 

            self.equipos[self.equipo_actual].borrar_pokemon(index_pokemon)
            
    def avanzar(self):
        if self.equipo_actual == len(self.equipos) - 1:
            self.equipo_actual = 0
        else:
            self.equipo_actual += 1
        
    def retroceder(self):
        if self.equipo_actual == 0:
            self.equipo_actual = len(self.equipos) - 1
        else:
            self.equipo_actual -= 1

    def agregar(self, nombre): 
        equipo_nuevo = Equipo(nombre)
        self.equipos.append(equipo_nuevo)

    def devolver(self):
        return self.equipos

    def devolver_equipo_actual(self):
        return self.equipo_actual
    