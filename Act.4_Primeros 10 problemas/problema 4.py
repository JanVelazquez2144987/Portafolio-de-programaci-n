def fibonacci(n):
    secuencia = [0, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

terminos = int(input("Ingrese el número de términos de la secuencia de Fibonacci: "))
print(f"La secuencia de Fibonacci es: {fibonacci(terminos)}")
