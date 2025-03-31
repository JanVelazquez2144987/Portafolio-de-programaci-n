import statistics

def calcular_estadisticas(*args):
    promedio = sum(args) / len(args)
    mediana = statistics.median(args)
    desviacion = statistics.stdev(args)
    
    return promedio, mediana, desviacion

# Ejemplo de uso:
numeros = [float(x) for x in input("Ingresa una lista de números separados por espacio: ").split()]
promedio, mediana, desviacion = calcular_estadisticas(*numeros)
print(f"Promedio: {promedio}, Mediana: {mediana}, Desviación estándar: {desviacion}")
