import math

# Funciones para áreas
def area_circulo(radio):
    return math.pi * radio ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

# Funciones para volúmenes
def volumen_cilindro(radio, altura):
    return math.pi * radio ** 2 * altura

def volumen_esfera(radio):
    return (4/3) * math.pi * radio ** 3

def volumen_cono(radio, altura):
    return (1/3) * math.pi * radio ** 2 * altura
