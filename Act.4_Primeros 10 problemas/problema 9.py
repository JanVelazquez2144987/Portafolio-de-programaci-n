def numeros_pares_impares(limite):
    pares = [i for i in range(2, limite + 1, 2)]
    impares = [i for i in range(1, limite + 1, 2)]
    return pares, impares

limite = int(input("Ingrese el límite: "))
pares, impares = numeros_pares_impares(limite)
print(f"Números pares hasta {limite}: {pares}")
print(f"Números impares hasta {limite}: {impares}")