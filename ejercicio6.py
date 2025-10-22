
'''
Precios de las entradas para personas con edades 8, 18, 25, 44, 64, 65, 70 
(precio normal de la entrada: 6€):
3.0, 3.0, 6.0, 6.0, 6.0, 3.0, 3.0
'''

def calcula_precios(precio_normal, edades):
    precios = []
    for edad in edades:
        precio = calcula_precio(precio_normal, edad)
        precios.append(precio)
    return precios

def calcula_precio(precio_normal,edad):
    if edad <= 18 or edad >=65:
        precio = precio_normal/2
    else:
        precio = precio_normal
    return precio 

if __name__ == '__main__':
    edades = [8,18,25,44,64,65,70]
    precio_normal=6
    precios = calcula_precios(precio_normal,edades)
    for edad, precio in zip(edades,precios):
        print(f"El precio para {edad} años es {precio}€")