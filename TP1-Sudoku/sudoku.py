VACIO = 0

ALTO_TABLERO = 9
ANCHO_TABLERO = 9

ALTO_CUADRANTE = 3
ANCHO_CUADRANTE = 3

def crear_juego(representacion):
    '''
    Dada una representación en cadena de un juego de Sudoku,
    devuelve un juego de Sudoku.

    El juego de Sudoku se representa como una matriz de 9x9
    donde cada elemento es un número entero o la constante
    VACIO para indicar que no se escribió ningún número en 
    esa posición.

    La representación es una cadena con el siguiente formato:

    003020600
    900305001
    001806400
    008102900
    700000008
    006708200
    002609500
    800203009
    005010300

    Donde un 0 significa que la casilla está vacía.
    '''
    fila_sudoku = []
    sudoku = []
    for valor in representacion:
        if valor.isdigit():
            fila_sudoku.append(int(valor))
        else:
            sudoku.append(fila_sudoku)
            fila_sudoku = []
    sudoku.append(fila_sudoku)
    return sudoku   

def hay_valor_en_fila(sudoku, fila, valor):
    '''
    Devuelve True si ya hay un casillero con el valor
    'valor' en la fila 'fila'.

    Por ejemplo para fila = 3 deberán revisar todas las
    siguientes celdas:
    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)
    '''
    for i in range(ANCHO_TABLERO):
        if obtener_valor(sudoku, fila, i) == valor:
            return True
    return False 

def hay_valor_en_columna(sudoku, columna, valor):
    '''
    Devuelve True si ya hay un casillero con el valor 'valor'
    en la columna 'columna'.

    Por ejemplo para columna = 3 deberán revisar todas las
    siguientes celdas:
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)
    '''
    for i in range(ALTO_TABLERO):
        if obtener_valor(sudoku, i, columna) == valor:
            return True
    return False   


def obtener_origen_region(fila, columna):
    '''
    Devuelve la posición de la celda de la esquina superior izquierda
    de la región en que se encuentra la celda en (fila, columna).

    Las regiones se agrupan de la siguiente forma:
   *[0,0] [0,1] [0,2] *[0,3] [0,4] [0,5] *[0,6] [0,7] [0,8]
    [1,0] [1,1] [1,2]  [1,3] [1,4] [1,5]  [1,6] [1,7] [1,8]
    [2,0] [2,1] [2,2]  [2,3] [2,4] [2,5]  [2,6] [2,7] [2,8]

   *[3,0] [3,1] [3,2] *[3,3] [3,4] [3,5] *[3,6] [3,7] [3,8]
    [4,0] [4,1] [4,2]  [4,3] [4,4] [4,5]  [4,6] [4,7] [4,8]
    [5,0] [5,1] [5,2]  [5,3] [5,4] [5,5]  [5,6] [5,7] [5,8]

   *[6,0] [6,1] [6,2] *[6,3] [6,4] [6,5] *[6,6] [6,7] [6,8]
    [7,0] [7,1] [7,2]  [7,3] [7,4] [7,5]  [7,6] [7,7] [7,8]
    [8,0] [8,1] [8,2]  [8,3] [8,4] [8,5]  [8,6] [8,7] [8,8]

    Las celdas marcadas con un (*) son las celdas que deberá 
    devolver esta función para la correspondiente región.

    Por ejemplo, para la posición (fila = 1, columna = 4) la función
    deberá devolver (0, 3).
    '''
    if fila < ALTO_CUADRANTE:
        if columna < ANCHO_CUADRANTE:
            return (0, 0)
        if columna < ANCHO_TABLERO - ANCHO_CUADRANTE:
            return (0, ANCHO_CUADRANTE)
        return (0, ANCHO_TABLERO - ANCHO_CUADRANTE)

    if fila < ALTO_TABLERO - ALTO_CUADRANTE:
        if columna < ANCHO_CUADRANTE:
            return (ALTO_CUADRANTE, 0)
        if columna < ANCHO_TABLERO - ANCHO_CUADRANTE:
            return (ALTO_CUADRANTE, ANCHO_CUADRANTE)
        return (ALTO_CUADRANTE, ANCHO_TABLERO - ANCHO_CUADRANTE)

    if columna < ANCHO_CUADRANTE: 
        return (ALTO_TABLERO - ALTO_CUADRANTE, 0)
    if columna < ANCHO_TABLERO - ANCHO_CUADRANTE:
        return (ALTO_TABLERO - ALTO_CUADRANTE, ANCHO_CUADRANTE)
    return (ALTO_TABLERO - ALTO_CUADRANTE, ANCHO_TABLERO - ANCHO_CUADRANTE)

