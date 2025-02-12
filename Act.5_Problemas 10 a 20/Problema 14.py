# Método de ordenamiento por burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Método de ordenamiento por selección
def seleccion(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

print(burbuja([64, 34, 25, 12, 22, 11, 90]))  # Ordena la lista con burbuja
print(seleccion([64, 34, 25, 12, 22, 11, 90]))  # Ordena la lista con selección
