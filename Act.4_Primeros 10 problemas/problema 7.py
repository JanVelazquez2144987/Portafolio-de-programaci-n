def par_impar_multiplo(num1, num2):
    if num1 % 2 == 0:
        print(f"{num1} es par.")
    else:
        print(f"{num1} es impar.")
    
    if num1 % num2 == 0:
        print(f"{num1} es múltiplo de {num2}.")
    else:
        print(f"{num1} no es múltiplo de {num2}.")

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

par_impar_multiplo(numero1, numero2)