def hay_valor_en_region(sudoku, fila, columna, valor):
    '''
    Devuelve True si hay hay algún casillero con el valor `valor`
    en la región de 3x3 a la que corresponde la posición (fila, columna).

    Ver como se agrupan las regiones en la documentación de la función
    obtener_origen_region.
    
    Por ejemplo, para la posición (fila = 0, columna = 1) deberán revisar 
    si está `valor` en todas las siguientes celdas:
    (0, 0), (0, 1) (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2).
    '''
    fila, columna = obtener_origen_region(fila, columna)
    for i in range(fila, fila + ALTO_CUADRANTE):
        for j in range(columna, columna + ANCHO_CUADRANTE):
            if obtener_valor(sudoku, i, j) == valor: 
                return True
    return False

def es_movimiento_valido(sudoku, fila, columna, valor):
    '''
    Devuelve True si se puede poner 'valor' en la posición
    (fila, columna) y el Sudoku sigue siendo válido; o False
    en caso contrario.

    'valor' se puede ubicar en la posición (fila, columna) si
    se cumple lo siguiente:
     - Ningún otro elemento que esté en la misma fila es igual a 'valor'
     - Ningún otro elemento que esté en la misma columna es igual a 'valor'
     - Ningún otro elemento que esté en la misma región es igual a 'valor'
    
    No modifica el Sudoku recibido.
    '''
    if hay_valor_en_fila(sudoku, fila, valor): return False
    if hay_valor_en_columna(sudoku, columna, valor): return False
    if hay_valor_en_region(sudoku, fila, columna, valor): return False
    return True

def insertar_valor(sudoku, fila, columna, valor):
    '''
    Intenta insertar el valor de la celda en la posición 
    (fila, columna). 
    
    Si el movimiento es válido se devolverá un nuevo Sudoku
    con el valor cambiado. En caso contrario se devolverá el
    mismo Sudoku que se recibió por parámetro.
    '''
    if es_movimiento_valido(sudoku, fila, columna, valor):
        sudoku_copiado = copiar_sudoku(sudoku)
        sudoku_copiado[fila][columna] = valor
        return sudoku_copiado
    return sudoku

def borrar_valor(sudoku, fila, columna):
    '''
    Borra el valor de la celda que está en la posición
    (fila, columna).

    No modifica el Sudoku recibido por parámetro, devuelve uno
    nuevo con la modificación realizada.
    '''
    sudoku_copiado = copiar_sudoku(sudoku)
    sudoku_copiado[fila][columna] = VACIO
    return sudoku_copiado

def copiar_sudoku(sudoku):
    '''
    Devulve una copia del sudoku recibido
    '''
    sudoku_copiado = []
    for fila in range(ALTO_TABLERO):
        sudoku_copiado.append(sudoku[fila].copy())
    return sudoku_copiado

def esta_terminado(sudoku):
    '''
    Devuelve True si el Sudoku está completado 
    correctamente.

    Un Sudoku está completado correctamente cuando todas 
    sus celdas tienen números y todos los números son válidos
    (es decir, no hay repetidos en la columna, ni en la fila
    ni en la región).
    '''
    # for i in range(ANCHO_TABLERO):
    #     for j in range(ALTO_TABLERO):
    #         x = obtener_valor(sudoku, i, j)
    #         sudoku = borrar_valor(sudoku, i, j)
    #         if not es_movimiento_valido(sudoku, i, j, x):
    #             return False
    #         insertar_valor(sudoku, i, j, x)
    # return True
 
    for i in range(ANCHO_TABLERO):
        for j in range(ALTO_TABLERO):
            if obtener_valor(sudoku, i, j) == VACIO:
                return False
    return True

def obtener_valor(sudoku, fila, columna):
    '''
    Devuelve el número que se encuentra en la celda (fila, columna)
    o la constante VACIO si no hay ningún número en dicha celda.
    '''
    return sudoku[fila][columna]

def hay_movimientos_posibles(sudoku):
    '''
    Devuelve True si hay al menos un movimiento posible
    en el estado actual del juego.

    Que exista un movimiento posible no implica que el juego
    pueda completarse correctamente, sólamente indica que hay
    al menos una posible inserción.
    '''
    for i in range(ANCHO_TABLERO):
        for j in range(ALTO_TABLERO):
            for x in range(1, ANCHO_TABLERO+1):
                if es_movimiento_valido(sudoku, i, j, x): return True
    return False