import math

def area_circunferencia(radio):
    area = math.pi * radio ** 2
    circunferencia = 2 * math.pi * radio
    return area, circunferencia

radio = float(input("Ingrese el radio del círculo: "))
area, circunferencia = area_circunferencia(radio)
print(f"El área del círculo es: {area}")
print(f"La circunferencia del círculo es: {circunferencia}")