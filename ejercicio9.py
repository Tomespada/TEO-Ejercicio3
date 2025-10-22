from collections import namedtuple
Persona = namedtuple("Persona", "nombre, edad")

def lee_personas(n):
    personas = []
    for i in range(n):
        print(f"Persona {i+1}")
        nombre = input("   Nombre : ")
        edad = int(input("   Edad: "))
        persona = Persona(nombre,edad)
        personas.append(persona)
    return personas 

def edad_media(peronas):
    suma = 0
    for p in personas:
        suma +=p.edad
    if len(personas)>0:
        media = suma / len(lee_personas)
    else:
        media = None 
    return media 

def mayores_18(personas):
    nombres = set()
    for p in personas:
        if p.edad >=18:
            nombres.append(p.nombre)
    return sorted(nombres, reverse=True)

def persona_mas_joven(personas):
    minimo = None
    for p in personas:
        if minimo is None or p.edad < minimo:
            minimo = p.edad
        return minimo.nombre
    
def persona_mas_joven_2(personas):
    return min(personas, key = lambda p:p.edad )

def todas_mayores_edad(personas):
    res = True 
    for p in personas:
        if p.edad < 18:
            res = False 
            break
        return res 
    

def alguna_mayor_edad(personas):
    res = False
    for p in personas:
        if p.edad >= 18:
            res =True 
            break 


if __name__ == '__main__':
    personas = lee_personas(3)
    print(personas)
    print(edad_media(personas))
    print(personas_mayores(personas ))