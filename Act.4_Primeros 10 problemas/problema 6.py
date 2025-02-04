def interes_compuesto(capital, tasa, tiempo):
    return capital * (1 + tasa / 100) ** tiempo

capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa de interés anual (%): "))
tiempo = int(input("Ingrese el tiempo en años: "))

monto = interes_compuesto(capital, tasa, tiempo)
print(f"El monto final después de {tiempo} años es: {monto}")