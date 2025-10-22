
'''
Precios de las entradas para personas con edades 8, 18, 25, 44, 64, 65, 70 
(precio normal de la entrada: 6€):
3.0, 3.0, 6.0, 6.0, 6.0, 3.0, 3.0
'''

def calcula_precios(precio_normal, edades):
    precios = []
    for edad in edades:
        precio = calcula_precios(precio_normal,edad)
        precios.add(precio)
    return precios