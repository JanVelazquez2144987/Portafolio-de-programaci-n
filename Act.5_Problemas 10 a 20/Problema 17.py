# Pila
class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
    
    def esta_vacia(self):
        return len(self.items) == 0

pila = Pila()
pila.apilar(1)
pila.apilar(2)
print(pila.desapilar())  # 2

# Cola
class Cola:
    def __init__(self):
        self.items = []
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
    
    def esta_vacia(self):
        return len(self.items) == 0

cola = Cola()
cola.encolar(1)
cola.encolar(2)
print(cola.desencolar())  # 1

# Lista enlazada
class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.head = None
    
    def agregar(self, data):
        nuevo_nodo = Nodo(data)
        nuevo_nodo.siguiente = self.head
        self.head = nuevo_nodo
    
    def mostrar(self):
        nodo = self.head
        while nodo:
            print(nodo.data)
            nodo = nodo.siguiente

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.mostrar()  # 2, 1
