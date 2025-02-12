def contar_vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    num_vocales = sum(1 for c in cadena if c in vocales)
    num_consonantes = sum(1 for c in cadena if c in consonantes)
    return num_vocales, num_consonantes

print(contar_vocales_consonantes("Hola Mundo"))  # (4, 5)
