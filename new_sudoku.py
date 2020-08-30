"""
    SUDOKU - nuevo intento, versión definitiva, usando set() y 
    estrategias de anotar a lápiz - anotar todos los número menos los que ya están -
    y buscar huérfanos - buscar número anotados a lápiz que sean únicos en
    esa fila/columna/cuadrado.
"""
import time

start_time = time.time()
FILAS = 9
LADO = 3
TODOS = '123456789ABCDEFG'
VALIDOS = set(TODOS[:FILAS])
SENTIDOS = ['por_filas', 'por_columnas']

muy_facil = [
    ' 4  5  3 ',
    '38 4   25',
    ' 2     6 ',
    '29    6 4',
    ' 6     7 ',
    ' 7 62 859',
    ' 5 97   3',
    '  9  3 8 ',
    '4 628    '
    ]

facil = [' 257348 6',
    '3  8 2 54',
    '7 46  3  ',
    '437    82',
    ' 913 7 65',
    ' 582   37',
    '     9  1',
    '  246 593',
    '5 9  367 '
    ]

normal = [
    '  4      ',
    '  8 2 9  ',
    '   9  564',
    '   78    ',
    ' 4  62 5 ',
    '87 3 524 ',
    ' 5   7   ',
    '4612  7 5',
    '7 36     '
    ]

dificil = [
    '   8    5',
    '    75269',
    ' 49  3  8',
    '  7  43 1',
    '       2 ',
    '3      9 ',
    '  4 6  8 ',
    ' 6 248 1 ',
    '8  3 9 4 '
    ]

muy_dificil = [
    '  5   9  ',
    '     645 ',
    '  854   3',
    '7       8',
    '   32  4 ',
    '   8  2  ',
    ' 5     72',
    '  6738   ',
    '  4   6  '
    ]

extremo = [
    ' 9   54  ',
    '       1 ',
    '  41   6 ',
    '   3 46  ',
    '  6 12   ',
    ' 48     5',
    '  5  3   ',
    '8   7    ',
    '      287'
    ]

problema = {
    '00': {'4'}, '01': {'1', '2'}, '02': {'5'}, '03': {'1', '2'}, '04': {'7'}, '05': {'3'}, '06': {'9'}, '07': {'8'}, '08': {'6'}, 
    '10': {'9', '2'}, '11': {'3'}, '12': {'7'}, '13': {'9', '2'}, '14': {'8'}, '15': {'6'}, '16': {'4'}, '17': {'5'}, '18': {'1'}, 
    '20': {'9', '1', '6'}, '21': {'9', '1', '6'}, '22': {'8'}, '23': {'5'}, '24': {'4'}, '25': {'9', '1'}, '26': {'7'}, '27': {'2'}, '28': {'3'}, 
    '30': {'7'}, '31': {'3', '9', '1', '6', '4'}, '32': {'2'}, '33': {'9', '4', '6'}, '34': {'9', '5', '1', '6'}, '35': {'9', '5', '1', '4'}, '36': {'3'}, '37': {'3', '9', '1', '6'}, '38': {'8'}, 
    '40': {'6'}, '41': {'8'}, '42': {'9', '1'}, '43': {'3'}, '44': {'2'}, '45': {'9', '5', '1', '7'}, '46': {'1'}, '47': {'4'}, '48': {'9', '5', '7'}, 
    '50': {'5'}, '51': {'3', '9', '1', '6', '4'}, '52': {'3'}, '53': {'8'}, '54': {'9', '5', '1', '7', '6'}, '55': {'9', '5', '1', '7', '4'}, '56': {'2'}, '57': {'3', '9', '1', '6'}, '58': {'9', '5', '7'}, 
    '60': {'3'}, '61': {'5'}, '62': {'9', '1'}, '63': {'9', '1', '6', '4'}, '64': {'9', '1', '6'}, '65': {'9', '1', '4'}, '66': {'8'}, '67': {'7'}, '68': {'2'}, 
    '70': {'9', '1', '2'}, '71': {'9', '1', '2'}, '72': {'6'}, '73': {'7'}, '74': {'3'}, '75': {'8'}, '76': {'5'}, '77': {'9', '1'}, '78': {'4'}, 
    '80': {'8'}, '81': {'7'}, '82': {'4'}, '83': {'9', '1', '2'}, '84': {'9', '5', '1'}, '85': {'2'}, '86': {'6'}, '87': {'3'}, '88': {'9', '5'}}

