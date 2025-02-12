# Búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1

# Búsqueda binaria
def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1

lista = [1, 3, 5, 7, 9, 11]
print(busqueda_lineal(lista, 5))  # 2
print(busqueda_binaria(lista, 5))  # 2
