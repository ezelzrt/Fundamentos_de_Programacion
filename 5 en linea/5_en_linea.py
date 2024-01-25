import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 300
ALTO_VENTANA_DEL_JUEGO = 250
ANCHO_CASILLA = ANCHO_VENTANA/10
ALTO_CASILLA = ALTO_VENTANA_DEL_JUEGO/10

def juego_crear():
    """Inicializar el estado del juego"""
    juego = {}
    return juego

def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    if y > ALTO_VENTANA_DEL_JUEGO-1: return juego
    x = x - x % ANCHO_CASILLA + ANCHO_CASILLA//2
    y = y - y % ALTO_CASILLA + ALTO_CASILLA//2

    flag = len(juego)
    if juego.get((x,y) ,' ') in 'XO': return juego
    elif flag % 2 == 0: juego[x,y] = 'O'
    else: juego[x,y] = 'X'
    return juego

def juego_mostrar(juego):
    """Actualizar la ventana"""
    gamelib.draw_rectangle(0, 0, ANCHO_VENTANA, ALTO_VENTANA)
    gamelib.draw_text('CINCO EN LINEA', ANCHO_VENTANA/2, ALTO_VENTANA-5, fill='black', size=6, bold=True)

    flag = len(juego)
    if flag % 2 == 0: 
        gamelib.draw_text('► Turno de O', 75, ALTO_VENTANA-30, fill='black', bold=True)
    else:
        gamelib.draw_text('► Turno de X', 225, ALTO_VENTANA-30, fill='black', bold=True)
    for i in range(11):
        gamelib.draw_line(i*ANCHO_CASILLA, 0, i*ANCHO_CASILLA, ALTO_VENTANA_DEL_JUEGO, fill='black')
        gamelib.draw_line(0, i*ALTO_CASILLA, ANCHO_VENTANA, i*ALTO_CASILLA, fill='black')
    for x, y in juego:
        gamelib.draw_text(juego[x,y], x, y, fill='black', bold=True)

def main():
    juego = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego = juego_actualizar(juego, x, y)

gamelib.init(main)