problema_extremo = {'00': {'3', '1'}, '01': {'9'}, '02': {'7', '2', '3', '1'}, '03': {'6', '7', '2'}, '04': {'6', '3'}, '05': {'5'}, '06': {'4'}, '07': {'2', '3'}, '08': {'8'}, 
    '10': {'6'}, '11': {'7', '5', '8', '2', '3'}, '12': {'7', '2', '3'}, '13': {'9', '7', '2'}, '14': {'4'}, '15': {'9', '7', '8'}, '16': {'7', '5'}, '17': {'1'}, '18': {'9', '2', '3'}, 
    '20': {'5', '2', '3'}, '21': {'7', '5', '8', '2', '3'}, '22': {'4'}, '23': {'1'}, '24': {'9', '3'}, '25': {'9', '7', '8'}, '26': {'7', '5'}, '27': {'6'}, '28': {'9', '2', '3'}, 
    '30': {'9', '5', '2', '1'}, '31': {'7', '5', '2', '1'}, '32': {'7', '2', '1'}, '33': {'3'}, '34': {'8'}, '35': {'4'}, '36': {'6'}, '37': {'9', '7'}, '38': {'2', '1'}, 
    '40': {'9', '3'}, '41': {'7', '3'}, '42': {'6'}, '43': {'5'}, '44': {'1'}, '45': {'2'}, '46': {'8'}, '47': {'9', '7'}, '48': {'4'}, 
    '50': {'2', '1'}, '51': {'4'}, '52': {'8'}, '53': {'6', '9', '7'}, '54': {'6', '9'}, '55': {'6', '9', '7'}, '56': {'3', '1'}, '57': {'2', '3'}, '58': {'5'}, 
    '60': {'7'}, '61': {'6', '1'}, '62': {'5'}, '63': {'8'}, '64': {'2'}, '65': {'3'}, '66': {'9'}, '67': {'4'}, '68': {'6', '1'}, 
    '70': {'8'}, '71': {'6', '2', '1'}, '72': {'9', '2', '1'}, '73': {'4'}, '74': {'7'}, '75': {'6', '9', '1'}, '76': {'3', '1'}, '77': {'5'}, '78': {'6', '3', '1'}, 
    '80': {'4'}, '81': {'6', '3', '1'}, '82': {'9', '3', '1'}, '83': {'6', '9'}, '84': {'5'}, '85': {'6', '9', '1'}, '86': {'2'}, '87': {'8'}, '88': {'7'}}


def rellena(sudoku, usar_ejemplo=False, tabla_ejemplo=facil) -> None:
    """ Rellena la tabla del SUDOKU con valores que pide al usuario
        o que saca de tablas de ejemplo"""
    def ruler():
        """ Guía para ayudar a ver los caracteres que hemos escrito."""
        print('  ', end='')
        for i in range(FILAS):
            print(i+1, end='')
        print()

    if usar_ejemplo:
        for f in range(FILAS):
            for c in range(FILAS):
                sudoku[f'{f}{c}'] = set(tabla_ejemplo[f][c]).intersection(VALIDOS)
    else:
        print('Escribe los números fila a fila sin separación, si es un espacio escribe un 0')
        ruler()
        for f in range(FILAS):
            fila = list()
            # pequeña comprobación de que llena todos los espacios necesarios en cada fila
            while len(fila) != FILAS:
                fila = list(input(f'{f+1}:'))
                if len(fila) != FILAS:
                    continue
            for c in range(FILAS):
                sudoku[f'{f}{c}'] = set(fila[c])


def he_terminado():
    """ Comprobar si ya se ha resuelto el sudoku,
        solo debe de haber 1 número en cada por número por fila/columna"""
    for sentido in 'por_filas', 'por_columnas':
        for f in range(FILAS):
            numbers = dict()
            for c in range(FILAS):
                fc = sentido_comprobacion(sentido, f, c)
                if len(sudoku[fc]) > 1:
                    return False

                ind = str(sudoku[fc])
                numbers.setdefault(ind, 0)
                numbers[ind] += 1

                if numbers[ind] > 1:
                    return False

    for f in range(0, FILAS, LADO):
        for c in range(0, FILAS, LADO):

            numbers = dict()
            for fc in coords_cuad(f, c):
                if len(sudoku[fc]) > 1:
                    return False

                ind = str(sudoku[fc])
                numbers.setdefault(ind, 0)
                numbers[ind] += 1

                if numbers[ind] > 1:
                    return False

    return True


def comp_sudoku(f, c) -> bool:
    """ Comprueba cómo va el resultado del último paso de la recursión.
        Sólo comprueba la fila, la columna y el cuadrado implicados.
        Retorna si vamos bien - True - o si hay conflicto - False.
    """

    for sentido in 'por_filas', 'por_columnas':
        esta_fila = dict()
        for col in range(FILAS):

            if sentido == 'por_filas':
                fc = f'{f}{col}'
            else:
                fc = f'{col}{c}'

            if len(sudoku[fc]) > 1:
                continue

            num = str(sudoku[fc])
            esta_fila.setdefault(num, 0)
            esta_fila[num] += 1

            if esta_fila[num] > 1:
                # print(f'\txxx Esta fila:\t{esta_fila}')
                esta_fila.clear()
                return False

    esta_fila = dict()
    for fc in coords_cuad(f, c):
        if len(sudoku[fc]) > 1:
            continue

        num = str(sudoku[fc])
        esta_fila.setdefault(num, 0)
        esta_fila[num] += 1

        if esta_fila[num] > 1:
            # print(f'\txxx Esta fila:\t{esta_fila}')
            esta_fila.clear()
            return False

    return True
        

