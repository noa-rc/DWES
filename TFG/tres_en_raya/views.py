from django.shortcuts import render

LINEAS_GANADORAS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def hay_ganador(tablero, marca):
    for a, b, c in LINEAS_GANADORAS:
        if tablero[a] == tablero[b] == tablero[c] == marca:
            return True
    return False


def tres_en_raya(request):
    tablero = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    turno = 'X'
    mensaje = 'Turno de X'
    terminado = False

    if request.method == 'POST':
        tablero_texto = request.POST.get('tablero')
        turno = request.POST.get('turno')
        posicion = int(request.POST.get('posicion'))
        tablero = [c for c in tablero_texto if c in 'XO-']

        if tablero[posicion] == '-':
            tablero[posicion] = turno
            if hay_ganador(tablero, turno):
                mensaje = 'Ha ganado ' + turno
                terminado = True
            elif '-' not in tablero:
                mensaje = 'Empate'
                terminado = True
            else:
                if turno == 'X':
                    turno = 'O'
                else:
                    turno = 'X'
                mensaje = 'Turno de ' + turno
        else:
            mensaje = 'Casilla ocupada. Turno de ' + turno

    contexto = {
        'tablero': tablero,
        'turno': turno,
        'mensaje': mensaje,
        'terminado': terminado,
    }
    return render(request, 'tres_en_raya/tres_en_raya.html', contexto)