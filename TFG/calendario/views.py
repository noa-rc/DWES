from datetime import date
from django.shortcuts import render

MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio',
         'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

DIAS_SEMANA = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes',
               'sábado', 'domingo']


def calendario(request, fecha):
    partes = fecha.split('-')

    try:
        if len(partes) != 3 or len(partes[2]) != 4:
            raise ValueError

        mi_dia = int(partes[0])
        mi_mes = int(partes[1])
        mi_ano = int(partes[2])
        dia_semana = DIAS_SEMANA[date(mi_ano, mi_mes, mi_dia).weekday()]
    except ValueError:
        return render(request, 'calendario/error.html', {'fecha': fecha}, status=400)

    mensaje = f'Ese día cae en {dia_semana}'

    return render(request, 'calendario/fecha.html', {
        'dia': mi_dia,
        'mes': MESES[mi_mes - 1],
        'ano': mi_ano,
        'mensaje': mensaje,
    })