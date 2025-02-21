import numpy as np # type: ignore

# Crear matrices
def crear_matriz(filas, columnas, valor=0):
    return np.full((filas, columnas), valor)

# Operar con matrices
def sumar_matrices(matriz1, matriz2):
    return np.add(matriz1, matriz2)

def multiplicar_matrices(matriz1, matriz2):
    return np.dot(matriz1, matriz2)
