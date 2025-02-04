def calculadora():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    operacion = input("Ingrese el número de la operación (1/2/3/4): ")
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    if operacion == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operacion == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operacion == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operacion == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("No se puede dividir entre 0.")
    else:
        print("Operación no válida.")

calculadora()