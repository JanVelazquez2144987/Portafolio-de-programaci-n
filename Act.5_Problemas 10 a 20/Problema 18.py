import cmath

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a)
    return raiz1, raiz2

print(resolver_ecuacion_cuadratica(1, -3, 2))  # (2.0, 1.0)
