# conversor.py
def kilometros_a_millas(km):
    return km * 0.621371

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def litros_a_galones(litros):
    return litros * 0.264172

# Programa principal
import conversor # type: ignore

km = float(input("Ingresa kilómetros: "))
celsius = float(input("Ingresa grados Celsius: "))
litros = float(input("Ingresa litros: "))

print(f"{km} km son {conversor.kilometros_a_millas(km)} millas")
print(f"{celsius} °C son {conversor.celsius_a_fahrenheit(celsius)} °F")
print(f"{litros} litros son {conversor.litros_a_galones(litros)} galones")
