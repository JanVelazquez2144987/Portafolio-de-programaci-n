# Paradigma Imperativo
x = 5
if x > 3:
    print("X es mayor que 3")

# Paradigma Estructurado
def calcular_area(base, altura):
    return base * altura

# Paradigma Modular
def saludo(nombre):
    return f"Hola, {nombre}!"

# Paradigma Orientado a Objetos
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

# Uso de los paradigmas
print(calcular_area(5, 3))
print(saludo("Juan"))
persona = Persona("Ana")
persona.saludar()
