import sudoku
from mapas import MAPAS
from random import choice

def main():
    juego = sudoku.crear_juego(choice(MAPAS))
    estado_de_juego(juego)
    while True:
        decision = input('  ♦ Ingrese una acción ( A / B / M / S ): ').lower()
        if decision == 'a':
            juego = usuario_agrega_valor(juego)
            if sudoku.esta_terminado(juego):
                juego_terminado(juego)
                if input().lower() in 'si':
                    juego = sudoku.crear_juego(choice(MAPAS))
                    estado_de_juego(juego)
                else:
                    return
            continue
        if decision == 'b':
            usuario_borra_valor(juego)
            continue
        if decision == 'm':
            if sudoku.hay_movimientos_posibles(juego):
                print('         ☺☺☺ ...si, si hay! ☺☺☺')
                print()
            else:
                print('         ▓▓▓ ...no hay movimientos posibles!!! ▓▓▓')
                print('TIP: intentá volver sobre tus pasos ')
                print()
            continue
        if decision == 's':
            return
        if decision == 'n':
            continue
        if not decision:
            print('    ¡Accion invalida!')
            continue
        print('    ¡Acción invalida!')


def usuario_agrega_valor(juego):
    '''
    Segun la fila, columna, y valor, ingresados por el usuario,
    si el movimineto es valido imprime el juego con el nuevo valor, de lo contrario 
    imprime el ultimo juego valido y lo devuelve. Avisa cuando un valor fue agregado o no.
    '''
    fila_ingresada, columna_ingresada = pedir_fila_columna()
    valor_ingresado = input('Ingrese el valor que quiere agregar: ')
    while not valor_ingresado.isdigit() or int(valor_ingresado) > 9 or int(valor_ingresado) < 1:
        print('¡Los valores en el sudoku van del 1 al 9, no del 10 al infinito!')
        valor_ingresado = input('Ingrese el valor que quiere agregar: ')
    valor_ingresado = int(valor_ingresado)

    juego_empezado = sudoku.insertar_valor(juego, fila_ingresada, columna_ingresada, valor_ingresado)
    if juego is juego_empezado:
        estado_de_juego(juego)
        print('           ▓▓▓ ¡Movimiento invalido! ▓▓▓')
        print()
    else:
        estado_de_juego(juego_empezado)
        print('             ☺☺☺ ¡Valor agregado! ☺☺☺')
        print()
        juego = juego_empezado
    return juego


def usuario_borra_valor(juego):
    '''
    Borra el valor que se encuentra en la fila y columna ingresada por el usuario
    '''
    fila_ingresada, columna_ingresada = pedir_fila_columna()
    juego = sudoku.borrar_valor(juego, fila_ingresada, columna_ingresada)
    estado_de_juego(juego)
    print('             ▓▓▓ ¡Valor borrado! ▓▓▓')
    print()


def pedir_fila_columna():
    '''
    Le pide al usuario una fila y una columna del sudoku hasta que sean validos y las devuelve.
    '''
    print('Ingrese fila y columna...')
    fila_ingresada = input('Ingrese fila: ')
    while fila_ingresada.isdigit() or fila_ingresada > 'i': 
        print(' ¿Tu gato salto sobre el teclado?  ' \
        '¡Las FILAS son las LETRAS de los costados!')
        fila_ingresada = input('Ingrese fila: ') 
    for i in range(9):
        str_posibles = 'abcdefghi'
        if fila_ingresada == str_posibles[i]:
            fila_ingresada = i
            break
    columna_ingresada = input('Ingrese columna: ')
    while not columna_ingresada.isdigit() or int(columna_ingresada) > 9 or int(columna_ingresada) < 1:
        print('Vamos a suponer que se te fue el dedo... ' \
        '¡Las COLUMNAS son los NUMEROS que estan sobre y debajo del sudoku!')
        columna_ingresada = input('Ingrese columna: ') 
    columna_ingresada = int(columna_ingresada) - 1
    return fila_ingresada, columna_ingresada


