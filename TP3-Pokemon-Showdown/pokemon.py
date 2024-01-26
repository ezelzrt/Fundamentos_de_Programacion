class Pokemon:

    def __init__(self, numero, nombre, imagen, tipos, hp, atk, _def, spa, spd, spe):
        self.numero = numero   
        self.nombre = nombre
        self.imagen = imagen
        self.tipos = tipos.split(',')
        self.hp_total = hp + 110
        self.hp = self.hp_total
        self.atk = atk
        self._def =_def
        self.spa = spa
        self.spd = spd
        self.spe = spe
        self.movimientos = []
        self.movimiento_actual = None
        self.puntos_movimientos = {}

    def devolver_nombre(self):
        return self.nombre

    def esta_vivo(self):
        
        return self.hp > 0

    def asignar_movimiento_actual(self, movimiento):
        self.movimiento_actual = movimiento

    def devolver_movimientos(self):
        return self.movimientos

    def asignar_puntos_movimiento(self, movimiento, pp):
        self.puntos_movimientos[movimiento] = pp

    def devolver_puntos_movimiento(self, movimiento):
        return self.puntos_movimientos[movimiento]

    def devolver_puntos_movimientos(self):
        return self.puntos_movimientos
