def convertir_temperatura(valor, escala_origen, escala_destino):
    if escala_origen == "Celsius":
        if escala_destino == "Fahrenheit":
            return (valor * 9/5) + 32
        elif escala_destino == "Kelvin":
            return valor + 273.15
    elif escala_origen == "Fahrenheit":
        if escala_destino == "Celsius":
            return (valor - 32) * 5/9
        elif escala_destino == "Kelvin":
            return (valor - 32) * 5/9 + 273.15
    elif escala_origen == "Kelvin":
        if escala_destino == "Celsius":
            return valor - 273.15
        elif escala_destino == "Fahrenheit":
            return (valor - 273.15) * 9/5 + 32

print(convertir_temperatura(100, "Celsius", "Fahrenheit"))  # 212.0
