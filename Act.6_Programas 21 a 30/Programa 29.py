import statistics

def analizar_datos(datos):
    media = statistics.mean(datos)
    mediana = statistics.median(datos)
    desviacion_estandar = statistics.stdev(datos)
    
    return media, mediana, desviacion_estandar

# Ejemplo de uso
datos = [10, 20, 30, 40, 50]
media, mediana, desvio = analizar_datos(datos)
print(f"Media: {media}, Mediana: {mediana}, Desviación Estándar: {desvio}")
