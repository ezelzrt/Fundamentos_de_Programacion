class Equipo:

    def __init__(self,nombre):
        self.nombre = nombre
        self.pokemones = {} 
        self.jugador = None
        self.pokemon_activo = None
        self.accion_actual = None

    def agregar_pokemon(self, pokemon):
        if len(self.pokemones) == 6:
            return
        if pokemon.movimientos:
            self.pokemones.append(pokemon)

    def borrar_pokemon(self, indice):
        self.pokemones.pop(indice-1) 

    def cambiar_pokemon_activo(self, pokemon):
        self.pokemon_activo = pokemon
    
    def devolver_pokemon_activo(self):
        return self.pokemon_activo
    
    def devolver_pokemones(self):
        return self.pokemones
    
    def asignar_jugador(self, jugador):
        self.jugador = jugador

    def devolver_jugador(self):
        return self.jugador

    def asignar_accion(self, accion):
        self.accion_actual = accion

    def devolver_accion(self):
        return self.accion_actual