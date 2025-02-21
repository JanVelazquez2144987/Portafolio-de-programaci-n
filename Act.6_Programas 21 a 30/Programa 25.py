import matplotlib.pyplot as plt # type: ignore

def generar_histograma(datos):
    plt.hist(datos, bins=10, edgecolor='black')
    plt.title("Histograma de Datos")
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.show()