def estado_de_juego(juego):
    '''
    Imprime el sudoku con los cambios hechos por el usuario
    y las posibles acciones a realizar.
    '''
    COORDENADAS_COLUMNA = '               1 2 3   4 5 6   7 8 9'
    PRESENTACION = '''
                     ╔════════╗
             ▄■▀■▄■▀■║ SUDOKU ║■▀■▄■▀■▄
                     ╚════════╝'''
    MARCO_SUPERIOR = '             ╔═══════╦═══════╦═══════╗'
    SEPARADOR = '             ╠═══════╬═══════╬═══════╣ '
    MARCO_INFERIOR = '             ╚═══════╩═══════╩═══════╝' 
    ACCIONES_POSIBLES = '''
┌────────────────────────┬────────────────────────┐
| ♦ A = agregar un valor | ♦ M = ¿Hay movimientos |
| ♦ B = borrar un valor  |       posibles?...     |
| ♦ S = salir            | ♦ N = nada             |
└────────────────────────┴────────────────────────┘'''

    fila_en_string = '' 
    juego_en_string = []
    for i in range(9):
        for j in range(9):
            fila_en_string += str(juego[i][j])
        fila_en_string = fila_en_string.replace('0', '·')
        juego_en_string.append(fila_en_string)
        fila_en_string = ''

    flag = 1
    coordenadas_filas = 'abcdefghi'
    print(PRESENTACION)
    print(COORDENADAS_COLUMNA)
    print(MARCO_SUPERIOR)
    for v1, v2, v3, v4, v5, v6, v7, v8, v9 in juego_en_string:
        letra = coordenadas_filas[flag - 1]
        print(f'          {letra} →║ {v1} {v2} {v3} ║ {v4} {v5} {v6} ║ {v7} {v8} {v9} ║← {letra}' )
        if flag % 3 == 0 and flag < 9:
            flag += 1
            print(SEPARADOR)
        else: flag += 1
    print(MARCO_INFERIOR)
    print(COORDENADAS_COLUMNA)
    print(ACCIONES_POSIBLES)


def juego_terminado(juego):
    '''
    imprime el sudoku terminado
    '''

    PRESENTACION = '''
                     ╔════════╗
             ▄■▀■▄■▀■║ ☺☺☺☺☺☺ ║■▀■▄■▀■▄
                     ╚════════╝'''
    COORDENADAS_COLUMNA = '               ☺ ☺ ☺   ☺ ☺ ☺   ☺ ☺ ☺'
    MARCO_SUPERIOR = '             ╔═══════╦═══════╦═══════╗'
    SEPARADOR = '             ╠═══════╬═══════╬═══════╣ '
    MARCO_INFERIOR = '             ╚═══════╩═══════╩═══════╝'
    CARTEL_FINAL = '''
        ╔══════════════════════════════════╗
▄■▀■▄■▀■║ FELICIDADES, COMPLETO EL SUDOKU! ║■▀■▄■▀■▄
        ╚══════════════════════════════════╝'''

    fila_en_string = '' 
    juego_en_string = []
    for i in range(9):
        for j in range(9):
            fila_en_string += str(juego[i][j])
        juego_en_string.append(fila_en_string)
        fila_en_string = ''

    flag = 1
    print(PRESENTACION)
    print(COORDENADAS_COLUMNA)
    print(MARCO_SUPERIOR)
    for v1, v2, v3, v4, v5, v6, v7, v8, v9 in juego_en_string:
        print(f'           ☺ ║ {v1} {v2} {v3} ║ {v4} {v5} {v6} ║ {v7} {v8} {v9} ║ ☺' )
        if flag % 3 == 0 and flag < 9:
            flag += 1
            print(SEPARADOR)
        else: flag += 1
    print(MARCO_INFERIOR)
    print(COORDENADAS_COLUMNA)
    print(CARTEL_FINAL)
    print('¿Volver a jugar? (si / no): ')

main()