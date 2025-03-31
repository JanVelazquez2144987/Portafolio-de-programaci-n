import random

# Quicksort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivot]
    derecha = [x for x in lista if x > pivot]
    return quicksort(izquierda) + [pivot] + quicksort(derecha)

# Búsqueda binaria
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Ejemplo de uso:
numeros = [random.randint(1, 100) for _ in range(10)]
print("Lista original:", numeros)
numeros_ordenados = quicksort(numeros)
print("Lista ordenada:", numeros_ordenados)
busqueda = int(input("Ingresa un número para buscar: "))
resultado = busqueda_binaria(numeros_ordenados, busqueda)
if resultado != -1:
    print(f"El número {busqueda} se encuentra en la posición {resultado}")
else:
    print("El número no fue encontrado")