def print_hasta_ahora(f, c) -> None:
    """ Imprime lo que ha encotrado hasta ahora. Solo para trazas."""
    # Solo para esta fila y esta columna
    for sentido in 'por_filas', 'por_columnas':
        print(f'\t{sentido}:\t', end='')
        for col in range(FILAS):
            if sentido == 'por_filas':
                fc = f'{f}{col}'
            else:
                fc = f'{col}{c}'
            print(str(sudoku[f'{fc}'])+ '|', end='')
        print()


def recursion(f, c) -> bool:
    """ Busca la respuesta por recursión de las posibilidades anotadas a lápiz.
        Busca desde f, c, idealmente 0, 0, hasta FILAS, FILAS.
    """
    if f == FILAS:
        print('***FIN***')
        # imprimir_todo(sudoku)
        return True
    
    fc = sentido_comprobacion('por_filas', f, c)
    valores = sudoku[fc].copy()
    
    for valor in valores:
        # print(f'+Celda {fc}:++++\tElegido {valor} entre {valores}')
        # print(f'{fc}:+++++++++++\tElegido {valor} entre {valores}')
        sudoku[fc].clear()
        sudoku[fc].add(valor)
        # input(f'Valores={valores}\tsudoku[{fc}]={sudoku[fc]}\tvalor={valor}')
        # print_hasta_ahora(f,c)
        if not comp_sudoku(f, c):
            # print('\t########### No_Ok.')
            continue
        # Mirar la siguiente celda.
        if recursion(f+((c+1)//FILAS), (c+1)%FILAS):
            return True
    sudoku[fc].clear()
    sudoku[fc].update(valores)
    return False


def coords_cuad(f, c) ->list:
    """ devuelve todas las coordenadas de un cuadrado que contenga f, c."""
    coord = list()
    for fil in range((int(f)//LADO)*LADO,((int(f)//LADO)+1)*LADO):
        for col in range((int(c)//LADO)*LADO,((int(c)//LADO)+1)*LADO):
            # print(f'{fil}{col}', end=' ')
            coord.append(f'{fil}{col}')
    
    """ con comprehension, en este caso es demasiado complicado, mejor verlo con 2 x for.
    coord = [ [ f'{fil}{col}' for col in range((int(c)//LADO)*LADO,((int(c)//LADO)+1)*LADO) ] 
                for fil in range((int(f)//LADO)*LADO,((int(f)//LADO)+1)*LADO) ]
    """
    return coord


def anotar_a_lapiz():
    """ Si no hay ningún número en el sudoku, poner todos los VALIDOS."""
    # Relleno con todos los números del 1 al 9.
    for f in range(FILAS):
        for c in range(FILAS):
            fc = f'{f}{c}'
            if sudoku[fc] == set():
                sudoku[fc] = VALIDOS.copy()


def limpiar_lapiz(destaca):
    """ Limpia las celdas encontradas de las anotadas a lápiz
        y luego busca celdas naked.
    """
    def borra(encontrados, fc, destaca) -> bool:
        """ Borra los encontrados de sudoku[fc]
            actualiza destaca por si hubiese que imprimir
            retorna bool por si se ha descubierto un nuevo número.
        """
        if len(sudoku[fc]) == 1:
            return False
        len_before = len(sudoku[fc])
        sudoku[fc].difference_update(encontrados)
        if len_before > len(sudoku[fc]) and len(sudoku[fc]) == 1:
            destaca.append(fc)
            return True
        return False


    def limpia_encontrados(destaca):
        """ Borra de las casillas a lápiz los que ya se han encontrado."""
        cambiado = False
        for sentido in SENTIDOS:
            for f in range(FILAS):
                encontrados = set()
                for c in range(FILAS):
                    fc = sentido_comprobacion(sentido, f, c)
                    if len(sudoku[fc]) == 1:
                        encontrados.update(sudoku[fc])
                # destaca = list()
                for c in range(FILAS):
                    fc = sentido_comprobacion(sentido, f, c)
                    cambiado = cambiado or borra(encontrados, fc, destaca)
                # imprimir_todo(sudoku, destaca)
                # input()

        for f in range(0, FILAS, LADO):
            for c in range(0, FILAS, LADO):
                encontrados = set()
                for fc in coords_cuad(f, c):
                    if len(sudoku[fc]) == 1:
                        encontrados.update(sudoku[fc])
                # destaca = list()
                for fc in coords_cuad(f, c):
                    cambiado = cambiado or borra(encontrados, fc, destaca)
                # imprimir_todo(sudoku, destaca)
                # input()
    
        return cambiado


    def clean_naked(fc, keys, destaca) -> bool:
        """ Para la lista de keys (fila/columna(cuadrado) mira si sudoku[fc] es naked."""
        valores_fc = sudoku[fc].copy()
        for key in keys:
            valores_fc.difference_update(sudoku[key])
            
        if len(valores_fc) == 1:
            sudoku[fc] = valores_fc.copy()
            destaca.append(fc)
            return True
        
        return False


    def check_naked(fil, col, destaca):
        """ Crea la lista de claves a comprobar."""
        if len(sudoku[f'{fil}{col}']) == 1:
            return False

        keys_filas = [f'{fil}{c}' for c in range(FILAS)]
        keys_colum = [f'{f}{col}' for f in range(FILAS)]
        keys_cuadr = list()
        keys_cuadr = coords_cuad(fil, col)

        fc = f'{fil}{col}'
        
        keys_filas.remove(fc)
        keys_colum.remove(fc)
        keys_cuadr.remove(fc)

        if clean_naked(fc, keys_filas, destaca):
            return True

        if clean_naked(fc, keys_colum, destaca):
            return True

        if clean_naked(fc, keys_cuadr, destaca):
            return True
        
        return False


    def limpia_naked(destaca) -> bool:
        """ Recorre todo el sudoku buscando celdas Naked
            Naked: celdas en las que aunque haya anotados a lápiz, en esa fila/columna/cuadrado
            hay algún número que sólo está anotado ahí.
        """
        cambiado = False
        for f in range(FILAS):
            for c in range(FILAS):
                cambiado = cambiado or check_naked(f, c, destaca)

        return cambiado

    cambiado = True
    # destaca = list()
    while cambiado:
        cambiado = False
        cambiado = cambiado or limpia_encontrados(destaca)
        cambiado = cambiado or limpia_naked(destaca)
    

def sentido_comprobacion(sentido, ff, cc) -> str:
    """ Devuelve la fc adecuada según el sentido sea por_filas o por_columnas."""
    if sentido == 'por_filas':
        return f'{ff}{cc}'
    else:
        return f'{cc}{ff}'


def imprimir_todo(sudoku, destacar=list()):
    """ Imprime el sudoku, si hay lista a destacar, destaca dichas celdas."""
    def print_horizontal(caracter):
        for _ in range(FILAS):
            print('+'+ caracter*(LADO+2), end='')
        print('+')

    for fila in range(FILAS):
        # Por filas
        if fila%LADO == 0:
            print_horizontal('=')
        else:
            print_horizontal('.')
        for linea in range(LADO):
            # Por cada línea de cada celda
            for columna in range(FILAS):
                # Por columnas
                if columna%LADO == 0:
                    print('#', end='')
                else:
                    print('.', end='')
                
                fc = f'{fila}{columna}'
                # if list(sudoku[fc])[0] in VALIDOS:
                if len(sudoku[fc]) == 1:
                    # Hay un número anotado
                    relleno = ' '
                    if fc in destacar:
                        relleno = '.'

                    if linea == 1:
                        print(relleno*2 + list(sudoku[fc])[0] + relleno*2,end='')
                    else:
                        print(relleno*(LADO+2), end='')
                elif len(sudoku[fc]) > 1:
                    # Escribimos las posibilidades de la casilla ordenadas según "línea"
                    print(' ', end='')
                    for ind in range(LADO*linea,LADO*(linea+1)):
                        if str(ind+1) in sudoku[fc]:
                            print(ind+1, end='')
                        else:
                            print(' ', end='')
                    print(' ', end='')
                else:
                    # print(' ' + ' '*LADO + ' ', end='')
                    # Error, cada casilla tiene que tener algún valor, o varios.
                    print("X"*(LADO+2), end='')
            print('#')
    print_horizontal('=')


ej = list()
ej = facil.copy()
sudoku = dict()


for tabla in [muy_facil, facil, normal, dificil, muy_dificil, extremo]:
    destaca = list()
    print(f'Tabla: {tabla}:')
    rellena(sudoku, usar_ejemplo=True, tabla_ejemplo=tabla)
    anotar_a_lapiz()
    imprimir_todo(sudoku)
    
    mid_start_time = time.time()
    
    limpiar_lapiz(destaca)
    # imprimir_todo(sudoku, destaca)
    recursion(0,0)

    print("Esta tabla --- %s seconds ---" % (time.time() - mid_start_time))
    
    print(f'¿He ternimado? {str(he_terminado())}')
    
print("Total --- %s seconds ---" % (time.time() - start_time))
