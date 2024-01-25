import gamelib 

def dibujar_pokemon(pokemones, numero):
    gamelib.draw_text(pokemones[numero]['nombre'],600, 120,None,20,True,False, fill='white')
    gamelib.draw_image(pokemones[numero]['imagen'], 130, 200)
    gamelib.draw_text("Hp:", 745, 250,None,12,True,False, fill='black')
    gamelib.draw_text(f"{pokemones[numero]['hp']}", 780, 250, fill='black')
    gamelib.draw_text(f"Ataque:", 765, 300,None,12,True,False, fill='black')
    gamelib.draw_text(f"{pokemones[numero]['atk']}", 818, 300, fill='black')
    gamelib.draw_text(f"Defensa:", 770, 350,None, 12,True,False, fill='black')
    gamelib.draw_text(f"{pokemones[numero]['def']}", 828, 350, fill='black')
    gamelib.draw_text(f"Ataque Especial:", 805, 400,None,12,True,False, fill='black')
    gamelib.draw_text(f"{pokemones[numero]['spa']}", 900, 400, fill='black')
    gamelib.draw_text(f"Defensa Especial:", 810, 450,None, 12, True, False, fill='black')
    gamelib.draw_text(f"{pokemones[numero]['spd']}", 905, 450, fill='black')
    gamelib.draw_text(f"Velocidad:", 775, 500,None, 12, True, False, fill='black')
    gamelib.draw_text(f"{pokemones[numero]['spe']}", 836, 500, fill='black')

def mostrar_pokedex(estado):
    gamelib.draw_rectangle(0,30,1200,700, fill='red')
    gamelib.draw_oval(80, 70, 130, 120, outline='black', fill='#15E8E8')
    gamelib.draw_oval(150, 70, 170, 90, outline='black', fill='red')
    gamelib.draw_oval(180, 70, 200, 90, outline='black', fill='green')
    gamelib.draw_oval(210, 70, 230, 90, outline='black', fill='yellow')
    gamelib.draw_rectangle(60,150,1140,610, fill='grey')
    gamelib.draw_rectangle(70,160,1130,600, fill='white')
    gamelib.draw_oval(80, 620, 120, 660, fill='blue')
    gamelib.draw_oval(1000, 65, 1030, 95, fill='black', outline='black')
    gamelib.draw_rectangle(1015, 65, 1110, 95, fill='black', outline='black')
    gamelib.draw_oval(1095, 65, 1125, 95, fill='black', outline='black')
    gamelib.draw_text('V = vista', 1060, 80, None, 14, True, False, fill='white')
    gamelib.draw_text('◄', 30, 390, size=50)
    gamelib.draw_text('►', 1170, 390, size=50)
    
    if estado == 1:
        gamelib.draw_oval(150, 620, 180, 650, fill='green', outline='green')
        gamelib.draw_rectangle(165, 620, 280, 650, fill='green', outline='green')
        gamelib.draw_oval(265, 620, 295, 650, fill='green', outline='green')
        gamelib.draw_text('B = buscar', 220, 636,None, 14, True, False, fill='white')
    else:
        gamelib.draw_oval(150, 620, 180, 650, fill='green', outline='green')
        gamelib.draw_rectangle(165, 620, 358, 650, fill='green', outline='green')
        gamelib.draw_oval(343, 620, 373, 650, fill='green', outline='green')
        gamelib.draw_oval(390, 620, 420, 650, fill='orange', outline='orange')
        gamelib.draw_rectangle(405, 620, 625, 650, fill='orange', outline='orange')
        gamelib.draw_oval(610, 620, 640, 650, fill='orange', outline='orange')
        gamelib.draw_oval(660, 620, 690, 650, fill='blue', outline='blue')
        gamelib.draw_rectangle(675, 620, 875, 650, fill='blue', outline='blue')
        gamelib.draw_oval(860, 620, 890, 650, fill='blue', outline='blue')
        gamelib.draw_text('C = crear equipo', 260, 636,None, 14, True, False, fill='white')
        gamelib.draw_text('A = agregar pokemon', 515, 636,None, 14, True, False, fill='white')
        gamelib.draw_text('B = borrar pokemon', 773, 636,None, 14, True, False, fill='white')


def dibujar_pokemon_movimientos(equipo):
    altura = 260
    gamelib.draw_text(f'{equipo.nombre}', 600, 120, None, 20, True, fill = 'white')
    gamelib.draw_text('POKEMONES', 300, 200, None, 18, False, fill = 'black')
    gamelib.draw_text('MOVIMIENTOS', 750, 200, None, 18, False, fill = 'black')
    if equipo.pokemones:
        for pokemon in equipo.pokemones:
            gamelib.draw_text(f'{equipo.pokemones.index(pokemon) + 1 }: ', 150, altura, None, 14, True, fill='black')
            gamelib.draw_text(f'{pokemon.nombre}', 300, altura, None, 14, True, fill ='black')
            movimientos_mostrar = ', '.join(pokemon.movimientos)
            gamelib.draw_text(f'{movimientos_mostrar}', 750, altura, None, 14, True, fill = 'black')
            altura += 60