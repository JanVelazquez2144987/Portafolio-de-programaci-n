def analizar_texto(texto):
    palabras = texto.split()
    total_palabras = len(palabras)
    palabras_unicas = set(palabras)
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    palabra_mas_frecuente = max(frecuencia, key=frecuencia.get)
    frecuencia_max = frecuencia[palabra_mas_frecuente]

    # Resultados
    print(f"Total de palabras: {total_palabras}")
    print(f"Palabras únicas: {len(palabras_unicas)}")
    print("Frecuencia de cada palabra:", frecuencia)
    print(f"La palabra más frecuente es '{palabra_mas_frecuente}' con {frecuencia_max} ocurrencias")

# Solicitar texto al usuario
texto = input("Ingresa un texto: ")
analizar_texto(texto)
