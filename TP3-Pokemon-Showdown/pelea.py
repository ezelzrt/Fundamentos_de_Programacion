from archivos import *
import random
import gamelib

class Pelea:

    def __init__(self, pokemon_1, pokemon_2):
        self.pokemon_activo_1 = pokemon_1
        self.pokemon_activo_2 = pokemon_2
        self.detalle_movimientos = traer_detalle_movimientos()
        self.modificadores = traer_modificadores()
        self.pokemones = traer_pokemones_archivo()
    

    def elegir_atacante(self,equipo1, equipo2):
        
        if equipo1.pokemon_activo.spe > equipo2.pokemon_activo.spe:
            return equipo1, equipo2
        
        return equipo2, equipo1
        

    def daño_movimiento(self, movimiento, atacante, defensor):
        poder = self.detalle_movimientos[movimiento]["poder"]
    
        if self.detalle_movimientos[movimiento]["categoria"] == 'Special':
            ataque = atacante.spa
            defensa = defensor.spd
        else:
            ataque = atacante.atk
            defensa = defensor._def

        daño_base = 15 * poder * (ataque/ defensa) / 50


        if self.detalle_movimientos[movimiento]["tipo"] in atacante.tipos:
            daño_base *= 1.5

        if len(defensor.tipos) > 1:
            multiplicador =  self.modificadores[defensor.tipos[0]][self.detalle_movimientos[movimiento]['tipo']]
            daño_base *= multiplicador
            return int(daño_base * round(random.uniform(0.8, 1),2))

        multiplicador =  self.modificadores[defensor.tipos[0]][self.detalle_movimientos[movimiento]['tipo']]            
        daño_base *= multiplicador
        return int(daño_base * round(random.uniform(0.8, 1),2))



    def manejar_movimiento(self, atacante, defensor):
        if self.detalle_movimientos[atacante.movimiento_actual]["categoria"] == 'Status':

            if self.detalle_movimientos[atacante.movimiento_actual]['objetivo'] == 'normal':
                self.alterar_Stats_Defensor(atacante, defensor)
            
            else:
                self.alterar_Stats_Propios(atacante)

        else:
            if self.detalle_movimientos[atacante.movimiento_actual]["categoria"] == 'Special' or 'Physical':
                self.atacar(atacante, defensor)
        

    def atacar(self, atacante, defensor):

        daño_atacante = self.daño_movimiento(atacante.movimiento_actual, atacante, defensor)
        
        if defensor.hp - daño_atacante <= 0:
            self.restaurar_Stats(defensor)
            defensor.hp = 0
            return
        
        defensor.hp -= daño_atacante


    def alterar_Stats_Propios(self, atacante):
        
        if not self.detalle_movimientos[atacante.movimiento_actual]['stats'][0]: 
            
            if atacante.hp + atacante.hp_total / 2 > atacante.hp_total:
                atacante.hp = atacante.hp_total
            
            else:
                atacante.hp += atacante.hp_total / 2
               
        else:
            for stat in self.detalle_movimientos[atacante.movimiento_actual]['stats']:
                valor = getattr(atacante, stat)
                setattr(atacante, stat, valor * 2)
                valor = getattr(atacante, stat)


    def alterar_Stats_Defensor(self, atacante, defensor):
        if not self.detalle_movimientos[atacante.movimiento_actual]['stats'][0]:
            return

        for stat in self.detalle_movimientos[atacante.movimiento_actual]['stats']:
                valor = getattr(defensor, stat)
                setattr(defensor, stat, valor * 2)
                valor = getattr(defensor, stat)


    def restaurar_Stats(self, pokemon):
        pokemon.atk = self.pokemones[pokemon.numero]['atk']
        pokemon._def = self.pokemones[pokemon.numero]['def']
        pokemon.spe = self.pokemones[pokemon.numero]['spe']
