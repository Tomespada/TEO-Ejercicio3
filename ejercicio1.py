from datetime import date
def fecha_en_intervalo(fecha, fecha_min, fecha_max):
    res = False 

    if (fecha_min is None or fecha >= fecha_min) and \
        (fecha_max is None or fecha <=fecha_max):
        res = True

    return 

